from django.shortcuts import get_object_or_404, render, redirect

from users.models import Note
from .forms import LoginForm, NoteModelForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    return render(request, 'index.html')

def note_list(request):
    context = dict()
    context['notes'] = Note.objects.all().order_by('-pk')
    return render(request, 'notes.html', context)

def note_create(request):
    context = dict()
    context['items'] = Note.objects.all().order_by('-pk')
    context['form'] = NoteModelForm()
    if request.method == 'POST':
        form = NoteModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request, 'Birseyler eklendi')
    return render(request, 'form.html', context)

def note_update(request, pk):
    context = dict()
    item = Note.objects.get(pk=pk)
    context['form'] = NoteModelForm(instance=item)

    if request.method == 'POST':
        form = NoteModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            messages.success(request,'güncellendi')
            return redirect('page_update', pk)
    return render(request, 'form.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                        password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'Disabled Account')

            else:
                messages.info(request, 'Check Your Username and Password')

    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form':form})


def user_register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created, You can LOGIN')
            return redirect('login')
    
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('index')

