from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from client.forms import ClientForm
from client.models import Client


@login_required
def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            return redirect('client:list_client')
    else:
        form = ClientForm()
    return render(request, 'client/create_client.html', {'form': form})


@login_required
def list_client(request):
    client_list = Client.objects.filter(user=request.user).order_by('first_name')
    paginator = Paginator(client_list, 6)

    page_number = request.GET.get('page')
    clients = paginator.get_page(page_number)
    return render(request, 'client/list_client.html', {'clients': clients})
