# Generated by Django 5.0.2 on 2024-05-01 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_users_end_time_remove_users_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='face_id_photos/')),
            ],
        ),
    ]
