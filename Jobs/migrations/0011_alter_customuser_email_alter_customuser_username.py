# Generated by Django 4.2.7 on 2023-11-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0010_alter_customuser_email_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
