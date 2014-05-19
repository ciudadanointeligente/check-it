from django.contrib import admin
from .models import TagExtraCss

class TagExtraCssAdmin(admin.ModelAdmin):
    pass

admin.site.register(TagExtraCss, TagExtraCssAdmin)
