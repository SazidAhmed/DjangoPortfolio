# Generated by Django 3.0.6 on 2020-06-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_interest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('workflow', models.CharField(max_length=150)),
            ],
        ),
    ]
