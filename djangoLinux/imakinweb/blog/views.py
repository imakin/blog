from django.shortcuts import render

from django.utils import timezone
from .models import Post

# Create your views here.
def posts(request):
	postpost = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#~ postpost = Post.objects.order_by('published_date')
	return render(request, 'posts.html', {'postpost':postpost})
