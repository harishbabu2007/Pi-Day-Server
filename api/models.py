from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Blogs(models.Model):
  student_name = models.CharField(max_length=100, default="undefined")
  roll_no = models.IntegerField(default=-1)
  flaged = models.BooleanField(default=False)
  flagged_comment = models.CharField(max_length=300, default="Nil")
  title = models.CharField(max_length=255, default="")
  body = RichTextField(blank=True, null=True, default="")
  innerHtml = models.TextField(default="")

  def __str__(self):
    return self.student_name +  "" + str(self.roll_no)