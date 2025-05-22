from django.urls import path
from .views import home,kurslar_view,kitoblar_view,contact_submit


urlpatterns = [
    path('', home, name='home'),
    path('kurslar/',kurslar_view, name='kurslar'),
    path('kitoblar/',kitoblar_view, name='kitoblarr'),
    path('contact-submit/', contact_submit, name='contact_submit'),

]
