from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY"),
    timeout=30.0,
)

response = client.chat.completions.create(
    model="meta/llama-3.3-70b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly the word: hello"
        }
    ],
    max_tokens=10,
    stream=False,
)

print(response.choices[0].message.content)