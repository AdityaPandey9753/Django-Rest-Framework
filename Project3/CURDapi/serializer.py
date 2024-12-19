from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  age = serializers.IntegerField()
  city = serializers.CharField(max_length=100)
  
  def create(self, validated_data):
    return Students.objects.create(**validated_data)
  
  """ def update(self, instance, validated_data):
    return super().update(instance, validated_data) """
    
  """ Partial Update """
  def update(self, instance, validated_data):
    print(instance.name)
    instance.name = validated_data.get('name', instance.name)
    print(instance.name)
    instance.age = validated_data.get('age', instance.age)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance