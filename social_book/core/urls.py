from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('follow', views.follow, name='follow'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('like/', views.post_like, name='post_like'),
]