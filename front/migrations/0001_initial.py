# Generated by Django 3.2.12 on 2023-08-28 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='', max_length=400)),
                ('des', models.TextField(default='', max_length=3000)),
                ('date', models.DateField(default='')),
                ('image', models.FileField(default='', upload_to='static')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.cate')),
            ],
        ),
    ]
