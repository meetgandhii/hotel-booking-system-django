# Generated by Django 3.2 on 2021-05-07 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactdetails',
            options={'verbose_name_plural': 'Contact Details'},
        ),
        migrations.AlterField(
            model_name='contactdetails',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
