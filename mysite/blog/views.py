#views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from .forms import ResponseForm
from . models import QuestionnairePage
from . serializers import QuestionSerializer

# * Function to get inout from users of questions only page questionnaire_page.html
#* Not yet working though
def submit_response(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or return a success message
            return redirect('questionnaire_page.html')  # Replace 'success_page' with the actual name of your success page URL
    else:
        form = ResponseForm()
    return render(request, 'questionnaire_page.html', {'form': form})


@api_view(['GET'])
def getRoutes(request):
    routes=[
       {
    "meta": {
        "total_count": 16
    },
    "items": [
        {
            "id": 3,
            "meta": {
                "type": "home.HomePage",
                "detail_url": "http://localhost/api/v2/pages/3/",
                "html_url": "http://localhost/",
                "slug": "home",
                "first_published_at":"2024-01-11T07:01:44.959296Z"
            },
            "title": "Home"
        },
        {
            "id": 4,
            "meta": {
                "type": "blog.BlogIndexPage",
                "detail_url": "http://localhost/api/v2/pages/4/",
                "html_url": "http://localhost/blog/",
                "slug": "blog",
                "first_published_at": "2024-01-11T07:01:44.959296Z"
            },
            "title": "Our blog"
        },
        {
            "id": 5,
            "meta": {
                "type": "blog.BlogPage",
                "detail_url": "http://localhost/api/v2/pages/5/",
                "html_url": "http://localhost/blog/first-blog-post/",
                "slug": "first-blog-post",
                "first_published_at": "2024-01-11T07:10:01.121023Z"
            },
            "title": "First Blog Post"
        },
        {
            "id": 6,
            "meta": {
                "type": "blog.BlogPage",
                "detail_url": "http://localhost/api/v2/pages/6/",
                "html_url": "http://localhost/blog/second-blog-post/",
                "slug": "second-blog-post",
                "first_published_at": "2024-01-11T07:11:58.594743Z"
            },
            "title": "Second Blog Post"
        },
        {
            "id": 7,
            "meta": {
                "type": "blog.BlogPage",
                "detail_url": "http://localhost/api/v2/pages/7/",
                "html_url": "http://localhost/blog/third-blog-post/",
                "slug": "third-blog-post",
                "first_published_at": "2024-01-11T09:06:17.505129Z"
            },
            "title": "third blog post"
        },
        {
            "id": 8,
            "meta": {
                "type": "blog.BlogPage",
                "detail_url": "http://localhost/api/v2/pages/8/",
                "html_url": "http://localhost/blog/fourth-blog-post/",
                "slug": "fourth-blog-post",
                "first_published_at": "2024-01-11T09:33:42.621189Z"
            },
            "title": "Fourth Blog Post"
        },
        {
            "id": 9,
            "meta": {
                "type": "blog.BlogPage",
                "detail_url": "http://localhost/api/v2/pages/9/",
                "html_url": "http://localhost/blog/fitth-blog-post/",
                "slug": "fitth-blog-post",
                "first_published_at": "2024-01-11T10:21:03.119624Z"
            },
            "title": "Fitth blog post"
        },
        {
            "id": 11,
            "meta": {
                "type": "blog.BlogPage",
                "detail_url": "http://localhost/api/v2/pages/11/",
                "html_url": "http://localhost/blog/i-want-to-continue-to-grow-as-a-brand-and-empower-more-individuals-by-being-a-pioneer-in-the-vegan-community-as-an-african-vegan-chef-says-chef-cola-founder-at-african-vegan-on-a-budget/",
                "slug": "i-want-to-continue-to-grow-as-a-brand-and-empower-more-individuals-by-being-a-pioneer-in-the-vegan-community-as-an-african-vegan-chef-says-chef-cola-founder-at-african-vegan-on-a-budget",
                "first_published_at": "2024-01-15T08:16:20.809613Z"
            },
            "title": "“I WANT TO CONTINUE TO GROW AS A BRAND AND EMPOWER MORE INDIVIDUALS BY BEING A PIONEER IN THE VEGAN COMMUNITY AS AN AFRICAN VEGAN CHEF” SAYS CHEF COLA FOUNDER AT AFRICAN VEGAN ON A BUDGET"
        },
        {
            "id": 10,
            "meta": {
                "type": "blog.BlogTagIndexPage",
                "detail_url": "http://localhost/api/v2/pages/10/",
                "html_url": "http://localhost/tags/",
                "slug": "tags",
                "first_published_at": "2024-01-11T18:01:36.458390Z"
            },
            "title": "Tags Page"
        },
        {
            "id": 14,
            "meta": {
                "type": "blog.QuestionPage",
                "detail_url": "http://localhost/api/v2/pages/14/",
                "html_url": "http://localhost/questionpage/",
                "slug": "questionpage",
                "first_published_at": "2024-01-14T11:21:59.093280Z"
            },
            "title": "Q/A"
        },
        {
            "id": 16,
            "meta": {
                "type": "blog.QuestionPage",
                "detail_url": "http://localhost/api/v2/pages/16/",
                "html_url": "http://localhost/question/",
                "slug": "question",
                "first_published_at": "2024-01-14T19:50:06.020520Z"
            },
            "title": "Q/A"
        },
        {
            "id": 17,
            "meta": {
                "type": "blog.QuestionPage",
                "detail_url": "http://localhost/api/v2/pages/17/",
                "html_url": "http://localhost/qa/",
                "slug": "qa",
                "first_published_at": "2024-01-14T21:29:14.959253Z"
            },
            "title": "Q/A"
        },
        {
            "id": 18,
            "meta": {
                "type": "blog.QuestionPage",
                "detail_url": "http://localhost/api/v2/pages/18/",
                "html_url": "http://localhost/qaa/",
                "slug": "qaa",
                "first_published_at": "2024-01-14T21:47:27.409039Z"
            },
            "title": "Q/A"
        },
        {
            "id": 19,
            "meta": {
                "type": "blog.QuestionnairePage",
                "detail_url": "http://localhost/api/v2/pages/19/",
                "html_url": "http://localhost/sq/",
                "slug": "sq",
                "first_published_at": "2024-01-15T01:31:53.810581Z"
            },
            "title": "S/Q"
        },
        {
            "id": 20,
            "meta": {
                "type": "blog.QuestionnairePage",
                "detail_url": "http://localhost/api/v2/pages/20/",
                "html_url": "http://localhost/sqq/",
                "slug": "sqq",
                "first_published_at": "2024-01-15T02:57:45.301833Z"
            },
            "title": "SQ"
        },
        {
            "id": 21,
            "meta": {
                "type": "blog.BlogPage",
                "detail_url": "http://localhost/api/v2/pages/21/",
                "html_url": "http://localhost/bussness/",
                "slug": "bussness",
                "first_published_at": "2024-01-15T08:46:24.862140Z"
            },
            "title": "Bussness"
        }
    ]
}
    ]

    return Response(routes)



@api_view(['GET'])
def getQuestions(request):
    question = QuestionnairePage.objects.all()
    serializer = QuestionSerializer(question, many=True)
    return Response(serializer.data)