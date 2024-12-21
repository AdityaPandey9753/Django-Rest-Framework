from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from .serializers import StudentSerializer
from .models import Student
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentValidatorApi(View):
  def get(self,request, *args, **kwargs):
    try:
      json_data = request.body
      stream = io.BytesIO(json_data)
      python_data = JSONParser().parse(stream)
      id = python_data.get('id',None)
      if id is not None:
        try:
          stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
          return JsonResponse({'error': f'Student with ID {id} does not exist.'}, status=404)
        # print(stu)
        serializer = StudentSerializer(stu)
        # print(serializer)
        # print(serializer.data)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)
      stu = Student.objects.all()
      serializer = StudentSerializer(stu, many=True)
      return JsonResponse(serializer.data, safe=False)
    except ValidationError as e:
      return JsonResponse({'error': 'Invalid data.', 'details': e.detail}, status=400)
    except Exception as e:
      return JsonResponse({'error': 'An unexpected error occurred.', 'details': str(e)}, status=500)
    
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
    stu = Student.objects.get(id = id)
    stu.delete()
    res = {'msg':'data deleted'}
    json_data = JSONRenderer().render(res)
    return HttpResponse(json_data)
  
  def put(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    stu = Student.objects.get(id = id)
    serializer = StudentSerializer(stu, data = python_data, partial=True) #pass total data in partial data field and remove partial = true for complete data
    if serializer.is_valid():
      serializer.save()
      res = {'msg': 'Data updated'}
      json_data = JSONRenderer().render(res)
      return HttpResponse( json_data)
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse( json_data)