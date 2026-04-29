from openai import OpenAI
import os
from dotenv import load_dotenv

# GOAL: Run this file to have a simple chat with the assistant USING FREE API KEY.
#       Type "exit" or "quit" to end the conversation.

# CREATE .env file with OPENAI_API_KEY=<your_api_key_here>
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# Start with a system + assistant greeting
messages = [
    {"role": "system", "content": "You are a friendly and helpful assistant."},
    {"role": "assistant", "content": "Hey! 👋 I'm your AI assistant. How can I help you today?"}
]

# Print initial greeting
print("AI:", messages[-1]["content"])

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("AI: Goodbye! 👋")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
    )

    reply = response.choices[0].message.content
    print("AI:", reply)

    messages.append({"role": "assistant", "content": reply})