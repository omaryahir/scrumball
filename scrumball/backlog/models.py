from django.db import models

# Create your models here.

class General():
	states = (
			('New','New Item'),
			('Reconsidered','Reconsidered Item'),
			('Removed','Removed Item'),
			('Approved','Approved by the product Owner'),
			('Commited','Commited by the team'),
			('Stopped','Work stopped'),
			('Done','Work finished')
			)

class Module(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

class Backlog(models.Model):
	title = models.CharField(max_length=100)
	state = models.CharField(max_length=20,choices=General.states)
	module = models.ForeignKey(Module)

	def __unicode__(self):
		return self.title