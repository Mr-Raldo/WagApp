# Generated by Django 5.0.1 on 2024-01-14 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_rename_answer_comment_answer_coment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionpage',
            name='question_text',
        ),
    ]
