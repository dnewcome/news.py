from django.db import models 
from django.contrib import admin

class User( models.Model ):
	username = models.CharField( max_length = 70 )
	password = models.CharField( max_length = 70 )
	def __unicode__( self ):
		return self.username

class Post( models.Model ): 
	title = models.CharField( max_length = 1000 )
	url = models.CharField( max_length = 1000 )
	body = models.CharField( max_length = 1000 )
	create_dt = models.DateTimeField()
	created_by = models.ForeignKey( User )
	parent = models.ForeignKey( 'self', null=True, blank=True )
	
	def __unicode__( self ):
		return self.title

	@classmethod
	def get_recursive(cls, par=None):
		posts = Post.objects.filter(parent=par) 
		for p in posts:
			p.children = []
			p.children.append(cls.get_recursive(p))

		print posts
		return posts
		

class Vote( models.Model ): 
	user = models.ForeignKey( User )
	post = models.ForeignKey( Post )

	def __unicode__( self ):
		return self.user
	
admin.site.register( Post )
admin.site.register( User )
admin.site.register( Vote )
