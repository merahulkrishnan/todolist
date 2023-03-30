from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# from django.urls import reverse_lazy

from datetime import datetime

from .forms import TodoForm
from .models import Task
# from django.views.generic import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import UpdateView, DeleteView


# class Tasklistview(ListView):
#     model = Task
#     template_name = 'home.html'
#     context_object_name = 'task'
#
#
# class Taskdetailview(DetailView):
#     model = Task
#     template_name = 'detail.html'
#     context_object_name = 'task'
#
#
# class Taskupdateview(UpdateView):
#     model = Task
#     template_name = 'update.html'
#     context_object_name = 'task'
#     fields = ('name', 'priority', 'date')
#
#     def get_success_url(self):
#         return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})
#
#
# class Taskdeleteview(DeleteView):
#     model = Task
#     template_name = 'delete.html'
#     success_url = reverse_lazy('cbvhome')


# Create your views here.

def newhome(request):
    return render(request, "newhome.html")


def demo(request):
    # Filter out old tasks and user-specific tasks
    task1 = Task.objects.filter(date__gte=datetime.now().date(), user=request.user)

    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')

        # Check if any fields are empty
        if not (name and priority and date):
            messages.info(request, 'Please fill all the fields')
            return render(request, "home.html", {'task1': task1})

        task = Task(name=name, priority=priority, date=date, user=request.user)
        task.save()

    return render(request, "home.html", {'task1': task1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('demo')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('demo')
    return render(request, 'edit.html', {'f': f, 'task': task})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        cpassword = request.POST.get('password1', '').strip()
        if not username or not password or not cpassword:
            messages.info(request, 'Please fill all the fields')
            return redirect('/register')
        elif password != cpassword:
            messages.info(request, 'Password does not match')
            return redirect('/register')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already used')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/login')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('demo')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
