from django.shortcuts import render

# Create your views here.


def index(request):
    # articles = Review.objects.order_by('-pk')
    # context = {
    #     'articles': articles
    # }
    return render(request, 'reviews/index.html')