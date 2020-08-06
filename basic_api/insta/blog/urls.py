from django.urls import path

from blog import views


urlpatterns = [
	path('',views.home_view, name='home'),
	path('profile/',views.profile_view, name='profile'),
	path('userprofile_view/<int:id>/',views.userprofile_view, name='userprofile_view'),
	path('add_comment_to_post/<int:id>/',views.add_comment_to_post, name='add_comment'),
	path('delete_post/<int:id>/',views.delete_post, name='delete_post'),
	path('delete_comment/<int:id>/',views.delete_comment, name='delete_comment'),
	path('edit_comment/<int:id>/',views.edit_comment, name='edit_comment'),
]
