# Generated by Django 3.2.7 on 2021-09-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(choices=[('about', 'about'), ('Services', 'Services'), ('Slider', 'Slider'), ('Welcome', 'Welcome'), ('Major Services', 'Major Services'), ('Vision', 'Vision'), ('Mission', 'Mission')], max_length=255),
        ),
    ]
