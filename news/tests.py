from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Category,Tag,Article,Subscribe

User=get_user_model()
class CategoryModelTest(TestCase):
    def setUp(self):
        self.category=Category.objects.create(name="Sport")

    def test_categorya_yaratish(self):
        self.assertEqual(self.category.name,"Sport")
        self.assertNotEqual(self.category.name,"Mahalliy")


class TagTest(TestCase):
    def setUp(self):
        self.tag=Tag.objects.create(name="Salom")

    def test_tag_yaratish(self):
        self.assertEqual(self.tag.name,"Salom")
        self.assertNotEqual(self.tag.name,"Ali")

class ArticleTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            username="Davron",
            password="testpassword123"
        )
        self.article=Article.objects.create(
            title="Salom alaykum",
            slug="salom-alaykum",
            body="Barchaga salom ahli guruppa",
            author=self.user,
        )
    def test_article_yaratish(self):
        self.assertEqual(self.article.title, "Salom alaykum")
        self.assertEqual(self.article.slug, "salom-alaykum")
        self.assertEqual(self.article.body, "Barchaga salom ahli guruppa")
        self.assertEqual(self.article.author.username, "Davron")



class SubscribeTest(TestCase):
    def setUp(self):
        self.email=Subscribe.objects.create(
            email="azim@gmail.com"
        )
    def test_subscribe_yaratish(self):
        self.assertEqual(self.email.email,"azim@gmail.com")
