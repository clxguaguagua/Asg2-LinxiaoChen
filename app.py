"""
app.py - Customer Support Response Generator
Uses Google Gemini API to draft professional support replies.
"""

import os
import json
import datetime
import time
from google import genai

API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
MODEL_NAME = "gemini-3-flash-preview"

SYSTEM_INSTRUCTION = """You are a professional customer support representative for an e-commerce company.
Your job is to write clear, empathetic, and helpful replies to customer inquiries or complaints.

Guidelines:
- Always greet the customer by acknowledging their issue
- Apologize when appropriate, without admitting legal liability
- Provide a concrete next step or solution
- Keep the tone warm, professional, and concise (under 150 words)
- End with an offer to help further
- Do NOT make up specific policies, dates, or tracking numbers
- If information is missing, ask one clarifying question
"""

def generate_reply(customer_message: str) -> str:
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=customer_message,
        config=genai.types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            max_output_tokens=300,
        )
    )
    return response.text.strip()

def run_eval_set(eval_path: str = "eval_set.json"):
    with open(eval_path, "r", encoding="utf-8") as f:
        eval_cases = json.load(f)

    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"outputs/results_{timestamp}.txt"

    print(f"Running {len(eval_cases)} eval cases with model: {MODEL_NAME}\n")
    print("=" * 70)

    with open(output_file, "w", encoding="utf-8") as out:
        out.write(f"Model: {MODEL_NAME}\nTimestamp: {timestamp}\n\n")

        for i, case in enumerate(eval_cases, 1):
            print(f"[Case {i}] {case['id']} — {case['type']}")
            print(f"Customer: {case['input']}\n")

            reply = generate_reply(case["input"])

            print(f"Reply:\n{reply}")
            print("-" * 70)

            out.write(f"{'='*70}\n")
            out.write(f"Case {i}: {case['id']} ({case['type']})\n")
            out.write(f"Customer Input:\n{case['input']}\n\n")
            out.write(f"Expected behavior:\n{case['expected_behavior']}\n\n")
            out.write(f"Generated Reply:\n{reply}\n\n")

            time.sleep(3)

    print(f"\n✅ Results saved to: {output_file}")

if __name__ == "__main__":
    run_eval_set("eval_set.json")