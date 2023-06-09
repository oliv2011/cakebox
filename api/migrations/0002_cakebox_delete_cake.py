# Generated by Django 4.1.4 on 2023-04-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CakeBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('shape', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('layers', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('weight', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cake',
        ),
    ]
