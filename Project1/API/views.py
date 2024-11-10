from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.
# Model object - single student data
def Student_detail(request, pk):
  stu = Student.objects.get(id=pk)
  # print(stu)
  serializer = StudentSerializer(stu)
  # print(serializer)
  # print(serializer.data)
  json_data = JSONRenderer().render(serializer.data) # converting data into json
  # print(json_data)
  return HttpResponse(json_data, content_type='application/json') # giving http response

# Query set - all student data
def Student_list(request):
  stu = Student.objects.all() #creating query set
  # print(stu)
  serializer = StudentSerializer(stu, many=True) #use many = true for multiple data that is not in dict form, default false
  # print(serializer)
  # print(serializer.data)
  # json_data = JSONRenderer().render(serializer.data)
  # print(json_data)
  # return HttpResponse(json_data, content_type='application/json')
  return JsonResponse(serializer.data, safe=False)

""" For this example only normal django views are used and drf views
first we create the instance of model stu
converting model instance stu into Python dict / Serializing object
then we render the data in JSON
"""