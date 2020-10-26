from typing import List, Optional, Dict

from post import Post


class Blog:
    def __init__(self, title: str, author: str, posts: Optional[List[Post]] = None):
        self.title = title
        self.author = author
        self.posts = [] if posts is None else posts[:]

    @staticmethod
    def create_post(title: str, content: str) -> Post:
        p = Post(title, content)

        return p

    def json(self) -> Dict[str, Dict]:
        return {
            "title": self.title,
            "author": self.author,
            "posts": self.posts
        }

    def __repr__(self):
        return f"<Blog(title: {self.title}, author: {self.author})>"
