# Generated by Django 4.0.5 on 2022-06-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('phonenumber', models.IntegerField()),
                ('select', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='product_image/')),
            ],
        ),
    ]
