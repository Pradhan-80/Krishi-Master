from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'main/post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'main/post.html'
