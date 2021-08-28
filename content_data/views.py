from django.shortcuts import render
from .models import home, about, contact, work, footer
from .forms import contact_form

# Create your views here.

def views_page(request):
    home_models = home.objects.all()
    about_models = about.objects.all()
    work_model = work.objects.all()
    footer_model = footer.objects.all()

    form_contact = contact_form(request.POST or None)
    if form_contact.is_valid():
        full_name = form_contact.cleaned_data.get('full_name')
        email = form_contact.cleaned_data.get('email')
        text = form_contact.cleaned_data.get('text')
        contact.objects.create(full_name=full_name, email=email, text=text, is_read=False)
        form_contact = contact_form()

    context = {
        'models': home_models,
        'about_models': about_models,
        'contact_form': form_contact,
        'work_model': work_model,
        'footer_model': footer_model,
    }

    return render(request, "index.html", context)