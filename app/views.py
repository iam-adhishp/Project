from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Item
from .forms import ProductForm
from .forms import SignupForm

def sample(request):
    return render(request, 'sample.html',)

@login_required
def home(request):
    query = request.GET.get('q', '')
    return render(request, 'index.html', {'query':query})
    
@login_required
def fashion(request):
    return render(request, 'fashion.html',)

@login_required
def wish(request):
    items = Product.objects.all()
    return render(request, 'add/wish.html', {'items':items})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def add_item(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_items')  
    else:
        form = ProductForm()
    return render(request, 'add/add_item.html', {'form': form})

@login_required
def view_items(request):
    items = Product.objects.all()
    return render(request, 'add/wish.html', {'items':items})

@login_required
def search_view(request):
    query = request.GET.get('q', '')  
    results = Item.objects.filter(name__icontains=query) if query else []
    return render(request, 'search.html', {'query': query, 'results': results})

@login_required
def map_view(request):
    return render(request, 'map_app/map.html')


