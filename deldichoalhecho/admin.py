from django.contrib import admin
from .models import Promise, Fulfillment, InformationSource, Category
from popolo.models import Person

# Register your models here.
class PromiseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Promise, PromiseAdmin)

class FulfillmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fulfillment, FulfillmentAdmin)

class InformationSourceAdmin(admin.ModelAdmin):
    pass
admin.site.register(InformationSource, InformationSourceAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Person, PersonAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
