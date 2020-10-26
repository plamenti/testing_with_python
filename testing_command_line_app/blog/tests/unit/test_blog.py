import json
from unittest import TestCase

from blog import Blog
from post import Post


class BlogTest(TestCase):

    def test_create_blog_without_posts(self):
        b = Blog("Test", "Author")

        self.assertEqual("Test", b.title, "Blog title is not correct")
        self.assertEqual("Author", b.author, "Blog author is not correct")
        self.assertListEqual([], b.posts, "Blog posts are not correct")

    def test_repr(self):
        b = Blog("Test", "Author")
        expected_repr = "<Blog(title: Test, author: Author)>"

        self.assertEqual(expected_repr, b.__repr__())
