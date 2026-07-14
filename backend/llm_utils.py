import os, json, re
from dotenv import load_dotenv
import openai
from app.prompts import SYSTEM_PROMPT

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai_chat(system, user_prompt, max_tokens=800):
    res = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":system},
            {"role":"user","content":user_prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.2
    )
    return res['choices'][0]['message']['content']
