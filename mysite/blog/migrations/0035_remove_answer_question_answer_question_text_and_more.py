# Generated by Django 5.0.1 on 2024-01-14 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_remove_questionpage_question_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='answer',
            name='question_text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.questionpage'),
        ),
        migrations.AddField(
            model_name='questionpage',
            name='question_text',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
