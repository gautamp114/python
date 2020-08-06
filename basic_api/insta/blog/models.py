from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, related_name = 'post')
	caption = models.TextField(blank=True, null= True)
	slug = models.SlugField(unique= True, null= True, blank=True)
	image = models.ImageField(upload_to='user/images/', null = True, blank = True)
	created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_on = models.DateTimeField(auto_now= True, auto_now_add=False)

	def __str__(self):
		return f'{self.user.username} Post'

	class Meta:
		ordering = ['-created_on',]


class Comment(models.Model):
	text = models.TextField(max_length=255)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	active = models.BooleanField(default = True)
	created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.text
