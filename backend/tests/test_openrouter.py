from openai import OpenAI
from app.core.config import settings

client = OpenAI(
    base_url=settings.OPENROUTER_BASE_URL,
    api_key=settings.OPENROUTER_API_KEY,
)

response = client.chat.completions.create(
    model=settings.LLM_MODEL,
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: Hello SAKURA"
        }
    ],
   
)

print(response.choices[0].message.content)