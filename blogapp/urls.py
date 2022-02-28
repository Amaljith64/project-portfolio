from django.urls import path

from . import views
app_name = 'blogs'
urlpatterns = [

    path('index', views.index, name='index'),
    # path('check/',views.check,name='check'),
    path('view/<int:post_id>/',views.detail,name='view'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete, name="delete"),
]