from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ( ListView , DetailView, CreateView )
from django.views.generic.edit import UpdateView , DeleteView
from .models import Post


# from django.core.mail import  send_mail

# def sendemails(request) : 
#     print('wewrwer')
#     send_mail('subject', 'message', 'hackathon28aug.gmail.com', ['shrirohitvishwakarma80@gmail.com'])
#     return redirect('/')
   
    

def home (request) :
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blogg/home.html' , context)

class PostListView(ListView):
    model = Post
    template_name = 'blogg/home.html'
    context_object_name = 'pkpost'
    ordering  = ['-date_posted']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'blogg/user_posts.html'
    context_object_name = 'posts'
  
    paginate_by = 3 

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return  Post.objects.filter(author=user).order_by('-date_posted')
       
    


class PostDetailView(DetailView):
    model = Post
   
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'
    
    def test_fuc(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields =['title','content']
    def form_valid(self, form ):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView( LoginRequiredMixin , UpdateView):
    model = Post
    fields =['title','content']
    def form_valid(self, form ):
        
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_fuc(self):
        post = self.get_object()
        if self.request.user == post.author:
         
            return True
        return False

  
def about(request) : 
    return render(request,'blogg/about.html')    