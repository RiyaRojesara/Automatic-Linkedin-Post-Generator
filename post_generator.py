from llm_helper import get_llm
from few_shot import FewShotPosts
import re

few_shot = None  # lazy init

VARIANTS = ["Story-based", "Value-based", "Question-based"]


def get_length_str(length):
    return {
        "Short": "1 to 5 lines",
        "Medium": "6 to 10 lines",
        "Long": "11 to 15 lines"
    }.get(length, "")


def get_tone_instruction(tone):
    return {
        "Professional": "Professional, clear, confident. Polished language. No slang.",
        "Humble": "Humble, grounded, relatable. Acknowledge learning and growth.",
        "Bold": "Bold, confident, opinionated. High energy.",
        "Storyteller": "Narrative-driven. Relatable moment → insight."
    }.get(tone, "")


def get_variant_instruction(variant):
    return {
        "Story-based": "Start with a personal story. Emotional hook. Short paras + emojis.",
        "Value-based": "Give clear takeaways or tips. Bullets + actionable value.",
        "Question-based": "Open with a strong question. Encourage comments."
    }.get(variant, "")


def format_post_for_linkedin(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    out = ""
    for i in range(0, len(sentences), 2):
        out += " ".join(sentences[i:i+2]) + "\n\n"
    return out.strip()


def remove_hashtags(text):
    lines = text.split("\n")
    clean_lines = [l for l in lines if not l.strip().startswith("#")]
    return "\n".join(clean_lines).strip()


def get_prompt(length, language, tag, tone, variant, asset_ctx):
    global few_shot
    if few_shot is None:
        few_shot = FewShotPosts()

    prompt = f"""
Generate a HIGH-ENGAGEMENT LinkedIn post. No preamble.

RULES:
- First line MUST be a hook (🔥 or 🚀)
- Short paragraphs (max 2 lines)
- Emojis allowed (professional)
- End with CTA starting 👇
- NO hashtags in post body

ASSETS:
- Link provided: {asset_ctx["has_link"]}
- Images provided: {asset_ctx["image_count"]}
- PDF provided: {asset_ctx["has_pdf"]}

INSTRUCTIONS:
- If link exists → add a clear CTA
- If images exist → hint visual context (e.g. “see image 👇”)
- If PDF exists → highlight value, not details

TONE:
{get_tone_instruction(tone)}

VARIANT STYLE:
{get_variant_instruction(variant)}

Topic: {tag}
Length: {get_length_str(length)}
Language: {language}
"""

    examples = few_shot.get_filtered_posts(length, language, tag)
    for i, ex in enumerate(examples[:2]):
        prompt += f"\n\nExample {i+1}:\n{ex['text']}"

    return prompt


def generate_post(llm, length, language, tag, tone, variant, asset_ctx):
    prompt = get_prompt(length, language, tag, tone, variant, asset_ctx)
    response = llm.invoke(prompt)
    clean_post = format_post_for_linkedin(response.content.strip())
    return remove_hashtags(clean_post)


def generate_hashtags(llm, post_text):
    prompt = f"""
Generate LinkedIn hashtags ONLY.

RULES:
- Each must start with #
- Space separated
- CamelCase
- No explanation

Post:
{post_text}
"""
    return llm.invoke(prompt).content.strip()


def force_hashtags(text):
    tags = []
    for w in text.replace("\n", " ").split():
        if not w.startswith("#"):
            w = "#" + w
        tags.append(w)
    return " ".join(dict.fromkeys(tags))


def generate_ab_variants(
    groq_key,
    length,
    language,
    tag,
    tone,
    asset_ctx
):
    llm = get_llm(groq_key)  # 🔥 USER-BASED LLM

    results = {}
    for variant in VARIANTS:
        post = generate_post(
            llm, length, language, tag, tone, variant, asset_ctx
        )
        hashtags = force_hashtags(
            generate_hashtags(llm, post)
        )
        results[variant] = {
            "post": post,
            "hashtags": hashtags
        }

    return results
