'''Week 0

This files includes week 0 exercises from Lonely Octopus Bootcamp

In this project, you will learn how to get started

'''
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Specify the model you want to use
model = "gpt-4o"  # You can change this to gpt-3.5-turbo or others

# Your input text
dish_name = "Chakalaka"

# Format the chat messages
messages = [
    {"role": "system", "content": "You are a World Class Chef"},
    {"role": "user", "content": f"Show me the ingredients, recipe and preparation method of this dish:{dish_name}. Organize your answer in clear and concise bullet points."}
]

# Send the request
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0
)

# Display the response
response_message = response.choices[0].message.content
print(response_message)