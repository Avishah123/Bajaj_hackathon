# Generated by Django 4.0.5 on 2022-06-08 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('customer', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('provider_name', models.TextField(blank=True, null=True)),
                ('provider_address', models.TextField(blank=True, null=True)),
                ('provider_pin', models.TextField(blank=True, null=True)),
                ('provider_city', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.TextField()),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.invoice')),
            ],
        ),
    ]
