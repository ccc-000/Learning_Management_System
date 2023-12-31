# Generated by Django 4.1.7 on 2023-04-18 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hydra_learning_management_system', '0013_alter_assessments_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessments',
            name='grade',
            field=models.TextField(default='{"quiz": [], "ass": [], "final exam": 0}'),
        ),
        migrations.CreateModel(
            name='LiveStream',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('attendance', models.TextField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hydra_learning_management_system.courses')),
                ('creatorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hydra_learning_management_system.users')),
            ],
        ),
    ]
