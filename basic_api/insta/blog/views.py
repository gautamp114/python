from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404

from .models import Post,Comment
from django.http import HttpResponseRedirect
from .forms import PostForm, CommentForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User


@login_required(login_url='login_page')
def home_view(request):
	comment_form = CommentForm()
	user_posts = Post.objects.all()

	context = {
		'user_posts':user_posts,
		'comment_form':comment_form
	}
	template = 'posts/home.html'
	return render(request, template, context)



@login_required(login_url='login_page')
def delete_post(request,id):
	post = Post.objects.filter(id = id)
	post.delete()
	return redirect('home')



@login_required(login_url='login_page')
def add_comment_to_post(request,id):
	comment_form = CommentForm()
	comment_user = request.user

	post = get_object_or_404(Post,id=id)

	if request.method == 'POST':
		comment_form = CommentForm(request.POST)


		if comment_form.is_valid():
			comment_form.save(commit = False)

			text = comment_form.cleaned_data['text']

			c_form = Comment()
			c_form.text = text
			c_form.post = post
			c_form.author = comment_user
			c_form.save()
			return redirect('home')

	context = {
		'comment_form': comment_form,
		}

	template = 'posts/home.html'
	return render(request, template, context)


@login_required(login_url='login_page')
def edit_comment(request,id):
	print('edit_comment')

	comment_user = request.user
	# post = get_object_or_404(Post,id=id)
	comment = get_object_or_404(Comment,id=id)
	update_comment = CommentForm(request.POST, instance=comment)

	if update_comment.is_valid():
		update_comment.save()

		text = update_comment.cleaned_data['text']

		updateForm = CommentForm()
		updateForm.text = text
		updateForm.post = post
		updateForm.author = comment_user
		updateForm.save()
		return redirect('home')

	context = {
		'update_comment':update_comment
	}

	template = 'posts/comments.html'
	return render(request,template,context)


@login_required(login_url='login_page')
def profile_view(request):
	form = PostForm()
	c_form = CommentForm()
	if request.method == 'POST':

		form = PostForm(request.POST,request.FILES)

		logged_in_user = request.user

		if form.is_valid():
			form.save(commit = False)
			caption = form.cleaned_data['caption']
			image = form.cleaned_data['image']


			post_text = Post()
			post_text.user = logged_in_user
			post_text.caption = caption
			post_text.image = image
			post_text.save()

			return redirect('profile')
	user_posts = Post.objects.filter(user = request.user)
	context = {'user_posts':user_posts, 'form':form, 'c_form':c_form}
	template = 'posts/profile.html'
	return render(request, template, context)




@login_required(login_url='login_page')
def userprofile_view(request,id):
	users = User.objects.filter(id = id)
	user_posts = Post.objects.filter(user = id)
	context = {'users':users, 'user_posts':user_posts}
	template = 'posts/userprofile.html'
	return render(request,template,context)



@login_required(login_url='login_page')
def delete_comment(request,id):
	comment = Comment.objects.filter(id = id)
	comment.delete()
	return redirect('home')