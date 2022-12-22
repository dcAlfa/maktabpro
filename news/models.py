from django.db import models

class News(models.Model):
    sarlovha = models.CharField(max_length=200, verbose_name="Yangilik uchun sarlovha")
    matn = models.TextField(verbose_name="Yangilik uchun to'liq ma'lumot")
    sana = models.DateField(auto_now_add=True)
    rasm = models.FileField(upload_to="rasmlar", blank=True, null=True, verbose_name="Rasm kiriting(rasm bo'lmasa bosh qolishi mumkin)")

    def __str__(self):
        return f"{self.sana}  {self.sarlovha}"

class Alboom(models.Model):
    rasm = models.FileField(upload_to="rasmlar")
    sana = models.DateField(auto_now_add=True)

