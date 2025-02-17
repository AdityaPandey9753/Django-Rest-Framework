# GenericAPIView Model Mixin
from .models import Student
from .serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class LCstudent(GenericAPIView, ListModelMixin, CreateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  
class RUDstudent(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

""" # GenericAPIView list model mixin
class StudentList(GenericAPIView, ListModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

# GenericAPIView Create Model Mixin
class StudentCreate(GenericAPIView, CreateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

# GenericAPIView Retrive Model Mixin
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)
  
# GenericAPIView Update Model Mixin
class StudentUpdate(GenericAPIView, UpdateModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

# GenericAPIView Destroy Model Mixin
class StudentDestroy(GenericAPIView, DestroyModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs) """