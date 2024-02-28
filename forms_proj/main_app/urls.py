from django.urls import path
from .views import home_page_view, delete_post, edit_post

urlpatterns=[
   path('', home_page_view, name="home"), 
   path("post/<int:post_id>/",delete_post, name="delete-post"),
   path("post/<int:post_id>/edit/", edit_post, name="edit-post")
   
   
]