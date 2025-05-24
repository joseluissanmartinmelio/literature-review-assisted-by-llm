from openai import OpenAI

client = OpenAI()

def ai_assistant(prompt: str, model: str = "gpt-4o-mini") -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.45
    )
    return response.choices[0].message.content.strip()