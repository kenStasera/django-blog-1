from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView,DetailView,DeleteView
from posts.models import BlogPost
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'
    #filtre sur le query set ....
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published = True)

@method_decorator(login_required, name ='dispatch')
class BlogPostCreate(CreateView):

    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ['title','content']

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_update.html"
    fields = ['title','content','published']

class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "posts/blogpost_detail.html"
    context_object_name = 'post'
# Create your views here.


class BlogPostDelete(DeleteView):
    model = BlogPost
    
    success_url = reverse_lazy('posts:home')