from django.contrib import admin
from .models import InstitutesListing,ApplyInstitute
# Register your models here.


class InstitueAdmin(admin.ModelAdmin):
      list_display = ("title", "slug", "status", "created_on")
      list_filter = ("status", "created_on")
      search_fields = ["title", "content"]
      prepopulated_fields = {"slug": ("title",)}


admin.site.register(InstitutesListing,InstitueAdmin)

@admin.register(ApplyInstitute)
class ApplyInstituteAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'phone', 'email',"city")
    list_filter = ('city','title')
    search_fields = ('name', 'email', 'title')
    