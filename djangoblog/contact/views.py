from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    human = False
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            human = True
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'human': human,
    })
