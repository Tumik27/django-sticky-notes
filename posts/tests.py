from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Post, Author


class PostModelTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name='Test Author')
        Post.objects.create(title='Test Post', content='This is a test post.', author=author)

    def test_post_has_title(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')


class PostViewTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name='Test Author')
        Post.objects.create(title='Test Post', content='This is a test post.', author=author)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')