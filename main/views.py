from django.shortcuts import render,redirect
from .models import Kurs, Kitob
from .forms import ContactForm
from django.contrib import messages


def home(request):
    kurslar = Kurs.objects.all()[:3]
    kitoblar = Kitob.objects.all()[:6]
    return render(request, 'index.html', {'kurslar': kurslar, 'kitoblar': kitoblar})


def kurslar_view(request):
    kurslar = Kurs.objects.all()
    return render(request, 'lesson.html', {'kurslar': kurslar})


def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    return render(request, 'book.html', {'kitoblar': kitoblar})


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('/')