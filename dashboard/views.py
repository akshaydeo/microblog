from django.shortcuts import render_to_response
from django.template import RequestContext

from dashboard.models import Post

def dashboard(request):
	#collect all posts	
	posts = Post.objects.all()
	return render_to_response('dashboard.html', {'posts' : posts}, context_instance=RequestContext(request))

def post(request):
	if request.method == "POST":
		if 'post' in request.POST:
			content = request.POST['post']
			print content
			if content != '':
				newPost = Post()
				newPost.content = content
				newPost.save()

	posts = Post.objects.all()	
	return render_to_response('dashboard.html', {'posts' : posts}, context_instance=RequestContext(request))	

