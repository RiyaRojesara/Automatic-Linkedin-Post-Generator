import streamlit as st
def render_preview_card(post, hashtags, images=None, link=None):
    with st.container(border=True): 
        # 1️⃣ POST 
        st.markdown(post) 
        # 2️⃣ HASHTAGS 
        st.markdown(hashtags) 
        # 3️⃣ IMAGES (LAST)
        if images: 
            cols = st.columns(2) 
            for i, img in enumerate(images[:4]): 
                cols[i % 2].image(img, use_container_width=True)
                





#def render_preview_card(post, hashtags, images=None, link=None):
#    with st.container(border=True):
#
#        # ---------- POST TEXT ----------
#        st.markdown(post)
#
#        # ---------- HASHTAGS ----------
#        st.markdown(hashtags)
#
#        # ---------- IMAGES (LAST) ----------
#        
#
#        if images:
#            if len(images) == 1:
#                st.image(images[0], use_container_width=True)
#
#            elif len(images) == 2:
#                col1, col2 = st.columns(2)
#                col1.image(images[0], use_container_width=True)
#                col2.image(images[1], use_container_width=True)
#
#            elif len(images) >= 3:
#                col1, col2 = st.columns(2)
#                col1.image(images[0], use_container_width=True)
#                col2.image(images[1], use_container_width=True)
#
#                col3, col4 = st.columns(2)
#                col3.image(images[2], use_container_width=True)
#                if len(images) > 3:
#                    col4.image(images[3], use_container_width=True)
#
#        # ---------- LINK (OPTIONAL) ----------
#        if link:
#            st.markdown(f"🔗 {link}")
