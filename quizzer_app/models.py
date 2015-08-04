from django.db import models

class School(models.Model):
	name = models.CharField(max_length=128, unique=True)
	address = models.CharField(max_length=256)
	state = models.CharField(max_length=128)
	zip_code = models.CharField(max_length=16)
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name


class Privilege(models.Model):
	title = models.CharField(max_length=128, unique=True)
	description = models.CharField(max_length=256)
	url = models.CharField(max_length=256)
		
	def __unicode__(self):
		return self.title

class Role(models.Model):
	title = models.CharField(max_length=128, unique=True)
	description = models.CharField(max_length=256)
	privileges = models.ManyToManyField(Privilege)

	def __unicode__(self):
		return self.title

class User(models.Model):
	school = models.ForeignKey(School)
	role = models.ForeignKey(Role)
	name = models.CharField(max_length=128) 
	password = models.CharField(max_length=256)
	password_salt = models.CharField(max_length=256)
	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)
	active = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.name

class Quiz(models.Model):
	title = models.CharField(max_length=128, unique=True)
	description = models.CharField(max_length=256)
	max_score = models.IntegerField()
	students = models.ManyToManyField(User)

	def __unicode__(self):
		return self.title

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	text = models.CharField(max_length=512)
	points = models.IntegerField()

	def __unicode__(self):
		return self.text

class AnswerChoice(models.Model):
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=512)
	correct = models.BooleanField(default=False)

	def __unicode__(self):
		return self.text

class StudentSubmission(models.Model):
	student = models.ForeignKey(User)
	quiz = models.ForeignKey(Quiz)
	date_submitted = models.DateField(null=True, blank=True)
	score = models.IntegerField()
	answers = models.ManyToManyField(AnswerChoice)

	def __unicode__(self):
		return self.id
