from django.http import HttpResponse
from django.template.response import TemplateResponse 
import models
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# 
def posts( request ):
	#posts = models.Post.objects.filter( parent = None ) 
	posts = models.Post.get_recursive(None) 
	return TemplateResponse(request, '_post.html', {'posts': posts})
	'''
	return TemplateResponse(
		request, '_post.html', {'posts': [
			{'title':'foo','children':[
				{'title':'bar','children':[]}
		] } ] }
	)
	'''

