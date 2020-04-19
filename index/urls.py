from django.urls import path, re_path
from index import views


app_name="blog"

urlpatterns = [
    path('index/', views.index, name="index"),
    re_path('detail/(?P<art_id>[0-9]+)', views.article_content, name="detail"),
    re_path('edit/(?P<art_id>[0-9]+)',views.article_edit,name="edit"),
    path('edit_action/',views.edit_action,name="edit_action"),
    re_path('mydelete/(?P<art_id>[0-9]+)',views.mydelete, name="mydelete")


]