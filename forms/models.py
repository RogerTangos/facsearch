from django.db import models

# Create your models here.

class Host(models.Model):
	lastLogin = models.DateTimeField('last login', null=True, blank=True)

	fName = models.CharField(max_length=100, null=True, blank=True)
	lName = models.CharField(max_length=100, null=True, blank=True)	

	officePhone = models.CharField(max_length=20, null=True, blank=True)
	officeNumber = models.CharField(max_length=7, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	mitId = models.CharField(max_length=100, null=True, blank=True)


	def __unicode__(self):
		return '%s, %s | %i | %s' %(self.fName, self.lName, self.pk, self.email)



class Visitor(models.Model):
	lastLogin = models.DateTimeField('last login', null=True, blank=True)
	hosts = models.ManyToManyField(Host)


	fName = models.CharField(max_length=100, null=True, blank=True)
	lName = models.CharField(max_length=100, null=True, blank=True)	

	email = models.CharField(max_length=100, null=True, blank=True)
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
		return '%s, %s | %i | %s' %(self.fName, self.lName, self.pk, self.email)



class Assistant(models.Model):
	# denormalized for convenience
	facMembers = models.ManyToManyField(Host)

	# may support assistant login later
	lastLogin = models.DateTimeField('last login', null=True, blank=True)

	fName = models.CharField(max_length=100, null=True, blank=True)
	lName = models.CharField(max_length=100, null=True, blank=True)	

	officePhone = models.CharField(max_length=20, null=True, blank=True)
	officeNumber = models.CharField(max_length=7, null=True, blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)
	mitId = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return '%s, %s | %i | %s' %(self.fName, self.lName, self.pk, self.email)
