from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import PostForm, CommentForm, UserRegisterForm, LoginForm
from .models import Post


# 🏠 Home Page
def home(request):
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)

    latest_posts = Post.objects.filter(is_approved=True).order_by("-created_at")[:5]
    popular_posts = Post.objects.filter(is_approved=True).order_by("-views_count")[:5]
    weekly_posts = Post.objects.filter(is_approved=True, created_at__gte=week_ago).order_by("-views_count")[:5]
    monthly_posts = Post.objects.filter(is_approved=True, created_at__gte=month_ago).order_by("-views_count")[:5]
    recommended_posts = Post.objects.filter(is_approved=True).annotate(
        num_comments=Count("comments")
    ).order_by("-num_comments")[:5]

    context = {
        "latest_posts": latest_posts,
        "popular_posts": popular_posts,
        "weekly_posts": weekly_posts,
        "monthly_posts": monthly_posts,
        "recommended_posts": recommended_posts,
    }
    return render(request, "blog/home.html", context)


# 📄 Post Detail Page + Comments
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_approved=True)

    # faqat GET so‘rovda views ko‘paytirish
    if request.method == "GET":
        post.views_count += 1
        post.save()

    comments = post.comments.all()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                messages.success(request, "Your comment has been added.")
                return redirect("post_detail", pk=post.pk)
        else:
            messages.error(request, "You must be logged in to comment.")
            return redirect("login")
    else:
        form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "comment_form": form}
    )


# ➕ Add New Post
@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "Your post has been submitted and awaits admin approval.")
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "blog/add_post.html", {"form": form})


# 📝 Register
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "blog/register.html", {"form": form})


# 🔑 Login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, "blog/login.html", {"form": form})


# 🚪 Logout
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")
