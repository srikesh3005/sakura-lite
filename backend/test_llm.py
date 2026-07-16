import asyncio

from app.llm.service import LLMService


async def main():
    llm = LLMService()

    response = await llm.chat(
        [
            {"role": "user", "content": "Hello"}
        ]
    )

    print(response)


asyncio.run(main())