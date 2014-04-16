from django.contrib import admin
from .models import Promise, Fulfillment, InformationSource, Category
from popolo.models import Person

# Register your models here.

class FulfillmentInlineAdmin(admin.StackedInline):
	model = Fulfillment

class InformationSourceInline(admin.TabularInline):
    model = InformationSource

class PromiseAdmin(admin.ModelAdmin):
    inlines = (FulfillmentInlineAdmin, InformationSourceInline)

admin.site.register(Promise, PromiseAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Person, PersonAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
