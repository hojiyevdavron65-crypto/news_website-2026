from django.test import TestCase
from .models import Comment,Contact,Like
from django.contrib.auth import get_user_model
from news.models import Article

User=get_user_model()


class TestComment(TestCase):
    def setUp(self):
        self.contact=Contact.objects.create(
            name="Ali",
            email="ali@gmail.com",
            subject="Xabar",
            message="Salom barchaga"
        )
    def test_contact_yaratish(self):
        self.assertEqual(self.contact.name,"Ali")
        self.assertNotEqual(self.contact.name,"Vali")
        self.assertEqual(self.contact.email,"ali@gmail.com")
        self.assertEqual(self.contact.subject,"Xabar")
        self.assertEqual(self.contact.message,"Salom barchaga")

class TestComment(TestCase):
    def setUp(self):
        self.author=User.objects.create_user(
            username="Ali",
            password="Testpassword123"
        )
        self.article=Article.objects.create(
            title="Salom alaykum",
            slug="salom-alaykum",
            body="Barchaga salom ahli guruppa",
            author=self.author,
        )
        self.comment=Comment.objects.create(
            article=self.article,
            author=self.author,
            body="saloom dasturchilar"
        )
    def test_comment_yaratish(self):
        self.assertEqual(self.article.title,"Salom alaykum")
        self.assertEqual(self.author.username,"Ali")
        self.assertEqual(self.comment.body,"saloom dasturchilar")


class LikeTest(TestCase):
    def setUp(self):
        self.author=User.objects,create_user(
            username="Ali",
            password="Testpassword123"
        )
        self.article=Article.objects.create(
            title="Salom alaykum",
            slug="salom-alaykum",
            body="Barchaga salom ahli guruppa",
            author=self.author,
        )
    def like_test_yarat(self):
        self.assertEqual(self.article.slug,"salom-alaykum")
        self.assertEqual(self.author.username,"Ali")