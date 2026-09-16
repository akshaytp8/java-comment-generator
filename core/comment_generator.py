import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_comments(code: str) -> str:
    """
    Uses Groq's latest Llama 3.3 model to generate descriptive comments
    for Java code. Returns fully commented code.
    """
    if not GROQ_API_KEY:
        return "ERROR: GROQ_API_KEY not found. Add it to your .env file."

    prompt = f"""
You are a Java code documentation assistant.
ONLY add meaningful comments to the Java code PROVIDED.
Do NOT convert or rewrite code into another language.
Do NOT change any logic.

Return ONLY the commented Java code.

Java code:
{code}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
