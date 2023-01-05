# Generated by Django 4.1.5 on 2023-01-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('AV', 'available'), ('PR', 'in-progress'), ('RW', 'in-review'), ('RV', 'in-revision'), ('CL', 'closed')], default='AV', max_length=100),
        ),
    ]
