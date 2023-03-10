# Generated by Django 4.1.4 on 2022-12-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alboom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='rasmlar')),
                ('sana', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlovha', models.CharField(max_length=200, verbose_name='Yangilik uchun sarlovha')),
                ('matn', models.TextField(verbose_name="Yangilik uchun to'liq ma'lumot")),
                ('sana', models.DateField(auto_now_add=True)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='rasmlar', verbose_name="Rasm kiriting(rasm bo'lmasa bosh qolishi mumkin)")),
            ],
        ),
    ]
