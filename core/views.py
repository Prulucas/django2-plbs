from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


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
    return render(request, 'product.html')
