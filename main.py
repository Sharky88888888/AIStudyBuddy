import os
import openai
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from dotenv import load_dotenv

# --- Load API key securely ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Database Setup ---
conn = sqlite3.connect("study_data.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    topic TEXT,
    correct INTEGER,
    total INTEGER
)
""")
conn.commit()

# --- Quiz Generation ---
def generate_questions(topic, num_questions):
    prompt = (
        f"Create {num_questions} multiple choice questions about {topic}. "
        "Each question should have 4 options (A–D) and indicate the correct answer."
    )
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=600
    )
    return response.choices[0].text.strip()

# --- UI Logic ---
def start_quiz():
    topic = topic_entry.get()
    if not topic:
        messagebox.showerror("Error", "Enter a topic first!")
        return

    try:
        num_questions = int(simpledialog.askstring("Number of Questions", "How many questions?"))
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    quiz_text.delete(1.0, tk.END)
    quiz_text.insert(tk.END, "Generating questions... please wait.\n")
    root.update()

    try:
        questions = generate_questions(topic, num_questions)
        quiz_text.delete(1.0, tk.END)
        quiz_text.insert(tk.END, questions)
    except Exception as e:
        messagebox.showerror("API Error", f"Error generating questions:\n{e}")

# --- UI Setup ---
root = tk.Tk()
root.title("AI Study Companion")

tk.Label(root, text="Enter a topic:").pack()
topic_entry = tk.Entry(root, width=40)
topic_entry.pack()

tk.Button(root, text="Generate Quiz", command=start_quiz).pack(pady=5)
quiz_text = tk.Text(root, height=15, width=70)
quiz_text.pack()

root.mainloop()
