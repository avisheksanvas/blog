from django.http import HttpResponse , HttpResponseRedirect , Http404
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post
from django.utils import timezone
from .forms  import PostForm
from django.db.models import Q

def posts_create(request):
	form = PostForm(request.POST or None , request.FILES or None )
	if not request.user.is_authenticated():
		raise Http404 
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		"form" : form
	}
	return render(request,"posts_create.html" , context)

def posts_detail(request,id):
	instance = get_object_or_404(Post,id=id)
	context = { "post" : instance }
	return render(request,"posts_detail.html" , context)

def posts_update(request,id=None):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None , request.FILES or None , instance=instance )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = { 
	"post" : instance ,
	"form" : form ,
	}
	return render(request,"posts_update.html",context)

def posts_delete(request,id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	return redirect("posts_home")

def posts_list(request):
	queryset = Post.objects.filter(draft=False).filter(publish__lte=timezone.now()).order_by("-timestamp")

	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)|
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
			).distinct()

	context = {
		"posts_list" : queryset , 

	}
	return render(request , "posts_list.html" , context )
	#return HttpResponse("<h1>List</h1>")