# Generated by Django 2.1.7 on 2019-04-04 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_auto_20190330_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]