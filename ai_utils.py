import os
from dotenv import load_dotenv
from groq import Groq

# Load the .env file
load_dotenv()

# Fetch the key from env
api_key = os.getenv("GROQ_API_KEY")

# Optional: Debug print (remove later)
print("Loaded Groq API Key:", api_key[:10], "..." if api_key else "❌ KEY NOT FOUND")

# Initialize Groq client
client = Groq(api_key=api_key)

def generate_email_with_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # You can also use "mixtral-8x7b-32768" or other available models
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes professional and well-structured emails based on user prompts."},
                {"role": "user", "content": f"Write an email based on this prompt: {prompt}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating email with Groq: {e}")
        return f"Error generating email: {str(e)}"