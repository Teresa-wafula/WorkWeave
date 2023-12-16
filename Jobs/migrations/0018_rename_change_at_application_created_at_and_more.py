# Generated by Django 4.2.7 on 2023-11-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0017_remove_job_change_at_application'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='change_at',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='job',
            name='change_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]