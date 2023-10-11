from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, TextEntryForm, TextEntry
#import deepl
import openai
import os


#load_dotenv()

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def text_entry_view(request):
    if request.method == 'POST':
        form = TextEntryForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_to_translate']
            text = translate_with_ai(text)
    else:
        form = TextEntryForm()
        text = ''

    return render(request, 'misc/projects.html' ,{'form': form, 'text': text})

def translate_with_ai(text):
    #return ''
    #openai.api_key = '1234'
    #return os.getenv("OPENAI_KEY")
    openai.api_key = os.getenv("OPENAI_KEY")
    return ('this is the key: ', openai.api_key)
  

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=
    "translate into English: \n\n\n"
    + text,
    temperature=0,
    max_tokens=1338,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
    completion = response.choices[0].text

    #return completion.strip()
