from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    def setUp(self) -> None:
        blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}

    def test_menu_prints_prompt(self):
        with patch("builtins.input", return_value="q") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value="q"):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("c", "Test", "Author", "q")
            app.menu()

            self.assertIsNotNone(app.blogs["Test"])

    def test_menu_calls_print_blogs(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("l", "q")
            with patch("builtins.print") as mocked_print:
                app.menu()

                mocked_print.assert_called_with("-<Blog(title: Test, author: Test Author)>")

    def test_menu_calls_selection(self):
        test_blog = app.blogs["Test"]
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("r", "Test", "q")
            with patch("app.print_posts") as mocked_print_posts:
                app.menu()

                mocked_print_posts.assert_called_with(test_blog)

    def test_menu_calls_create_post(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("p", "Test", "Test Post Title", "Test Post Content", "q")
            app.menu()

            post = app.blogs["Test"].posts[0]
            self.assertIsNotNone(post)
            self.assertEqual("Test Post Title", post.title)
            self.assertEqual("Test Post Content", post.content)

    def test_print_blogs(self):
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("-<Blog(title: Test, author: Test Author)>")

    def test_ask_create_blogs(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test Blog Title", "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test Blog Title"))

    def test_ask_read_blog(self):
        test_blog = app.blogs["Test"]
        with patch("builtins.input", return_value="Test"):
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(test_blog)

    def test_print_posts(self):
        test_blog = app.blogs["Test"]
        post = test_blog.create_post("Test Post", "Test Content")
        test_blog.posts.append(post)
        with patch("app.print_posts") as mocked_print_posts:
            app.print_posts(test_blog)

            mocked_print_posts.assert_called_with(test_blog)

    def test_print_post(self):
        test_blog = app.blogs["Test"]
        post = test_blog.create_post("Test Post", "Test Content")
        test_blog.posts.append(post)

        with patch("app.print_post") as mocked_print_post:
            app.print_post(post)

            mocked_print_post.assert_called_with(post)

    def test_ask_create_post(self):

        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Title", "Test Content")
            app.ask_create_post()

            post = app.blogs["Test"].posts[0]
            self.assertIsNotNone(post)
            self.assertEqual("Test Title", post.title)
            self.assertEqual("Test Content", post.content)
