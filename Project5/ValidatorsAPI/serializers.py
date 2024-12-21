from dataclasses import fields
from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

  # function based validator
def start_with_k(value):
  if value[0].lower() == 'k':
    raise serializers.ValidationError('Name should not start with k') 

  #class based validator
class no_even_number:
  def __call__(self,value):
    if value % 2 == 0:
      raise serializers.ValidationError('No even number roll no. allowed')

class StudentSerializer(serializers.ModelSerializer):
  
  name = serializers.CharField(validators=[start_with_k])
  roll = serializers.IntegerField(validators = [no_even_number()])
  
  class Meta:
    model = Student
    fields = ['name','roll','city']
  
  # field level validation
  """ def validate_roll(self, value):
    if value >= 200:
      raise serializers.ValidationError('Seat Full')
    return value """
  
  # object level validation
  def validate(self, attrs):
    nm = attrs.get('name')
    ct = attrs.get('city')
    if nm.lower() == 'rohit' and ct.lower() != 'thane':
      raise serializers.ValidationError('City for rohit should be thane')
    return attrs