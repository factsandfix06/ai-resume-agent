# 🤖 AI Resume Agent

An AI-powered resume assistant that answers questions about me using my resume and personal summary.

This project integrates a Large Language Model (LLM) with a simple chat interface so users can interactively ask questions and receive responses **as if they are speaking directly with me**.

The agent reads my resume and background information, constructs a system prompt, and uses an LLM to generate professional answers based only on that information.

---

# 🚀 Features

- AI-powered resume Q&A
- Answers interview-style questions based on resume data
- Uses an LLM to generate professional responses
- Simple chat interface using Gradio
- Resume parsing from PDF
- Personal summary injection for better context
- Secure API key management using environment variables

---

# 🧠 How It Works

1. The system loads my **resume PDF** and extracts text.
2. It loads a **personal summary** file containing additional context about me.
3. A **system prompt** is constructed describing who I am.
4. When a user asks a question:
- The message and chat history are sent to the LLM
- The LLM answers **in my voice** based on the resume information
5. The response is returned through a **chat interface**.

This allows users (or recruiters) to interactively explore my experience.

---

# 🛠 Tech Stack

- Python
- LLM API (DeepSeek / OpenAI compatible)
- Gradio (UI)
- PyPDF
- python-dotenv
- uv (Python dependency manager)

---

# 📂 Project Structure

```
ai-resume-agent
│
├── main.py
├── src/
│   ├── agent.py
│   ├── config.py
│   ├── data_loader.py
│   ├── prompt_builder.py
│   └── ui.py
│
├── data/
│   ├── resume.pdf
│   └── summary.txt
│
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```
git clone https://github.com/yourusername/ai-resume-agent.git
cd ai-resume-agent
```

---

## 2. Install Dependencies

Using **uv**:

```
uv sync
```

---

## 3. Configure Environment Variables

Create a `.env` file in the root directory:

```
DEEPSEEK_API_KEY=your_api_key_here
```

---

## 4. Run the Application

```
python main.py
```

This will launch the Gradio interface locally.

---

# 💬 Example Questions You Can Ask

- Tell me about yourself
- What technologies do you work with?
- What projects have you worked on?
- What is your experience with Java development?
- What are your strengths as a developer?

---

# 📸 Example Interaction

```
User: Tell me about yourself.

Agent:
Hi, I'm Neha Alex, a software engineer with experience in backend and frontend development.
I have worked with technologies like Java, Spring Boot, Angular, and REST APIs while building
scalable applications in an Agile environment.
```

---

# 🔐 Environment Variables

| Variable | Description |
|--------|--------|
| DEEPSEEK_API_KEY | API key used to access the LLM |

---

# 🌱 Future Improvements

- Add streaming responses
- Add voice interaction
- Deploy using FastAPI and Docker
- Deploy to cloud platforms (Cloud Run / AWS)
- Improve resume parsing using structured extraction
- Add recruiter-specific question prompts

---

# 👩‍💻 Author

**Neha Alex**

Software Engineer | Full Stack Developer | AI Enthusiast

---

# ⭐ Motivation

This project explores how LLMs can be used to create **interactive AI agents powered by personal data**.
It demonstrates practical AI integration, prompt engineering, and building lightweight AI tools using Python.

If you found this project interesting, feel free to ⭐ the repository!