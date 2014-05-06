from django.db import models

class PromiseSummary(object):
    def __init__(self, accomplished=None,\
                 in_progress=None,\
                 no_progress=None):
        self.accomplished = accomplished
        self.in_progress = in_progress
        self.no_progress = no_progress

class PromiseQuerySet(models.query.QuerySet):
    def summary(self):
        summary = PromiseSummary()
        summary.no_progress = self.filter(fulfillment__percentage__exact=0).count()
        summary.accomplished = self.filter(fulfillment__percentage__exact=100).count()
        summary.in_progress = self.filter(fulfillment__percentage__range=(1,99)).count()
        return summary

class PromiseManager(models.Manager):
    def get_queryset(self):
        return PromiseQuerySet(self.model, using=self._db)
