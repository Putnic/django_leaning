from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
  path('', views.post_list, name='post_list_url'),
  path('post/<int:pk>/', views.post_detail, name='post_detail_url'),
  path('post/new/', views.post_new, name='post_new_url'),
  path('post/<int:pk>/edit/', views.post_edit, name='post_edit_url'),
  path('drafts/', views.post_draft_list, name='post_draft_list_url'),
  path('post/<pk>/publish/', views.post_publish, name='post_publish_url'),
  path('post/<pk>/remove/', views.post_remove, name='post_remove_url'),
  path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post_url'),
  path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
  path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]