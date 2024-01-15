from django.db import models
from django import forms
# Add these:


from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import User
from wagtail.models import Page , Orderable 

from wagtail.fields import RichTextField

from wagtail.admin.panels import  FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from django.contrib import admin

from django.forms import ModelForm
from wagtail.fields import StreamField

from wagtail import blocks


from modelcluster.contrib.taggit import  ClusterTaggableManager
from taggit.models import TaggedItemBase


# * To capture responses from questionnaire page
class Response(models.Model):
    section_title = models.CharField(max_length=100)
    question_text = models.CharField(max_length=100)
    response_text = models.CharField(max_length=255)


class QuestionnaireSection(blocks.StructBlock):
    section_title = blocks.CharBlock(required=True, help_text='Title of the section')
    questions = blocks.ListBlock(
        blocks.StructBlock([
            ('question_text', blocks.CharBlock(required=True, help_text='Question text')),
            ('question_type', blocks.ChoiceBlock(choices=[
                ('text', 'Text'),
                ('multiple_choice', 'Multiple Choice'),
                # Add more question types as needed
            ], icon='radio-full')),
        ])
    )


class QuestionnairePage(Page):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    sections = StreamField([
        ('section', QuestionnaireSection()),
    ], use_json_field=True)  # Add use_json_field=True here

    content_panels = Page.content_panels + [
        FieldPanel('user'),
        FieldPanel('sections'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('user'),
        FieldPanel('sections'),
    ]
    def get_context(self, request):
        context = super().get_context(request)
        # Retrieve and add the objects to the context
        questionnaire_objects = QuestionnairePage.objects.all()  # Replace with your actual query
        context['questionnaire_objects'] = questionnaire_objects
        return context
# * Class to show who created the question--

#* Creating the question model

class QuestionPage(Page):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=300)
    question_text = models.CharField(max_length=255)
    
    content_panels = Page.content_panels + [
        FieldPanel('user'),
        
        FieldPanel('topic'),
        
        FieldPanel('question_text'),
        InlinePanel('answers', label='Answers'),
        
        ]
    def get_answers(self):
        
        return Answer.objects.filter(question=self)
    
    def get_questions(self):
        return QuestionPage.objects.all()
    # * For getting all the answers related to that question
   
#*  Creating the answer model
    
class Answer(models.Model):
    question = ParentalKey(QuestionPage, on_delete=models.CASCADE, null=True, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer_text = models.TextField()

    panels = [
        FieldPanel('user'),
        FieldPanel('answer_text'),
        
    ]

  
# * Adding a comment model

# class Comment(models.Model):
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True,  related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     add_time = models.DateTimeField(auto_now_add=True)
#     comment_text = models.TextField()

# #* Adding model for upvote 
# class UpVote(models.Model):
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="upvote_user")
    

# #* Adding model for down vote
# class DownVote(models.Model):
#     answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="downvote_user")
    




# * class for tag posts 
class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

#* Tag index page to let users click buttons of tags.

class BlogTagIndexPage(Page):
    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context



class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    authors = ParentalManyToManyField('blog.Author', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('authors', widget=forms.CheckboxSelectMultiple),

            # Add this:
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    # add the get_context method:
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]

@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='author'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('author_image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'


