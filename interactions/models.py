
from django.db import models
from django.conf import settings
from news.models import Article

class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE, related_name="comments")
    author=models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    body=models.TextField()
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='replies')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username} -> {self.article.title}"
    class Meta:
        ordering = ['-created_at']

class Like(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,related_name="likes")
    user=models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE )

    class Meta:
        unique_together=("article","user")

class Contact(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.name



