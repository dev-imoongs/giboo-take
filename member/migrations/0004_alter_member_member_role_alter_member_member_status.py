# Generated by Django 4.2.4 on 2023-08-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_donation_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_role',
            field=models.CharField(default='MEMBER', max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_status',
            field=models.CharField(default='NORMAL', max_length=10),
        ),
    ]