from forms.models import Host, Visitor, Assistant
from django.contrib import admin



# class HostAdmin(admin.ModelAdmin):
# 	fields = ['officePhone', 'officeNumber', 'mitId']

admin.site.register(Host, HostAdmin)


# class VisitorAdmin(admin.ModelAdmin):
# 	field = ['dietary','videoRecording', 'cellPhone', 'officePhone', 'state', 'zipcode', 'country']

admin.site.register(Visitor, VisitorAdmin)

# class AssistantAdmin(admin.ModelAdmin):
# 	field = ['officePhone','officeNumber']

admin.site.register(Assistant, AssistantAdmin)
