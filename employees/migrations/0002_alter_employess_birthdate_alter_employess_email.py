# Generated by Django 5.1.6 on 2025-02-26 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employess',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employess',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
