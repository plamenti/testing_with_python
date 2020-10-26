from typing import Dict


class Post:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def json(self) -> Dict[str, str]:
        return {
            "title": self.title,
            "content": self.content
        }

    def __repr__(self):
        return f"<Post(title: {self.title}, content: {self.content})>"
