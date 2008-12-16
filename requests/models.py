from django.db import models
from django.contrib import admin

class Query(models.Model):
    name = models.CharField(max_length=30)
    from_sites = models.CharField(max_length=50) # list of origins
    to_domains = models.CharField(max_length=50) #list of destinations.  can also be IP addresses.
    PROTOCOL_CHOICES = (
        ('tcptraceroute', 'TCP Traceroute'),
        ('dns', 'DNS Lookup'),
    )
    protocol = models.CharField(max_length=30, choices=PROTOCOL_CHOICES)
    TIMING_CHOICES = (
        ('m', 'monthly'),
        ('w', 'weekly'),
        ('d', 'daily'),
        ('h', 'hourly'),
    )
    frequency = models.CharField(max_length = 1, choices=TIMING_CHOICES)

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.from_sites, self.to_domains, self.protocol)
