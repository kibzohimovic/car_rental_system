# Generated by Django 3.1.5 on 2021-01-30 21:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcarmodel',
            name='choose_car',
            field=models.CharField(choices=[('BW', 'BMW'), ('AI', 'AUDI'), ('LS', 'Lexus')], default='BW', max_length=100),
        ),
        migrations.AddField(
            model_name='bookcarmodel',
            name='location',
            field=models.CharField(choices=[('MK', 'MUKONO'), ('KA', 'KAMPALA'), ('KI', 'KIREKA'), ('GZ', 'GAYAZA'), ('SA', 'SEETA'), ('BE', 'BWEYOGERERE'), ('BA', 'BANDA'), ('KE', 'KAWEMPE'), ('MA', 'MAKINDYE')], default='KA', max_length=100),
        ),
        migrations.AddField(
            model_name='bookcarmodel',
            name='pick_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookcarmodel',
            name='return_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]