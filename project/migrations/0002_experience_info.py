# Generated by Django 3.0.6 on 2020-06-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('objective', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='resume/images/')),
            ],
        ),
    ]
