# AI Study Buddy

A Python desktop app that generates topic-based multiple choice quizzes using ChatGPT’s API

## Features
- Enter any topic and number of questions
- Auto-generates MCQs with answers
- Stores quiz results locally in `SQLite`
- Secure API key handling via `.env`

## Setup
#1 Clone the repository
git clone https://github.com/yourusername/ai-study-companion
cd ai-study-companion

#2 Create a virtual environment (optional but recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

#3 Install dependencies
pip install -r requirements.txt

#4 Create a .env file in the project folder
# (Do NOT upload this file to GitHub)
echo OPENAI_API_KEY=sk-your-real-key-here > .env

#5 Run the app
python main.py
