# Generated by Django 3.1.1 on 2021-09-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_patientregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.CharField(max_length=350)),
            ],
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='age',
            field=models.IntegerField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='dateofbirth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='describeproblem',
            field=models.CharField(max_length=350),
        ),
    ]
