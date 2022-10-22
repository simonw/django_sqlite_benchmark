from django.db import models


class Row(models.Model):
    name = models.TextField()
    campaign = models.TextField()
    voice = models.TextField()
    recognize = models.TextField()
    inside = models.FloatField()
    growth = models.TextField()
    side = models.FloatField()
    yard = models.TextField()
    discussion = models.TextField()

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "name": self.name,
            "campaign": self.campaign,
            "voice": self.voice,
            "recognize": self.recognize,
            "inside": self.inside,
            "growth": self.growth,
            "side": self.side,
            "yard": self.yard,
            "discussion": self.discussion,
        }
