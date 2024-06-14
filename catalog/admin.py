from django.contrib import admin
from .models import SubSystems, Services, SecurityServers

# Register your models here.
admin.site.register(SubSystems)
admin.site.register(Services)
admin.site.register(SecurityServers)
