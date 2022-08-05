# Generated by Django 4.0.6 on 2022-08-03 10:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp2', '0005_task1_file_delete_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task1',
            name='file',
        ),
        migrations.CreateModel(
            name='TaskFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='file', validators=[django.core.validators.FileExtensionValidator(['pdf', 'jpg', 'gif', 'jpeg', 'bmp', 'ai', 'eps'])])),
                ('task1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='testapp2.task1')),
            ],
        ),
    ]