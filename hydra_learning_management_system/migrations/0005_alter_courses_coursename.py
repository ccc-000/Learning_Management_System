# Generated by Django 4.1.7 on 2023-04-10 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydra_learning_management_system', '0004_rename_perferredlanguage_users_preferredlanguage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='coursename',
            field=models.CharField(max_length=60),
        ),
    ]
