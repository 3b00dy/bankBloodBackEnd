# Generated by Django 3.2.9 on 2022-03-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodBank', '0009_alter_volunteers_volunteerage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteers',
            name='volunteerAge',
            field=models.IntegerField(null=True, verbose_name='volunteerAge'),
        ),
    ]
