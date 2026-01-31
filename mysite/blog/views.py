from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm


# List all blog posts (Task-5)
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


# Show single post using dynamic URL (Task-6)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# Create new post using form (Task-6)
class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, 'blog/post_form.html', {'form': form})
