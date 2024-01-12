from django.db import models
from django import forms
# Add these:
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.models import register_snippet

from wagtail.models import Page , Orderable 
from wagtail.fields import RichTextField
from wagtail.admin.panels import  FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index

# * Imports for tag posts
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


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


# ! Creating a class for Authors to rectify issue of Authors presence

# class  BlogAuthorsOrderable(Orderable):
#     """Allows to select one or more blog authors from stippents"""
#     page = ParentalKey("blog.BlogPage", related_name="blog_authors")
#     author= models.ForeignKey(
#         "blog.BlogAuthor", on_delete=models.CASCADE,
#     )

#     panels=[
#         FieldPanel("author"),
#     ]



# class BlogAuthor(models.Model):
#     name= models.CharField(max_length=255)
#     image = models.ForeignKey(
#          'wagtailimages.Image', null=True, blank=True,
#          on_delete=models.SET_NULL, related_name='+'
#     )

#     panels=[
#         MultiFieldPanel(
#             [
#                 FieldPanel("name"),
#                 FieldPanel("image"),
#             ],
#             heading="Name and Image",
#         )
#     ]
#     def __str__(self):
#          return self.name
#     class Meta:
#         verbose_name= "Blog Author"
#         verbose_name_plural = "Blog Authors"

