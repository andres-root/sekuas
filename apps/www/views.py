from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.www.forms import newPostForm
from apps.www.models import News 

def add_post_view(request):
	if request.method == "POST":
		form = newPostForm(request.POST)
		info = "Inicializando"
		if form.is_valid():
			title = form.cleaned_data['title']	
			content = form.cleaned_data['content']	
			p = News()
			p.title = title
			p.content = content
			p.visible = True
			p.save()
			info = "Se guardo"
		else:
			info = "Datos incorrectos"
		form = newPostForm()
		ctx = {'form':form, 'info':info}
		return render_to_response('manager/wall.html',ctx,context_instance=RequestContext(request))
	else:
		form = newPostForm()
		ctx = {'form':form} 
		return render_to_response('manager/wall.html',ctx,context_instance=RequestContext(request))
