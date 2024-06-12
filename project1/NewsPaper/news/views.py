# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Posts
from .filters import PostsFilter
from django.urls import reverse_lazy
from .forms import PostsForm


class PostsList(ListView):
    model = Posts
    ordering = '-name_post'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostsFilter(self.request.GET, queryset)
        return self.filterset.qs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Posts
    template_name = 'post.html'
    context_object_name = 'post'

class PostsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_posts',)
    raise_exception = True
    form_class = PostsForm
    model = Posts
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post= form.save(commit=False)
        post.item='news'
        return super().form_valid(form)

class PostsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_posts',)
    raise_exception = True
    form_class = PostsForm
    model = Posts
    template_name = 'post_edit.html'

class PostsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_posts',)
    raise_exception = True
    model = Posts
    template_name = 'posts_delete.html'
    success_url = reverse_lazy('post_list')

class PostsSearch(ListView):
    raise_exception = True
    model = Posts
    template_name = 'posts_search.html'
    context_object_name = 'posts'



    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostsFilter(self.request.GET, queryset)
        return self.filterset.qs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_article',)
    raise_exception = True
    form_class = PostsForm
    model = Posts
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post= form.save(commit=False)
        post.item='article'
        return super().form_valid(form)

class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_article',)
    raise_exception = True
    form_class = PostsForm
    model = Posts
    template_name = 'article_edit.html'

class ArticleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_article',)
    raise_exception = True
    model = Posts
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

class ArticleList(ListView):
    model = Posts
    ordering = '-name_post'
    template_name = 'article.html'
    context_object_name = 'article'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostsFilter(self.request.GET, queryset)
        return self.filterset.qs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context