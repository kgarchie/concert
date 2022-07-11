import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Concert, Bookings
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    concerts = Concert.objects.all().distinct()
    context = {
        'concerts': concerts,
    }
    return render(request, 'index.html', context)


def details(request, date):
    concerts = Concert.objects.filter(concert_Date__date=date)
    context = {
        'concerts': concerts,
    }
    return render(request, 'details.html', context)


def book(request, date, id):
    concerts = Concert.objects.filter(concert_Date__date=date)
    concert = concerts.get(id=id)
    context = {
        'concert': concert
    }

    return render(request, 'book.html', context)


def book_request(request, date, id):
    concerts = Concert.objects.filter(concert_Date__date=date)
    concert = concerts.get(id=id)
    user = request.user
    Bookings.objects.create(user=user, concert=concert)

    bookings = Bookings.objects.filter(user=user)
    context = {
        'bookings': bookings
    }

    return render(request, 'bookings.html', context)


def search(request):
    if request.method == 'POST':
        query = request.POST['q']

        composition_filter = Concert.objects.filter(compositions__composition_Name__icontains=query)
        composer_filter = Concert.objects.filter(compositions__composer_Name__icontains=query)
        movement_filter = Concert.objects.filter(compositions__movement_ID__movement_Name__icontains=query)
        try:
            q_date = datetime.datetime.strptime(query, '%Y-%m-%d')
            date_filter = Concert.objects.filter(concert_Date__date=q_date)
        except Exception:
            date_filter = None

        results = composer_filter | composition_filter | movement_filter

        if date_filter is not None:
            results = results | date_filter

        context = {
            'concerts': results
        }

        return render(request, 'search.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('app:home')
        else:
            context = {
                'errors': "User does not exist",
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('app:login')


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = form.save(commit=False)
            if user is not None:
                User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('app:home')
    return render(request, 'registration/register.html', {'form': form})


def about(request):
    return render(request, 'about.html')
