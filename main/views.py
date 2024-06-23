from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

def change_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        request.session['django_language'] = language
    return redirect(request.META.get('HTTP_REFERER', '/'))
