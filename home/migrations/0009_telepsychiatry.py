# Generated by Django 3.1.1 on 2021-09-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_content_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='telepsychiatry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('emailaddress', models.CharField(max_length=250)),
                ('phonenumber', models.CharField(max_length=250)),
                ('dateofbirth', models.DateField()),
                ('fulladdress', models.CharField(max_length=350)),
                ('Signature', models.CharField(max_length=350)),
                ('datesign', models.CharField(max_length=350)),
                ('signer', models.CharField(max_length=350)),
            ],
        ),
    ]
