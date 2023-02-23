from django.shortcuts import render
from studyonlineapp.models import Student

# Create your views here.
def homepage(request):
	return render(request=request,template_name='studyonlineapp/homepage.html')

def display(request):
	student_data=Student.objects.all()
	print(student_data)
	print(type(student_data))
	dict_data={'student_data' : student_data}
	return render(request=request,template_name='studyonlineapp/display.html', context=dict_data)
