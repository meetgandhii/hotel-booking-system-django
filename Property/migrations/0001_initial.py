# Generated by Django 3.2 on 2021-05-03 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_type', models.CharField(choices=[('R', 'Rent'), ('S', 'Sale')], default='S', max_length=1)),
                ('price', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=5)),
                ('number_of_rooms', models.PositiveIntegerField()),
                ('number_of_bathrooms', models.PositiveIntegerField()),
                ('number_of_parking', models.PositiveIntegerField()),
            ],
        ),
    ]
