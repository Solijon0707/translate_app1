from django.shortcuts import render, redirect
from .models import *
from translate import Translator
# Create your views here.
def index(request):
	if request.method=='POST':
		student=Student(name=request.POST['task'])
		student.save()
		return redirect('/app')
	student=Student.objects.all()
	return render(request, 'index.html', {'student':student})




def delete(request , id):
	Student.objects.get(id=id).delete()
	return redirect('/app')


def edit(request , id):
	student1=Student.objects.get(id=id)
	if request.method=='POST':
		student1.name = request.POST['task']
		student1.save()
		return redirect('/app')
	student=Student.objects.all()
	return render (request , 'Mysite.html',{'student':student,'student1':student1}) 






def translation(request):
	if request.method=='POST':
		student=request.POST['tran']
		translator= Translator(to_lang="uz")
		translation = translator.translate(student)
		
		return render(request, 'translate.html',{'translation':translation, 'text': student})
	return render(request , 'translate.html')
