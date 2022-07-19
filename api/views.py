from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


@api_view(['GET'])
def all_blogs(request):
  data = Blogs.objects.all()
  processed_data = BlogSerializer(data, many=True)

  return Response(processed_data.data)

@api_view(["POST"])
def add_blog(request):
  name = request.data.get("name")
  roll_no = request.data.get("rollno")
  blog_title = request.data.get("title")
  blog_body = request.data.get("blog_body")

  name = str(name)
  name = name.lower()

  # print(name)
  # print(blog_body)
  # print(blog_title)
  # print(roll_no)
  # print(request.data)

  check = Blogs.objects.filter(student_name=name)
  # print(check)

  if len(check) == 1:
    return Response({
      "message": "fail",
      "msg": "Seems like there is already a blog with the same name... please consult the developer(harish) if this problem persists"
    })


  data = Blogs(
    student_name = name,
    roll_no = roll_no,
    title = blog_title,
    body = blog_body,
    innerHtml = blog_body,
  )

  data.save()

  return Response({
    "message": "sucess"
  })
