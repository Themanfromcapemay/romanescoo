# Generated by Django 4.1.7 on 2023-08-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0004_rename_recieved_at_warehouse_rma_converted_or_closed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rma',
            name='goods_condition',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rma',
            name='package_condition',
            field=models.CharField(blank=True, choices=[('Intact', 'Intact'), ('Damaged', 'Damaged'), ('Sealed', 'Sealed'), ('No Packaging', 'No Packaging')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rma',
            name='service_centre',
            field=models.CharField(blank=True, choices=[('Johannesburg Centre', 'Johannesburg Centre'), ('Durban Service Centre', 'Durban Service Centre')], max_length=200, null=True),
        ),
    ]
