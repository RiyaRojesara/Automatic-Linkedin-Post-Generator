import streamlit as st
from post_generator import generate_ab_variants
from preview_card import render_preview_card
from assets import build_asset_context
from storage import save_images, save_pdf

st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼")

st.title("💼 LinkedIn Post Generator")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    groq_api_key = st.text_input("Groq API Key", type="password")

    st.divider()

    length = st.selectbox("Length", ["Short", "Medium", "Long"])
    language = st.selectbox("Language", ["English", "Hinglish"])

    try:
        from few_shot import FewShotPosts
        few_shot = FewShotPosts()
        available_tags = few_shot.get_tags()
        tag = st.selectbox("Topic/Tag", available_tags)
    except Exception:
        tag = st.text_input("Topic/Tag", "Career")

    tone = st.selectbox("Tone", ["Professional", "Humble", "Bold", "Storyteller"])

    st.divider()

    link = st.text_input("Link (optional)")
    images = st.file_uploader("Images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    pdf = st.file_uploader("PDF (optional)", type=["pdf"])

# Generate
if st.button("🚀 Generate Posts", type="primary"):
    if not groq_api_key:
        st.error("❌ Please enter your Groq API Key")
    else:
        with st.spinner("✨ Generating posts..."):
            try:
                image_paths = save_images(images) if images else []
                pdf_path = save_pdf(pdf) if pdf else None
                asset_ctx = build_asset_context(link, image_paths, pdf_path)

                results = generate_ab_variants(
                    groq_api_key,
                    length.lower(),
                    language,
                    tag,
                    tone,
                    asset_ctx
                )

                st.session_state.results = results
                st.session_state.image_paths = image_paths
                st.session_state.link = link

                st.success("✅ Posts generated!")

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Display results
if "results" in st.session_state:
    st.header("📊 Generated Variants")

    results = st.session_state.results
    image_paths = st.session_state.get("image_paths", [])
    link = st.session_state.get("link", "")

    tabs = st.tabs(list(results.keys()))

    for i, (variant_name, variant_data) in enumerate(results.items()):
        with tabs[i]:
            st.subheader(f"✨ {variant_name}")

            render_preview_card(
                variant_data["post"],
                variant_data["hashtags"],
                image_paths,
                link
            )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:
                full_text = f"{variant_data['post']}\n\n{variant_data['hashtags']}"
                st.text_area("📝 Copy this:", full_text, height=200, key=f"ta_{i}")

            with col2:
                full_text = f"{variant_data['post']}\n\n{variant_data['hashtags']}"
                st.download_button(
                    "⬇️ Download as .txt",
                    full_text,
                    file_name=f"{variant_name.replace(' ', '_')}.txt",
                    key=f"dl_{i}"
                )
                st.link_button("🔗 Open LinkedIn", "https://www.linkedin.com/feed/")
                st.info("💡 Copy text → Open LinkedIn → Paste → Post!")

st.divider()
st.caption("Made with ❤️ using Streamlit + Groq")