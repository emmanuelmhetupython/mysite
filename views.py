from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .forms import PostForm
from .models import Book
from .models import Post
from .models import Question
from .forms import QuestionForm

# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request,'home.html',{
        'count': count
    })

def signup(request):
    if request.method =='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewUserForm
    return render(request,'registration/signup.html',{ 
        'form': form
    })
@login_required
def secret_page(request):
    return render (request,'secret_page.html')  
@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request,'upload.html',context)
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request,'book_list.html',{
        'books':books
    })
@login_required
def upload_book(request):
    if request.method=='POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'upload_book.html',{
        'form':form

    }
     
    )
@login_required
def create_post(request):
    if request.method=='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Question was created successfully. You will receive answers to your email</h2>")
    else:
        form = PostForm()
    return render(request,'create_post.html',{
        'form':form

    }
     
    )
@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request,'posts_list.html',{
        'post':posts
    })

@login_required
def create_question(request):
    if request.method=='POST':
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request,'create_question.html',{
        'form':form

    }
     
    )
@login_required
def aboutMI(request):
    return render(request,"aboutMI.html")
@login_required
def donate(request):
    return render(request,"donate.html")
@login_required
def Learn_more(request):
    return render(request,"learn_more.html")