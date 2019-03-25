from django.shortcuts import render, redirect
from .models import cliente
from .forms import clienteForm


def list_cliente(request):
    clientes = cliente.objects.all()
    return render(request, 'cliente.html', {'clientes': clientes})


def create_cliente(request):
    form = clienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_cliente')

    return render(request, 'clientes-form.html', {'form': form})


def update_cliente(request, id):
    Cliente = cliente.objects.get(idcliente=id)
    form = clienteForm(request.POST or None, instance=Cliente)

    if form.is_valid():
        form.save()
        return redirect('list_cliente')

    return render(request, 'clientes-form.html', {'form': form, 'cliente': Cliente})


def delete_cliente(request, id):
    Cliente = cliente.objects.get(idcliente=id)

    if request.method == 'POST':
        cliente.delete(Cliente)
        return redirect('list_cliente')

    return render(request, 'cliente-delete-confirm.html', {'cliente': Cliente})
