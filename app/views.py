from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

# Create your views here.
amtOfQuestions = 10
question_list = []
for i in range(amtOfQuestions):
    question_list.append(i)

tagList = []
for i in range(amtOfQuestions):
    tagList.append(["SQL", "Python"])
amountOfAns = range(amtOfQuestions)
rating = range(amtOfQuestions)

QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"This is text for question #{i}",
        "number": i,
        "tag": tagList[i],
        "amountOfAns": amountOfAns[i],
        "rating": rating[i]
    } for i in range(amtOfQuestions)
]

ANSWERS = [
    {
        "text": f"This is text for ans #{i}",
        "number": i,
        "rating": rating[i]
    } for i in range(10)
]

tagName = ["perl", "C", "SQL", "python", "C++", "Pascal", "Basic", "ASCII", "Django", "Web", "git"]

TAGS = [
    {
        "title": tagName[i]
    } for i in range(len(tagName))
]

memberName = ["Mr. Who", "Mr. What", "Mr. Where", "Mr. Why", "Mr. How"]

MEMBERS = [
    {
        "title": memberName[i]
    } for i in range(len(memberName))
]


def paginate(objects_list, request, per_page=3):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    # page1 = paginator.page(1)
    # page_range = paginator.page_range
    res = paginator.get_page(page)
    return res


def index(request):
    p = paginate(QUESTIONS, request)
    return render(request, "index.html", {"questions": p, "tags": TAGS, "members": MEMBERS})


def ask(request):
    return render(request, "ask.html", {"tags": TAGS, "members": MEMBERS})


def question(request, i: int):
    return render(request, "question-page.html",
                  {"question": QUESTIONS[i], "tags": TAGS, "members": MEMBERS, "answers": ANSWERS})


def hot(request):
    p = paginate(QUESTIONS, request)
    return render(request, "index.html", {"questions": p, "tags": TAGS, "members": MEMBERS})


def custom_handler_404(request):
    response = render(request, '404.html', )
    response.status_code = 404
    return response


def tag(request, s: str):
    for j in tagList:
        if s in j:
            return render(request, "index.html",
                          {"questions": paginate(QUESTIONS, request), "tags": TAGS, "members": MEMBERS})
        else:
            return HttpResponse(status=404)


def log_in(request):
    return render(request, "log-in.html", {"tags": TAGS, "members": MEMBERS})


def sign_up(request):
    return render(request, "sign-up.html", {"tags": TAGS, "members": MEMBERS})


def settings(request):
    return render(request, "settings.html", {"tags": TAGS, "members": MEMBERS})
