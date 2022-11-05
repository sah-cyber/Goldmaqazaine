from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('post/<int:get_id>/', views.partjeweler, name='post'),
    path('category/<slug:category_id>/', views.category, name='category'),
    path('email/', views.contact_email, name='contact_email'),
    path('tag/', views.tag, name='tag_url'),
    path('tags/<slug:tag_slug>/',views.tag_detail, name ='tag_detail')
]