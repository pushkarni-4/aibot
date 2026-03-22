import os
import json
from dotenv import load_dotenv
from groq import Groq

# 1. Load your secret key from the .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# 2. Load your 'Hindsight' memory from the json file
with open('memory.json', 'r') as file:
    data = json.load(file)
    past_lessons = ", ".join(data['lessons_learned'])

# 3. Setup the AI Mentor
client = Groq(api_key=api_key)

# This tells the AI who it is and what you've learned before
system_info = f"You are a Senior Coding Mentor. Your student is {data['student_name']}. They have already learned: {past_lessons}."

def talk_to_mentor(question):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_info},
                {"role": "user", "content": question}
            ]
        )
        print("\n--- MENTOR'S ADVICE ---")
        print(completion.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

# 4. Let's ask the mentor a test question!
talk_to_mentor("What model should I use for my Groq project?")
import json

def get_stats():
    with open('memory.json', 'r') as f:
        data = json.load(f)
        total_lessons = len(data.get("lessons_learned", []))
        name = data.get("student_name", "User")
        return total_lessons, name

def get_recent_lessons():
    with open('memory.json', 'r') as f:
        data = json.load(f)
        return data.get("lessons_learned", [])[-3:] # Returns last 3 lessons
