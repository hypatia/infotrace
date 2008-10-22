from django.db import models

class Traceroute(models.Model):
    output = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return '%s %s' % (self.name, self.date)

