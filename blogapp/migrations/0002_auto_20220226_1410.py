# Generated by Django 2.2 on 2022-02-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
