from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
amtOfQuestions = 5
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
    } for i in range(3)
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


def index(request):
    return render(request, "index.html", {"questions": QUESTIONS, "tags": TAGS, "members": MEMBERS})


def ask(request):
    return render(request, "ask.html", {"tags": TAGS, "members": MEMBERS})


def question(request, i: int):
    return render(request, "question-page.html",
                  {"question": QUESTIONS[i], "tags": TAGS, "members": MEMBERS, "answers": ANSWERS})


def base(request):
    return render(request, "inc/base.html")


def hot(request):
    return render(request, "index.html", {"questions": QUESTIONS, "tags": TAGS, "members": MEMBERS})


def tag(request, s: str):
    return render(request, "index.html", {"questions": QUESTIONS, "tags": TAGS, "members": MEMBERS})


def logIn(request):
    return render(request, "log-in.html", {"tags": TAGS, "members": MEMBERS})


def signUp(request):
    return render(request, "sign-up.html", {"tags": TAGS, "members": MEMBERS})

def settings(request):
    return render(request, "settings.html", {"tags": TAGS, "members": MEMBERS})
