# Generated by Django 3.2.7 on 2021-09-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210916_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(choices=[('about', 'about'), ('Services', 'Services'), ('Slider', 'Slider'), ('Welcome', 'Welcome'), ('Major Services', 'Major Services'), ('Vision', 'Vision'), ('Mission', 'Mission'), ('Docs', 'Docs'), ('Services Content', 'Services Content'), ('Other services', 'Other services'), ('Why', 'Why choose us?')], max_length=255),
        ),
    ]
