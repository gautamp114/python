from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
	caption = forms.CharField(widget = forms.Textarea(
		attrs={
		'class':'form-control',
		'style':'width:550px;','height':'10px;',
		'overflow-y': 'scroll;',
		"rows":1, "cols":10}))

	class Meta:
		model = Post
		fields = ['image', 'caption']

class CommentForm(forms.ModelForm):
	text = forms.CharField(widget = forms.Textarea(
		attrs={
		'class':'form-control',
		'style':'width:500px;','height':'10px;',
		'overflow-y': 'scroll;',
		"rows":1, "cols":10}))

	class Meta:
		model = Comment
		fields = ['text']
