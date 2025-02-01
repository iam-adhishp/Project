from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm
from support.models import BestSeller

def cs(request):
    tickets = Ticket.objects.all()
    return render(request, 'support/home.html', {'tickets': tickets})


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request, 'support/create_ticket.html', {'form': form})


def sampl(request):
    return render(request, 'try/try.html',)


def bestsellers_list(request):
    bestsellers = BestSeller.objects.all()
    return render(request, 'bestsellers/bestsellers_list.html', {'bestsellers': bestsellers})


MAX_SEED = 10000


def index(request):
    return render(request, 'try/index.html')


