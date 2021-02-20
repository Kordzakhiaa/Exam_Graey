# Generated by Django 3.1.7 on 2021-02-20 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_end_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_start_date',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orders', to='ecommerce.ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='end_date',
            field=models.DateTimeField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='start_date',
            field=models.DateTimeField(verbose_name='Start Date'),
        ),
    ]
