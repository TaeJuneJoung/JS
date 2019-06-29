from django.db import models

# Create your models here.
class Love(models.Model):
    isLike = (
        (0, 'dislike'),
        (1, 'like'),
    )
    like = models.IntegerField(default=0, choices=isLike)