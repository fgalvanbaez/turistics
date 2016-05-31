from django.contrib import admin
from web.models import Host


# Register your models here.
class HostAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'date', 'type', 'total')


admin.site.register(Host, HostAdmin)
