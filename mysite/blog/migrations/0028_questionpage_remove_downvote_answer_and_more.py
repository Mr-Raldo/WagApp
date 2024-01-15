# Generated by Django 5.0.1 on 2024-01-14 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_alter_qamodelpage_answer'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('question_text', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=300)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='downvote',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='downvote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='qamodelpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='user',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='detail',
            new_name='answer_text',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='add_time',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='DownVote',
        ),
        migrations.DeleteModel(
            name='QAModelPage',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='UpVote',
        ),
    ]