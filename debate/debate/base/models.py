from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Debate(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=6000)
    author = models.ForeignKey(User)
    url = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        return super(Debate, self).save(*args, **kwargs)


class Solution(models.Model):
    text = models.CharField(max_length=300)
    debate = models.ForeignKey(Debate, related_name='solutions')


class Comment(models.Model):
    text = models.CharField(max_length=200)
    solution = models.ForeignKey(
        Solution, related_name='solution_comments',
        blank=True, null=True
    )
    comment = models.ForeignKey(
        'base.Comment', related_name='comment_comments',
        blank=True, null=True
    )
    author = models.ForeignKey(
        User, related_name='user_comments'
    )


class Follow(models.Model):
    comment = models.ForeignKey(Comment, null=True, blank=True)
    debate = models.ForeignKey(Debate, null=True, blank=True)
    user = models.ForeignKey(User, related_name='followers')
