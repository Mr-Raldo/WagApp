# Generated by Django 5.0.1 on 2024-01-15 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_questionnairepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_title', models.CharField(max_length=100)),
                ('question_text', models.CharField(max_length=100)),
                ('response_text', models.CharField(max_length=255)),
            ],
        ),
    ]
