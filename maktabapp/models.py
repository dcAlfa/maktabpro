from django.db import models

from Userapp.models import Account


class Fanlar(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom}"

class Oqtuvchi(models.Model):
    ism_familya = models.CharField(max_length=50)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    fan = models.ManyToManyField(Fanlar)

    def __str__(self):
        return f"{self.ism_familya}  ({self.fan})"


class Sinf(models.Model):
    a = (
        ("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11"),
    )
    b = (
        ("Green","Green"),("Blue","Blue")
    )
    sinf = models.CharField(max_length=50,choices=a)
    nomi = models.CharField(max_length=50,choices=b)
    fanlar = models.ManyToManyField(Fanlar)

    def __str__(self):
        return f"{self.sinf}-{self.nomi}"

class Oquvchi(models.Model):
    ism_familya = models.CharField(max_length=50)
    sinf = models.ForeignKey(Sinf, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.ism_familya}  ({self.sinf})"

class Chorak(models.Model):
    oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE)
    oqtuvchi = models.ForeignKey(Oqtuvchi, on_delete=models.CASCADE)
    baho1 = models.PositiveIntegerField(blank=True,null=True)
    baho2 = models.PositiveIntegerField(blank=True,null=True)
    baho3 = models.PositiveIntegerField(blank=True,null=True)
    baho4 = models.PositiveIntegerField(blank=True,null=True)

