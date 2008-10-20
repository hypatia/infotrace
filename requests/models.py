from django.db import models
from django.contrib import admin
#admin.site.register() 

class Query(models.Model):
    name = models.CharField(max_length=30)
    from_site = models.CharField(max_length=50)
    to_domain = models.CharField(max_length=50)
    protocol = models.CharField(max_length=30)

    def __str__(self):
        return self.name

#class QueryAdmin(admin.ModelAdmin):
#    model = Query


class Timing(models.Model):
    run_at = models.DateField()
    cron = models.CharField(max_length=30)
    queries = models.ManyToManyField(Query)

#class TimerAdmin(admin.ModelAdmin):
#    model = Timer

#admin.site.register(Query)
#admin.site.register(Timing)
