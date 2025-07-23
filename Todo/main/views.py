from django.shortcuts import render,redirect , get_object_or_404
from .models import Tododb
# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        task = request.POST.get('task')
        date = request.POST.get('date')

        Tododb.objects.create(title=title,task=task,date=date)

        return redirect('home')

    all_tasks = Tododb.objects.all()
    return render(request,'html/home.html',{'tasks':all_tasks})

def delete(request,id):
    item = get_object_or_404(Tododb,id=id)
    item.delete()
    return redirect('home')