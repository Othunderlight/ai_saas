# Generated by Django 5.0.6 on 2024-08-03 04:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0002_aimodel_main_tag_aimodel_short_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='aimodel',
            name='img',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='chatgroup',
            name='ai_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ai.aimodel'),
        ),
    ]
