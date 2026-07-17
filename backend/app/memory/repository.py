from app.memory.models import Memory


class MemoryRepository:
    def __init__(self):
        self._memories: list[Memory] = []

    def add(self, memory: Memory):
        self._memories.append(memory)

    def all(self) -> list[Memory]:
        return self._memories

    def search(self, query: str) -> list[Memory]:
        query = query.lower()

        return [
            memory
            for memory in self._memories
            if query in memory.content.lower()
        ]