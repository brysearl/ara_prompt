# Generated by Django 2.0.2 on 2018-02-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('matcher', models.CharField(choices=[('MATCHER1', 'search matcher 1'), ('MATCHER2', 'search matcher 2')], max_length=64)),
            ],
        ),
    ]
