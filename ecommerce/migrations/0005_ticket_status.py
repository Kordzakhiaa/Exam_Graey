# Generated by Django 3.1.6 on 2021-02-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20210220_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], default='available', max_length=50),
        ),
    ]
