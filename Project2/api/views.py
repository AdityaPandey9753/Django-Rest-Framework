import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_Create(request):
  if request.method == 'POST':
    json_data = request.body  # Get the raw binary data from the request body
    
    stream = io.BytesIO(json_data)  # Convert binary data into an in-memory binary stream
    
    python_data = JSONParser().parse(stream)  # Deserialize (parse) the binary stream into a Python dictionary
    
    serializer = StudentSerializer(data=python_data)  # Pass the parsed data to the serializer
    
    if serializer.is_valid():  # Check if the data is valid (ensures data types, required fields, etc.)
      
      serializer.save()  # Save the data to the database using the create() method in the serializer
      
      res = {'msg': 'Data Created'}  # Success message
      
      json_data = JSONRenderer().render(res)  # Convert the Python dict into binary JSON
      
      return HttpResponse(json_data, content_type='application/json')  # Send HTTP response
    
    json_data = JSONRenderer().render(serializer.errors)  # Convert validation errors into binary JSON
    
    return HttpResponse(json_data, content_type='application/json')  # Send the errors as a response
