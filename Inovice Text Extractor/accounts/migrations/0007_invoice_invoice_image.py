# Generated by Django 4.0.5 on 2022-06-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_hotel_main_img_hotel_invoice_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='invoice_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]