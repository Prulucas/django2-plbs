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
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print('mensagem enviada')
            print(f'{name}, from {email}')
            print(f'subject {subject} says: {message}')
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
