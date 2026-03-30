# 💼 LinkedIn Post Generator

An AI-powered LinkedIn post generator built with **Streamlit** and **Groq (LLaMA 3.3 70B)**. Generate high-engagement LinkedIn posts in multiple styles, tones, and languages — instantly.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.3-purple?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-app-link.streamlit.app)

> **Note:** You'll need your own [Groq API Key](https://console.groq.com) to generate posts. It's free!

---

## ✨ Features

- 🤖 **AI-Powered Generation** — Uses LLaMA 3.3 70B via Groq for fast, high-quality posts
- 🎭 **3 Post Variants** — Story-based, Value-based, and Question-based styles generated simultaneously
- 🎨 **4 Tone Options** — Professional, Humble, Bold, Storyteller
- 🌐 **Multi-language** — English and Hinglish support
- 📏 **Length Control** — Short, Medium, Long post lengths
- 🏷️ **Topic/Tag Selection** — Smart tag selection based on real LinkedIn post data
- 📎 **Asset Support** — Attach links, images (JPG/PNG), and PDFs to influence post content
- 👀 **Live Preview** — See how your post looks before posting
- #️⃣ **Auto Hashtags** — Relevant hashtags generated separately
- ⬇️ **Download Option** — Save any post variant as a .txt file
- 🔗 **One-click LinkedIn** — Direct button to open LinkedIn feed

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Streamlit | Frontend UI |
| Groq API | LLM inference (LLaMA 3.3 70B) |
| LangChain | LLM chaining and prompting |
| Pandas | Data handling for few-shot examples |
| Python | Backend logic |

---

## 📁 Project Structure

```
linkedin-post-generator/
│
├── app.py                  # Main Streamlit app
├── post_generator.py       # Core post generation logic
├── llm_helper.py           # Groq LLM setup
├── few_shot.py             # Few-shot examples handler
├── assets.py               # Asset context builder
├── storage.py              # Image/PDF storage handler
├── preview_card.py         # Post preview UI component
├── requirements.txt        # Dependencies
│
└── data/
    └── processed_posts.json  # Few-shot LinkedIn post examples
```

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/RiyaRojesara/Automatic-Linkedin-Post-Generator.git
cd Automatic-Linkedin-Post-Generator
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Enter your Groq API Key in the sidebar**

Get your free API key from 👉 [console.groq.com](https://console.groq.com)

---

## 🎯 How to Use

1. Enter your **Groq API Key** in the sidebar
2. Select **Length**, **Language**, **Topic**, and **Tone**
3. Optionally add a **Link**, **Images**, or **PDF**
4. Click **🚀 Generate Posts**
5. View **3 different variants** in tabs
6. **Copy** or **Download** your favourite post
7. Open LinkedIn and paste!

---

## 📸 Screenshots

> _Add screenshots of your app here_

---

## 🙋‍♀️ Author

**Riya Rojesara**
- GitHub: [@RiyaRojesara](https://github.com/RiyaRojesara)

---

## ⚠️ Disclaimer

This tool generates post content only. Manual posting is recommended. Automated posting via bots may violate LinkedIn's Terms of Service.

---

⭐ **If you found this useful, give it a star!**
