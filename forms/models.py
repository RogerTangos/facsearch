from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Host(models.Model):
	user = models.OneToOneField(User)
	lastLogin = models.DateTimeField('last login', null=True, blank=True)

	officePhone = models.CharField(max_length=20, null=True, blank=True)
	officeNumber = models.CharField(max_length=7, null=True, blank=True)
	mitId = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return '%s, %s | %i | %s' %(self.user.last_name, self.user.first_name, self.pk, self.user.email)


class Visitor(models.Model):
	user = models.OneToOneField(User)
	hosts = models.ManyToManyField(Host, null=True, blank=True)
	
	lastLogin = models.DateTimeField('last login', null=True, blank=True)

	address1 = models.CharField(max_length=100, null=True, blank=True)
	address2 = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=50, null=True, blank=True)
	state = models.CharField(max_length=50, null=True, blank=True)
	zipcode = models.CharField(max_length=50, null=True, blank=True)
	country = models.CharField(max_length=50, null=True, blank=True)

	officePhone = models.CharField(max_length=20, null=True, blank=True)
	cellPhone = models.CharField(max_length=20, null=True, blank=True)
	dietary = models.CharField(max_length=300, null=True, blank=True)

	videoRecording = models.BooleanField()

	def __unicode__(self):
		return '%s, %s | %i | %s' %(self.user.last_name, self.user.first_name, self.pk, self.user.email)


class Assistant(models.Model):
	# denormalized for convenience
	user = models.OneToOneField(User)
	facMembers = models.ManyToManyField(Host, null=True, blank=True)

	# may support assistant login later
	lastLogin = models.DateTimeField('last login', null=True, blank=True)

	officePhone = models.CharField(max_length=20, null=True, blank=True)
	officeNumber = models.CharField(max_length=7, null=True, blank=True)
	mitId = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return '%s, %s | %i | %s' %(self.user.last_name, self.user.first_name, self.pk, self.user.email)


class Event(models.Model):
	title = models.CharField(max_length=60)
	location = models.CharField(max_length=60)
	start = models.DateTimeField(null=True, blank=True) #problem
	end = models.DateTimeField(null=True, blank=True) #problem
	phone = models.CharField(max_length=20)

	creator = models.ForeignKey(User, related_name='event_user_creator', blank=True) #problem
	editor = models.ForeignKey(User, related_name='event_user_editor', blank=True, default=creator) #problem
	visitor = models.ForeignKey(Visitor, related_name='event_user_visitor') #problem
	lastEdit = models.DateTimeField(auto_now=True, null=True, blank=False)
	detail = models.CharField(max_length=500, null=True, blank=True)
	# if editor == None:
	# 	editor = creator

	def __unicode__(self):
		return '%s, %s' %(self.title, self.creator.username)