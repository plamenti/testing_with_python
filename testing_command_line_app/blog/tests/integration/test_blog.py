import json
from unittest import TestCase

from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_blog_with_posts(self):
        post1 = Post("post1 title", "post1 content")
        post2 = Post("post2 title", "post2 content")
        posts = [post1, post2]
        b = Blog("Test", "Author", posts)

        self.assertEqual("Test", b.title, "Blog title is not correct")
        self.assertEqual("Author", b.author, "Blog author is not correct")
        self.assertListEqual(posts, b.posts, "Blog posts are not correct")

    def test_create_post(self):
        p = Blog.create_post("Test", "Test Content")

        self.assertEqual("Test", p.title, "Post title is incorrect!")
        self.assertEqual("Test Content", p.content, "Post content is not correct")

    def test_json(self):
        post1 = Post("post1 title", "post1 content")
        post2 = Post("post2 title", "post2 content")
        posts = [post1, post2]
        expected_json = {
            "title": "Test",
            "author": "Author",
            "posts": [Post("post1 title", "post1 content"),
                      Post("post2 title", "post2 content")]
        }

        b = Blog("Test", "Author", posts)

        print(b.json().__repr__())
        print(expected_json.__repr__())

        self.assertEqual(expected_json.__repr__(), b.json().__repr__(), "Blog json is incorrect!")
