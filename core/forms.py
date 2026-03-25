from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, min_length=10)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Subject', max_length=200)  # assunto
    message = forms.CharField(label='Message', widget=forms.Textarea())
