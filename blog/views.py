from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views_counter += 1
        obj.save(update_fields=['views_counter'])
        return obj


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=(self.kwargs.get('pk'),))


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')





