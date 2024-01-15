# Generated by Django 5.0.1 on 2024-01-15 01:29

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_delete_comment'),
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionnairePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('sections', wagtail.fields.StreamField([('section', wagtail.blocks.StructBlock([('section_title', wagtail.blocks.CharBlock(help_text='Title of the section', required=True)), ('questions', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question_text', wagtail.blocks.CharBlock(help_text='Question text', required=True)), ('question_type', wagtail.blocks.ChoiceBlock(choices=[('text', 'Text'), ('multiple_choice', 'Multiple Choice')], icon='radio-full'))])))]))], use_json_field=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
