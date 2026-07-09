from django.test import TestCase
from .models import Profile
from django.contrib.auth import get_user_model

User=get_user_model()

class ProfileTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            username="Davron",
            password="Testpassword123"
        )

        self.profile=Profile.objects.create(
            user=self.user,
            avatar="media/avatars/7dbed90655c6d7de0f4d01eb01b9cbe1.jpg",
            bio="salom dasturchilar")

    def test_profile(self):
        self.assertEqual(self.profile.user.username,"Davron")
        self.assertNotEqual(self.profile.user.password,"Testpassword123")
        self.assertEqual(self.profile.avatar,"media/avatars/7dbed90655c6d7de0f4d01eb01b9cbe1.jpg")
        self.assertEqual(self.profile.bio,"salom dasturchilar")
