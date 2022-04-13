from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from app.models import Question, Answer, Tag, Profile, User


# Create your views here.

def paginate(objects_list, request, per_page=3):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    res = paginator.get_page(page)
    return res


def index(request):
    q = Question.objects.latest()
    t = q[:10]
    q = paginate(q, request)
    return render(request, "index.html", {"questions": q, "tags": t})


def hot(request):
    q = Question.objects.hot()
    t = q[:10]
    q = paginate(q, request)
    return render(request, "index.html", {"questions": q, "tags": t})


def ask(request):
    return render(request, "ask.html", {"tags": Question.objects.hot()[:10]})


def question(request, i: int):
    q = Question.objects.get(id=i)

    return render(request, "question-page.html",
                  {"question": q, "tags": Question.objects.hot()[:10]})


def question_rating_up(request, i: int):
    q = Question.objects.get(id=i)
    q.rating_up()
    return redirect(request.META['HTTP_REFERER'])


def question_rating_down(request, i: int):
    q = Question.objects.get(id=i)
    q.rating_down()
    return redirect(request.META['HTTP_REFERER'])


def answer_rating_up(request, i: int):
    q = Answer.objects.get(id=i)
    q.rating_up()
    return redirect(request.META['HTTP_REFERER'])


def answer_rating_down(request, i: int):
    q = Answer.objects.get(id=i)
    q.rating_down()
    return redirect(request.META['HTTP_REFERER'])


'''
def custom_handler_404(request):
    response = render(request, '404.html', )
    response.status_code = 404
    return response
'''


def tag(request, s: str):
    try:
        t = Tag.objects.get(title=s)
    except:
        return HttpResponse(status=404)

    q = Question.objects.filter(tags=t.id)
    q = paginate(q, request)
    return render(request, "index.html",
                  {"questions": q, "tags": Question.objects.hot()[:10]})


def log_in(request):
    return render(request, "log-in.html", {"tags": Question.objects.hot()[:10]})


def sign_up(request):
    return render(request, "sign-up.html", {"tags": Question.objects.hot()[:10]})


def settings(request):
    return render(request, "settings.html", {"tags": Question.objects.hot()[:10]})
