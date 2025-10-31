# AI Study Buddy

A Python desktop app that generates topic-based multiple choice quizzes using ChatGPT’s API.

## Features
- Enter any topic and number of questions
- Auto-generates MCQs with answers
- Stores quiz results locally in `SQLite`
- Secure API key handling via `.env`

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-study-companion
   cd ai-study-companion
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project folder and add your OpenAI API key

5. **Run the app**
   ```bash
   python main.py
   ```
