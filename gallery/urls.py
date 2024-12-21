from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PhotoListViews.as_view(), name='gallery-list' ),
    path('creat/', views.PhotoCreatViews.as_view(), name= 'gallery-creat'),
    path('delete/<int:pk>/', views.PhotoDeleteViews.as_view(),name='gallary-delete'),
    path('detail/<int:pk>/', views.PhotoDetailViews.as_view(), name='gallery-detail')
]
