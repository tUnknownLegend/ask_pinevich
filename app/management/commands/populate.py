from itertools import islice
from random import randrange
from django.core.management.base import BaseCommand, CommandError
from app.models import Question, Answer, Tag, Profile, User


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        tag_name = ["perl", "C", "SQL", "python", "C++", "Pascal", "Basic", "ASCII", "Django", "Web"]
        tag_range = 10001
        t_list = []
        for j in range(tag_range):
            for i in tag_name:
                t = Tag(title=i + '%s' % j)
                t_list.append(t)
                #  t.save()
        Tag.objects.bulk_create(t_list, tag_range)
        self.stdout.write(self.style.SUCCESS('Successfully created t'))

        u_list = []
        u_range = 10001
        for i in range(u_range):
            u = User(first_name='Name%s' % i, last_name='Surname%s' % i, email='email%s@example.com' % i,
                     username='username%s' % i)
            # u.save()
            u_list.append(u)
        User.objects.bulk_create(u_list, u_range)
        self.stdout.write(self.style.SUCCESS('Successfully created u'))

        q_list = []
        q_range = 100001
        for i in range(q_range):
            q = Question(author=u_list[randrange(0, u_range - 1)], title="test question %s" % i,
                         text="Text for question %s" % i, rating=randrange(-999, 999))
            q.save()

            q.tags.add(t_list[randrange(0, tag_range * len(tag_name) - 1)],
                       t_list[randrange(0, tag_range * len(tag_name) - 1)])
            q.save()
            q_list.append(q)
        # Question.objects.bulk_create(q_list, q_range)
        self.stdout.write(self.style.SUCCESS('Successfully created q'))
        '''
        for i in q_list:
            i.tags.add(t_list[randrange(0, tag_range * len(tag_name) - 1)],
                       t_list[randrange(0, tag_range * len(tag_name) - 1)])
            # q.save()
        Question.objects.bulk_update(q_list, q_range)
        self.stdout.write(self.style.SUCCESS('Successfully created q'))
        '''
        a_list = []
        a_range = 1000001
        for i in range(a_range):
            a = Answer(author=u_list[randrange(0, u_range - 1)], text="Text for answer %s" % i,
                       rating=randrange(-999, 999),
                       question=q_list[randrange(0, q_range - 1)], correct=randrange(0, 1))
            # a.save()
            a_list.append(a)
        Answer.objects.bulk_create(a_list, a_range)
        self.stdout.write(self.style.SUCCESS('Successfully created a'))


'''
amtOfQuestions = 10
question_list = []
for i in range(amtOfQuestions):
    question_list.append(i)

tagList = []
for i in range(amtOfQuestions):
    tagList.append(["SQL", "Python"])
amountOfAns = range(amtOfQuestions)
rating = range(amtOfQuestions)

tagName = ["perl", "C", "SQL", "python", "C++", "Pascal", "Basic", "ASCII", "Django", "Web"]

memberName = ["Mr. Who", "Mr. What", "Mr. Where", "Mr. Why", "Mr. How", "Ms. Who", "Ms. What", "Ms. Where", "Ms. Why",
              "Ms. How"]

def gen_data(Entry, objs, batch_size):
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        Entry.objects.bulk_create(batch, batch_size)


batch_size = 10001
user = (User(id=i, first_name='Name%s' % i, last_name='Surname%s' % i, email='email%s@example.com' % i,
             username='username%s' % i) for i in range(batch_size))
gen_data(User, user, batch_size)

# profile = (Profile(user=User.objects.get(id=i)) for i in range(batch_size))
# gen_data(Profile, profile, batch_size)

batch_size = 10001
tag = (Tag(title="Tag #%s") for i in range(batch_size))
gen_data(Tag, tag, batch_size)

batch_size = 100001
question = (Question(author=User.objects.get(id=random.randrange(0, 10000), tags={
    Tag.objects.get(id=random.randrange(0, 10000), Tag.objects.get(id=random.randrange(0, 10000)},
                                             text='Text for question #%s', tags="") for
                     i in range(batch_size))
            gen_data(Question, question, batch_size)

batch_size = 1000001
answer = (Answer(title="Tag #%s") for i in range(batch_size))
gen_data(Answer, answer, batch_size)
'''
