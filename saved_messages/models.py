from django.db import models
from django.contrib.auth.hashers import make_password


class Message(models.Model):
  text = models.TextField()
  password = models.CharField(max_length=80, null=True)

  def save(self, *args, **kwargs):
    if self.password:
      self.password = make_password(self.password, 'unsalted_sha1')
    super().save(*args, **kwargs)
  
  class Meta:
    ordering = ['-pk']