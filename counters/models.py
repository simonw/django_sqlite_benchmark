from django.db import models


class Counter(models.Model):
    slug = models.SlugField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return "{}: {}".format(self.slug, self.count)
