from app.conversation.service import ConversationService

service = ConversationService()

conversation = service.create()

conversation.add_user_message("Hello")

conversation.add_assistant_message("Hi! I'm SAKURA.")

print(conversation)