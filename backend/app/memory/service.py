from app.memory.models import Memory
from app.memory.repository import MemoryRepository


class MemoryService:
    def __init__(self, repository: MemoryRepository):
        self.repository = repository

    def add(self, memory: Memory):
        self.repository.add(memory)

    def search(self, query: str):
        return self.repository.search(query)

    def all(self):
        return self.repository.all()