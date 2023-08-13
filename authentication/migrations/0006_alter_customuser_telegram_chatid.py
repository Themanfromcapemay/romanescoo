# Generated by Django 4.1.7 on 2023-08-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_customuser_telegram_chatid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='telegram_ChatID',
            field=models.CharField(blank=True, choices=[('Middelburg SC', 'Middelburg SC'), ('Polokwane SC', 'Polokwane SC'), ('Cape Town SC', 'Cape Town SC'), ('Johannesburg SC', 'Johannesburg SC'), ('Bloemfontein SC', 'Bloemfontein SC'), ('Port Elizabeth SC', 'Port Elizabeth SC'), ('Durban SC', 'Durban SC'), ('MRE JHB', 'MRE JHB')], max_length=100, null=True),
        ),
    ]