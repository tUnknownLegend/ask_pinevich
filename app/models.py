from django.db import models
from django.contrib.auth.models import User
from collections import Counter

# from django.utils import timezone

'''
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    # username = models.CharField(max_length=128, blank=False, unique=True, verbose_name='Email', name='email')
    #email = models.EmailField(_("email address"), blank=True, unique=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # user_name = models.CharField(max_length=30)
    # email = models.CharField(max_length=30)
    # country = models.CharField(max_length=30)
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

'''


class Profile(models.Model):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # user_name = models.CharField(max_length=30)
    # email = models.CharField(max_length=30)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # country = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(blank=True)

    # def __str__(self):
    #    return f"{self.first_name} {self.last_name}"


class QuestionManager(models.Manager):
    def filter_by_tag(self):
        return self.filter(tag__isnull=True)

    def hot(self):
        return self.order_by('-rating')

    def latest(self):
        return self.order_by('-release_date')


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User, models.PROTECT)
    release_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="question_tag")
    rating = models.IntegerField(blank=True, null=True)
    objects = QuestionManager()

    def rating_up(self):
        self.rating += 1
        self.save()

    def rating_down(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.title

    def get_tags(self):
        return self.tags


class Answer(models.Model):
    author = models.ForeignKey(User, models.PROTECT)
    question = models.ForeignKey(Question, models.PROTECT, related_name="answers", null=True)
    correct = models.BooleanField(blank=True, null=True)
    release_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    rating = models.IntegerField(blank=True, null=True)

    def rating_up(self):
        self.rating += 1
        self.save()

    def rating_down(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f"{self.author} on {self.question}"
