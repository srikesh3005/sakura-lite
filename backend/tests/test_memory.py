import asyncio

from app.chat.service import ChatService


async def main():
    service = ChatService()

    print("========== FIRST MESSAGE ==========")

    result = await service.chat(
        conversation_id=None,
        message="Hello!"
    )

    print(result)

    conversation_id = result["conversation_id"]

    print("\n========== SECOND MESSAGE ==========")

    result = await service.chat(
        conversation_id=conversation_id,
        message="What's my previous message?"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())