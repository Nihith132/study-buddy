# 📚 Study Buddy AI Agent

**Study Buddy AI** is a personal AI assistant designed to help you learn, revise, and understand complex topics efficiently.  
It uses an **LLM (Large Language Model) API** to process your queries and provide intelligent, context-aware responses.  
The project is built in **Python** and can integrate with multiple LLM providers such as **OpenAI**, **Mistral**, **LLaMA**, or **any API key-based model**.

---

## ✨ Features

- 🔑 **Bring Your Own API Key** – Works with any LLM provider that supports an API.
- 📄 **Handles Long & Complex Inputs** – You can ask detailed and multi-part questions.
- 🧠 **Context-Aware Responses** – AI remembers the conversation flow during a session.
- 🎯 **Study-Oriented Design** – Tailored for learning, summarizing, and explaining concepts.
- 💻 **Web Interface** – Simple and user-friendly UI for easy interaction.
- ⚡ **Modular Code** – Logic separated from UI for easy customization.

---

## 📂 Project Structure

```
├── app.py                 # Flask (or Streamlit/FastAPI) web app to interact with the AI
├── study_buddy_logic.py   # Core AI logic, API calls, and response handling
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

---

## 🛠️ Requirements

- Python 3.8 or later
- An API key from your preferred LLM provider (e.g., OpenAI, Mistral, Hugging Face)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/study-buddy-ai.git
cd study-buddy-ai
```

2. **Set Up Environment Variables**
```bash
export LLM_API_KEY="your_api_key_here"
export LLM_PROVIDER="openai"   # or mistral, llama, etc.
```

3. **Run the App**
```bash
python app.py
```

4. Open your browser and go to:
```
http://localhost:5000
```

---

## ⚙️ Configuration

You can configure:
- **Model Name** (e.g., `gpt-3.5-turbo`, `mistral-7b-instruct`, etc.)
- **Max Tokens** for output length
- **Temperature** for creativity level

---

## 📌 Use Cases

- 📖 Study helper for summarizing long notes
- 📝 Answering conceptual questions
- 🗒 Generating revision flashcards
- 🧩 Breaking down complex topics into simpler parts

---


## 🤝 Contributing

Contributions are welcome!  
If you have improvements, new features, or bug fixes, please fork the repo and submit a pull request.

---

## 🙋 Author

**Arramareddy Nihith Reddy**  
💼 GitHub: [yourusername]((https://github.com/Nihith132))  
📧 Email: your.email@example.com

---

⭐ If you found this project helpful, consider giving it a star on GitHub!
