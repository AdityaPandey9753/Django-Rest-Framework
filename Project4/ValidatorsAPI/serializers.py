from wsgiref.validate import validator
from rest_framework import serializers
from .models import Student

# function based validator
def start_with_r(value):
  if value[0].lower() == 'k':
    raise serializers.ValidationError('Name should not start with k') 

#class based validator
class no_even_number:
  def __call__(self,value):
    if value % 2 == 0:
      raise serializers.ValidationError('No even number roll no. allowed')

class StudentSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100, validators=[start_with_r])
  roll = serializers.IntegerField(validators=[no_even_number()])
  city = serializers.CharField(max_length=100)
  
  def create(self, validated_data):
    return Student.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    # print(instance.name)
    instance.name = validated_data.get('name', instance.name)
    # print(instance.name)
    instance.age = validated_data.get('age', instance.age)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance
  
  # field level validation
  def validate_roll(self, value):
    if value >= 200:
      raise serializers.ValidationError('Seat Full')
    return value
  
  # object level validation
  def validate(self, attrs):
    nm = attrs.get('name')
    ct = attrs.get('city')
    if nm.lower() == 'rohit' and ct.lower != 'thane':
      raise serializers.ValidationError('City for rohit should be thane')
    return attrs