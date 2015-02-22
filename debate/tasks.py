import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "debate.settings")

import django
from django.contrib.auth.models import User
django.setup()

from invoke import task
from debate.base.models import Debate, Solution, Comment


@task
def make_users():
    usernames = ['harry', 'henry', 'zanzi']

    for username in usernames:
        User.objects.create_user(username, password='greatpass')


@task
def make_debates():
    title = "We need an easy way to debate on the internet"
    description = """
        We need an easy way to debate on the internet!
        We need an easy way to debate on the internet!
        We need an easy way to debate on the internet!
    """
    author = User.objects.get(username='henry')
    debate = Debate(
        title=title,
        description=description,
        author=author
    )
    debate.save()


@task
def make_solutions():
    solutions_text = [
        "Lest make a webssite to solve this",
        "Lest sell the website and become rich",
        "Lest move to hawaii and code all day",
    ]
    debate = Debate.objects.all().first()
    solutions = []
    for text in solutions_text:
        solution = Solution(text=text, debate=debate)
        solutions.append(solution)

    Solution.objects.bulk_create(solutions)


@task
def make_comments():
    solutions = list(Solution.objects.all())
    zanzi = User.objects.get(username='zanzi')
    comment = Comment(
        text='I disagree because the earth is flat',
        author=zanzi,
        solution=solutions[0]
    )
    comment.save()

    harry = User.objects.get(username='harry')
    comment2 = Comment(
        text='Challange accepted',
        author=harry,
        comment=comment
    )
    comment2.save()


@task
def make_data():
    make_users()
    make_debates()
    make_solutions()
    make_comments()
