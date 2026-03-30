from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm, ProductModelForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    # instancia do nosso formulário, pode conter dados ou não
    form = ContactForm(request.POST or None)

    if str(request.method) == 'POST':
        # se formulário for POST validar se ele é valido
        # is_valid() é um método da classe forms.Form, possivel verificar no django shell
        # crsf token, torna um formulário único, medida de segurança
        if form.is_valid():
            form.send_mail()
            # função vinda de forms.py
            messages.success(request, 'Email sent successfully!')
            form = ContactForm()
        else:
            messages.error(request, 'Error sending email.')
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def product(request):
    if str(request.method) == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # isso somente para salvar dados

            messages.success(request, 'Product Saved successfull.')
            form = ProductModelForm()
        else:
            messages.error(request, 'Error to save a Product')
    else:
        form = ProductModelForm()
    context = {
        'form': form
    }
    return render(request, 'product.html', context)
