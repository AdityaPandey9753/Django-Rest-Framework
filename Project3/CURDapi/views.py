from functools import partial
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Students
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator


# Create your views here.
@csrf_exempt
def StudentApi(request):
  if request.method == 'GET':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id', None)
    if id is not None:
      stu = Students.objects.get(id = id)
      serializer = StudentSerializer(stu)
      print(serializer)
      json_data = JSONRenderer().render(serializer.data)
      return HttpResponse(json_data, content_type = 'application/json')
    stu = Students.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
  
  if request.method == 'POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data = python_data)
    if serializer.is_valid():
      serializer.save()
      res = {'msg':'data inserted'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
  
  if request.method == 'PUT':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    stu = Students.objects.get(id = id)
    serializer = StudentSerializer(stu, data = python_data, partial=True) #pass total data in partial data field and remove partial = true for complete data
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data updated'}
      json_data = JSONRenderer().render(res)
      return HttpResponse( json_data)
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse( json_data)
    
  if request.method == 'DELETE':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    stu = Students.objects.get(id = id)
    stu.delete()
    res = {'msg':'data deleted'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data)
    
@method_decorator(csrf_exempt, name='dispatch')
class StudentApiCLass(View):
  def get(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id', None)
    if id is not None:
      stu = Students.objects.get(id = id)
      serializer = StudentSerializer(stu)
      print(serializer)
      json_data = JSONRenderer().render(serializer.data)
      return HttpResponse(json_data, content_type = 'application/json')
    stu = Students.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')
  
  def post(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data = python_data)
    if serializer.is_valid():
      serializer.save()
      res = {'msg':'data inserted'}
      json_data = JSONRenderer().render(res)
      return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')
  
  def delete(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    stu = Students.objects.get(id = id)
    stu.delete()
    res = {'msg':'data deleted'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data)
  
  def put(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    stu = Students.objects.get(id = id)
    serializer = StudentSerializer(stu, data = python_data, partial=True) #pass total data in partial data field and remove partial = true for complete data
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data updated'}
      json_data = JSONRenderer().render(res)
      return HttpResponse( json_data)
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse( json_data)