# Generated by Django 5.0.2 on 2024-06-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_kelish_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ish_vaqti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ishkelish', models.TimeField()),
                ('ishketish', models.TimeField()),
            ],
        ),
    ]
