from dataclasses import dataclass, field
import uuid

@dataclass
class Task:
    description: str
    completed: bool = field(default=False)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))  

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        return f"Task ID: {self.id}, Description: {self.description}, Status: {'Completed' if self.completed else 'Pending'}"
