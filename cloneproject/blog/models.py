from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True) #if the user does not want to pulish it yet or if they do not want it at all.


#this here is to make sure that when the author is ready to post the blogs they get the date and time at the moment.
    def publish(self):
        self.published_date=timezone.now()
        self.save()

#here since the user is going to have comments that are approved and rejected we would only want to show the comments that have been approved.
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length = 200)
    text = models.TextField()
    created_date=models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_post_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
