# Generated by Django 3.2.7 on 2021-09-16 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(choices=[('about', 'about'), ('Services', 'Services'), ('Slider', 'Slider'), ('Welcome', 'Welcome'), ('Major Services', 'Major Services'), ('Vision', 'Vision'), ('Mission', 'Mission'), ('Sub-about', 'Sub-about'), ('Services Content', 'Services Content')], max_length=255),
        ),
    ]
