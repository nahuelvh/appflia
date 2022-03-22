# Generated by Django 4.0.3 on 2022-03-21 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=40)),
                ('fecha_nacimiento', models.DateField()),
                ('altura', models.FloatField()),
            ],
        ),
    ]