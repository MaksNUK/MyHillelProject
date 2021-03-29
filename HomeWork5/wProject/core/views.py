from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import ListView
from core.models import Post
from django.http.response import Http404


class IndexView(ListView):
    template_name = "index.html"
    model = Post


class CreatePostView(CreateView):
    template_name = "add_post.html"
    model = Post
    fields = '__all__'
    success_url = '/'


class UpdatePostView(UpdateView):
    template_name = "add_post.html"
    model = Post
    fields = '__all__'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.id != Post.objects.get(id=self.kwargs['pk']).author.id:
            raise Http404()
        return super(UpdatePostView, self).dispatch(request, *args, **kwargs)


class DeletePost(DeleteView):
    template_name = "yes_no.html"
    model = Post
    success_url = '/'


class TagFilterView(ListView):
    template_name = "index.html"
    model = Post

    def get_queryset(self):
        return self.model.objects.filter(tags__id=self.kwargs['pk'])


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    slug_field = 'title'
    slug_url_kwarg = 'title'
