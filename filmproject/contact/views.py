from django.shortcuts import render
from contact.models import ContactModel
from film.models import CategoryModel

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = ContactModel.objects.create(
            name = name,
            surname = surname,
            email = email,
            phone = phone,
            message = message
        )
    categories = CategoryModel.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'contact.html', context)