# Generated by Django 5.0.4 on 2024-04-30 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_is_staff_alter_customuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='color',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
