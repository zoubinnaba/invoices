# Generated by Django 5.1.1 on 2024-09-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('Mr.', 'Mister'), ('Mr.', 'Miss')], max_length=3),
        ),
    ]
