import gradio as gr
from .agent import chat

def start_ui():
    interface = gr.ChatInterface(
        fn = lambda message, history:chat(message, history),
        title = "AI Resume Agent",
        description="Hi, This is Neha Alex's AI Resume Assistant \n\n"
        "You can ask me anything about Neha's experience, skills, or projects. \n"
        "If you're a recruiter, feel free to leave your name and email - Neha will get back to you!"
    )
    interface.launch()