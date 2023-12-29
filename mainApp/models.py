from django.db import models
from django.contrib.auth.models import User


class Suv(models.Model):
    brend = models.CharField(max_length=255)
    narx = models.PositiveIntegerField()
    litr = models.PositiveIntegerField()
    batafsil = models.TextField()

    def __str__(self):
        return self.brend


class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    manzil = models.CharField(max_length=255)
    qarz = models.PositiveIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Admin(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveIntegerField()
    ish_vaqti = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Haydovchi(models.Model):
    ism = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    kiritilgan_sana = models.DateField()

    def __str__(self):
        return self.ism


class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField()
    umumiy_narx = models.PositiveIntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.mijoz.ism
