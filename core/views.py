from django.shortcuts import render

from .forms import ContactForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm()  # instancia do nosso formulário
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')
