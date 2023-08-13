# Generated by Django 4.1.7 on 2023-08-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0004_rename_assigned_time_jobcard_assigned_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RMA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rma_number', models.CharField(blank=True, max_length=200, null=True)),
                ('service_centre', models.CharField(blank=True, max_length=200, null=True)),
                ('date_returned', models.DateField(blank=True, null=True)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_person', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=200, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('inv_no', models.CharField(blank=True, max_length=200, null=True)),
                ('inv_date', models.DateField(blank=True, null=True)),
                ('item_code', models.CharField(blank=True, max_length=200, null=True)),
                ('package_condition', models.CharField(blank=True, max_length=200, null=True)),
                ('goods_condition', models.CharField(blank=True, max_length=200, null=True)),
                ('action', models.CharField(blank=True, choices=[('Repair', 'Repair'), ('Replace', 'Replace'), ('Refund', 'Refund')], max_length=10, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_signature', models.ImageField(blank=True, null=True, upload_to='')),
                ('serial_no', models.ManyToManyField(blank=True, null=True, to='system.jobcard')),
            ],
        ),
    ]