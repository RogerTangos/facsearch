from forms.models import Host, Visitor, Assistant
from django.contrib.auth.models import User
from django.contrib import admin



# class HostAdmin(admin.ModelAdmin):
# 	fields = ['officePhone', 'officeNumber', 'mitId']

admin.site.register(Host)


# class VisitorAdmin(admin.ModelAdmin):
# 	field = ['dietary','videoRecording', 'cellPhone', 'officePhone', 'state', 'zipcode', 'country']

admin.site.register(Visitor)

# class AssistantAdmin(admin.ModelAdmin):
# 	field = ['officePhone','officeNumber']

admin.site.register(Assistant)
