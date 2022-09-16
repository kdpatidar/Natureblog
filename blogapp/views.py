from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post,CommentModel

# from django.contrib.auth import logout

# Create your views here.

# @login_required
def home(request):
    return render(request, 'home.html')



# SIGN UP FORM view function 
def sign_up(request):
    if request.method == "POST":
     user_signup = SignUpForm(request.POST)
     if user_signup.is_valid():       
        user_signup.save()
        request.session["success"] = 'account created successfully !!'
        return redirect('login')
    else:
        
        user_signup = SignUpForm 
          
    
    return render(request,'blogapp/register.html',{'form':user_signup})



#user Login

def user_login (request):
    
    if request.method == "POST":
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            
            user = authenticate(username=uname, password=upass)
            
            if user is not None: 
                login(request, user) 
                return HttpResponseRedirect('/')
            
                # return HttpResponse('Invalid username or Password')    
                
            request.session["success"] = 'invalid user name or password !!'
            redirect('login')   
            
            
    form=LoginForm 
   
    message1 = ''
    if "success" in request.session.keys():
        message1 = request.session.get("success")
        del request.session["success"]
    else:
        pass
    return render(request, 'blogapp/login.html', {'form':form,"message1":message1 })

  


# def detail(request):
#     # breakpoint()
#     user = request.user.id
#     # data = User.objects.all()
#     # data = Employee.objects.get(user=user)
#     # print(data)
#     # obj = request.user 
#     # print(obj)
    
#     data = User.objects.filter(id =user)
#     # print(data,"HHHHHHHHHHh")
#     return render(request, 'blogapp/detail.html',{'data':data})

@login_required
def add_blog(request):
    
    if request.method == "POST":
        author = request.user
        title = request.POST.get("title")
        slug = request.POST.get("slug")
        content = request.POST.get("content")
        created_on = request.POST.get("created_on")
        blog_image=request.FILES.get("blog_image")
        
        
        obj=Post(title= title,
                 slug= slug,
                 content= content,
                 created_on=created_on,
                 author=author,
                 blog_image=blog_image
                 
                 )
        
        obj.save()
        return redirect('blogs')
    else:
        return render(request, 'blogapp/addblog.html/')  
    
    
    
# Show All post in Frontend

def show_blog(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/blogs.html', {'posts': posts,})

# Show Single Post Detail in Frontend
@login_required
def post_detail(request, id):
    post = Post.objects.filter(id=id)
    # print(post)
    com = CommentModel.objects.filter(post=id)
    # print(request.POST)
    # com = CommentModel.objects.filter(id=id)
    # print(com)
    if request.method == "POST":
        # print(request.POST)
        comment = request.POST.get("comment")
        
        # print(comment)
        username = request.POST.get('username')
        comment_date = request.POST.get('comment_date')
        post_obj = Post.objects.get(id =id)
        user = User.objects.get(username = request.user)
        data=CommentModel(post =post_obj,comment=comment,username=user )
        data.save()
    # comment_form = CommentForm(data=request.POST)    
    form = CommentForm
    return render(request, 'blogapp/post_detail.html', {'post': post, 'form':form, 'com':com})


# User Logout
def logout_user(request):
    logout(request)
    return redirect('login')
    


        
    
    