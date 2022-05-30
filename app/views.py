from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from app.models import *
from app.forms import *
from django.contrib.auth import login, authenticate


def paginate(objects_list, request, per_page=3):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    res = paginator.get_page(page)
    return res


def get_unique(iterable, n):
    seen = set()
    for e in iterable:
        if e.author in seen:
            continue
        seen.add(e.author)
        yield e
        if len(seen) == n:
            return seen


def index(request):
    q = Question.objects.latest()
    t = q[:10]
    m = get_unique(q[:50], 10)
    q = paginate(q, request)
    return render(request, "index.html", {"questions": q, "tags": t, "members": m})


def hot(request):
    q = Question.objects.hot()
    t = q[:10]
    m = get_unique(q[:50], 10)
    q = paginate(q, request)
    return render(request, "index.html", {"questions": q, "tags": t, "members": m})


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
                  {"questions": q, "tags": Question.objects.hot()[:10],
                   "members": get_unique(Question.objects.hot()[:50], 10)})


def log_in(request):
    # print(request.POST)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect("index")
        user_form = LoginForm()
    elif request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            # user = authenticate(request, **user_form.changed_data)

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user_form.clean()
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(request.path)

    return render(request, "log-in.html", {"tags": Question.objects.hot()[:10], "form": user_form,
                                           "members": get_unique(Question.objects.hot()[:50], 10)})


def sign_up(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect("index")
        user_form = SignUpForm()
    elif request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():

            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            email = user_form.cleaned_data['email']
            # user_form.save()
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("index")

    return render(request, "sign-up.html", {"tags": Question.objects.hot()[:10], "form": user_form,
                                            "members": get_unique(Question.objects.hot()[:50], 10)})


def settings(request):
    if request.method == 'GET':
        user_form = EditProfile(initial={"username": request.user.username, "email": request.user.email})
    elif request.method == 'POST':
        user_form = EditProfile(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            # avatar = user_form.cleaned_data['avatar']

            user = request.user
            user.username = username
            user.email = email
            user.save()

            if user:
                return redirect(request.META['HTTP_REFERER'])

    return render(request, "settings.html", {"tags": Question.objects.hot()[:10], "form": user_form,
                                             "members": get_unique(Question.objects.hot()[:50], 10)})


def ask(request):
    if request.method == 'GET':
        user_form = AddQuestion()
    elif request.method == 'POST':
        user_form = AddQuestion(request.POST)
        if user_form.is_valid():
            title = user_form.cleaned_data['title']
            body = user_form.cleaned_data['body']
            tags = user_form.cleaned_data['tags']

            q = Question(author=request.user, title=title,
                         text=body, rating=0)

            q.save()

            t_list = []

            for tag in tags:
                t = Tag(title=tag)
                t_list.append(t)
                t.save()

            for tag in t_list:
                q.tags.add(tag)
                q.save()
            if q:
                return redirect(request.META['HTTP_REFERER'])

    return render(request, "ask.html", {"tags": Question.objects.hot()[:10], "form": user_form,
                                        "members": get_unique(Question.objects.hot()[:50], 10)})


def question(request, i: int):
    q = Question.objects.get(id=i)

    if request.method == 'GET':
        user_form = AddAnswer()
    elif request.method == 'POST':
        user_form = AddAnswer(request.POST)
        if user_form.is_valid():
            body = user_form.cleaned_data['body']

            a = Answer(author=request.user, text=body,
                       rating=0,
                       question=q, correct=0)
            a.save()

            if a:
                return redirect(request.META['HTTP_REFERER'])

    return render(request, "question-page.html",
                  {"question": q, "tags": Question.objects.hot()[:10], "form": user_form,
                   "members": get_unique(Question.objects.hot()[:50], 10)})
