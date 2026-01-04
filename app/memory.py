class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def get(self):
        return self.history

    def clear(self):
        self.history = []
