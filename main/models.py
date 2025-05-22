from django.db import models

class Kurs(models.Model):
    nomi = models.CharField(max_length=255)
    daraja = models.CharField(max_length=50, choices=[("boshlang'ich", "Boshlang'ich"), ("o'rta", "O'rta"), ('yuqori', 'Yuqori')])
    davomiylik = models.CharField(max_length=50)
    baho = models.FloatField()
    reyting_izohi = models.CharField(max_length=100,blank=True,null=True)
    youtube_url = models.URLField()
    youtube_img = models.URLField()
    tomoshabinlar_soni = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi

class Kitob(models.Model):
    nomi = models.CharField(max_length=255)
    tavsif = models.TextField()
    rasm = models.ImageField(upload_to='kitob_rasmlar/')
    fayl = models.FileField(upload_to='kitob_fayllar/')

    def __str__(self):
        return self.nomi


class Contact(models.Model):
    name = models.CharField("Ism", max_length=100)
    email = models.EmailField("Email")
    created_at = models.DateTimeField("Yuborilgan vaqti", auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"