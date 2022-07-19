from .views import *
from django.urls import path

urlpatterns = [
  path("api/blogs/all", all_blogs, name="all-blogs"),
  path("api/blogs/add", add_blog, name="add_blog")
]