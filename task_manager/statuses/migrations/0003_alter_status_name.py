# Generated by Django 4.2.4 on 2023-09-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
