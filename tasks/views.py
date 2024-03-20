from django.shortcuts import render,redirect
from .models import task
from .forms import*

# Create your views here.
def index(request):
    tasks=task.objects.all()
    form=Taskform()
    if request.method=='POST':
        form=Taskform(request.POST)   
        if form.is_valid():
            form.save()
        return redirect('/')    

    contex={"tasks":tasks,'form':form}  
    return render (request,'index.html',contex)



# def  updatee(request,pk):
#     taske=task.objects.get(id=pk)
#     form=Taskform(instance=taske)
#     if request.method=="POST":
#         form=Taskform(request.POST,instance=taske)
#         if form.is_valid():
#             form.save()
#             return redirect('/')


    
#     contex={'form':form}
#     return render(request,'uptask.html',contex)
def updatee(request, pk):
	taske = task.objects.get(id=pk)

	form = Taskform(instance=taske)

	if request.method == 'POST':
		form = Taskform(request.POST, instance=taske)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'uptask.html', context)


def deletetask(request, pk):
    item = task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect("/")
    context = {'item': item}
    return render(request, 'delete.html', context)