# Generated by Django 4.0.4 on 2022-05-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0004_jobmodel_defaultapplicationform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='defaultApplicationForm',
            field=models.CharField(choices=[('0', 'Default Application Form'), ('1', 'Customise Application Form')], max_length=2),
        ),
    ]