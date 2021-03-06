from django.db import models
from django.conf import settings
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib import auth


# Create your models here.
class Post(models.Model):
  # id = models.AutoField(primary_key=True)
  # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()
  
  def approved_comments(self):
    return self.comments.filter(approved_comment=True)

  def __str__(self):
    return self.title

  # def get_absolute_url(self):
  #   from django.urls import reverse
  #   return reverse('post/<int:pk>', args=[str(self.id)])

  # class Meta:
  #   ordering = ['-published_date']


class Comment(models.Model):
  id = models.AutoField(primary_key=True)
  post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
  author = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  approved_comment = models.BooleanField(default=False)

  def approve(self):
    self.approved_comment = True
    self.save()

  def __str__(self):
    return self.text
