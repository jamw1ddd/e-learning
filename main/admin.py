from django.contrib import admin
from .models import Kurs, Kitob, Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")

admin.site.register(Kurs)
admin.site.register(Kitob)