# Generated by Django 3.1.6 on 2021-02-22 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_ticket_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_date']},
        ),
    ]
