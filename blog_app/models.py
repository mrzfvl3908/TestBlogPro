from django.db import models


class Post(models.Model):
    #category
    #author
    #image
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()
    counted_views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
