from django.contrib import admin
from infotrace.requests.models import Query

class QueryAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_site', 'to_domain', 'protocol')
    list_filter = ('from_site', 'to_domain', 'protocol')
    ordering = ('name', 'from_site', 'to_domain', 'protocol')


#class TimingAdmin(admin.ModelAdmin):
#    list_display = ('run_at', 'cron', 'queries')
#    ordering = ('queries',)

admin.site.register(Query) 
#admin.site.register(Timing, TimingAdmin) 

