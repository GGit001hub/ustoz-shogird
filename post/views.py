from pprint import pprint
from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    ListView,DetailView,
    CreateView,UpdateView,
    DeleteView,TemplateView
) 
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post, Comment,CustomUser
from .forms import CommentForm
# Create your views here.




def detail_view(request,slug, id=id):
    post = get_object_or_404(Post,slug=slug)
    author = get_object_or_404(CustomUser,id=2)
    comments = post.comments.filter(status=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'post':post,
        'comments':comments,
        'new_comment':[new_comment,author],
        'comment_form':comment_form
    }

    return render(request,'post_detail.html',context)




class HomeView(TemplateView):
    model = Post
    template_name = 'home.html'

def list_view(request):
    posts = Post.objects.filter(status = True)
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'posts':posts, 'page':page})


class PostCreateView(UserPassesTestMixin,CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ['drift','name','age','address','technology','jobs','price','application_time','phone','photo','title',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_active



class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['drift','name','age','address','technology','jobs','price','application_time','phone','photo','title',]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user



class PostDeletView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


### SHu yerdan pasti funksiya orqali yasalgan View lar uchun 👇
### SHu yerdan pasti funksiya orqali yasalgan View lar uchun  👇
### SHu yerdan pasti funksiya orqali yasalgan View lar uchun   👇


def list_ustoz_view(request):
    ustoz = Post.objects.filter(drift='ustoz',status=True)
    paginator = Paginator(ustoz,3)
    page = request.GET.get('page')
    try:
        ustoz = paginator.page(page)
    except PageNotAnInteger:
        ustoz = paginator.page(1)
    except EmptyPage:
        ustoz = paginator.page(paginator.num_pages)

    return render(request,'ajratish/ustoz.html',{'ustoz':ustoz, 'page':page})




def list_shogird_view(request):
    """Faqat shogirdlarni qaytaradi !!!"""
    shogird = Post.objects.filter(drift='shogird',status=True)
    paginator = Paginator(shogird,3)
    page = request.GET.get('page')
    try:
        shogird = paginator.page(page)
    except PageNotAnInteger:
        shogird = paginator.page(1)
    except EmptyPage:
        shogird = paginator.page(paginator.num_pages)

    return render(request,'ajratish/shogird.html',{'shogird':shogird, 'page':page})


def list_sherig_view(request):
    sherig = Post.objects.filter(drift='sherig',status=True)
    paginator = Paginator(sherig,3)
    page = request.GET.get('page')
    try:
        sherig = paginator.page(page)
    except PageNotAnInteger:
        sherig = paginator.page(1)
    except EmptyPage:
        sherig = paginator.page(paginator.num_pages)

    return render(request,'ajratish/sherig.html',{'sherig':sherig, 'page':page})


def list_hodim_view(request):
    hodim = Post.objects.filter(drift='hodim',status=True)
    paginator = Paginator(hodim,3)
    page = request.GET.get('page')
    try:
        hodim = paginator.page(page)
    except PageNotAnInteger:
        hodim = paginator.page(1)
    except EmptyPage:
        hodim = paginator.page(paginator.num_pages)

    return render(request,'ajratish/hodim.html',{'hodim':hodim, 'page':page})



def list_ishchi_view(request):
    ishchi = Post.objects.filter(drift='ish_joyi',status=True)
    paginator = Paginator(ishchi,3)
    page = request.GET.get('page')
    try:
        ishchi = paginator.page(page)
    except PageNotAnInteger:
        ishchi = paginator.page(1)
    except EmptyPage:
        ishchi = paginator.page(paginator.num_pages)

    return render(request,'ajratish/ishchi.html',{'ishchi':ishchi, 'page':page})





