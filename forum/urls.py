from django.urls import path
from forum import views

urlpatterns = [
    path('post-creat/', views.PostCreateViews.as_view(), name='post-creat'),
    path('post-list/', views.PostListViews.as_view(), name='post-list'),
    path('post-detail/<int:pk>', views.PostDetailViews.as_view(), name='post-detail'),
    path('post-delite/<int:pk>', views.TaskDeliteView.as_view(), name='post-delite'),
    path('comment/like/<int:pk>/',views.PostLikeToggel.as_view(), name="comment-toggle-like"),
    path('comment/dislike/<int:pk>/', views.PostDislikeToggel.as_view(), name="comment-toggle-dislike"),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post-update'),
    path('close/<int:pk>/', views.PostCloseView.as_view(), name='post-close'),
    path('open/<int:pk>/', views.PostOpenView.as_view(), name='post-open')
]
