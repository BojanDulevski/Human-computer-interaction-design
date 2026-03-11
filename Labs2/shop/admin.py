from django.contrib import admin
from .models import Category, Company, Supplement


class SupplementAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()


admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Supplement, SupplementAdmin)