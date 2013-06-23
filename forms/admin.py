from forms.models import Host, Visitor, Assistant
from django.contrib import admin


class HostAdmin(admin.ModelAdmin):
	fields = ['fName', 'lName', 'officePhone', 'officeNumber', 'email']

	def __unicode__(self):
		return self.lName

admin.site.register(Host, HostAdmin)

class VisitorAdmin(admin.ModelAdmin):
	field = ['fName', 'lName', 'dietary','videoRecording', 'cellPhone', 'officePhone', 'email', 'state', 'zipcode', 'country']

admin.site.register(Visitor, VisitorAdmin)

class AssistantAdmin(admin.ModelAdmin):
	field = ['fName', 'lName', 'officePhone','officeNumber', 'email']

admin.site.register(Assistant, AssistantAdmin)
