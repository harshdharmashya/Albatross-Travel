from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
path('admin/', admin.site.urls),
path('',views.indexpage,name='indexpage'),
path('indexpage',views.indexpage,name='indexpage'),
path('login',views.login,name='login'),
path('signup',views.signup,name='signup'),
path('logout',views.logout,name='logout'),
path('profile',views.profile,name='profile'),
path('edit',views.edit,name='edit'),

# blog page
path('blog',views.blog,name='blog'),
path('blogdesti',views.blogdesti,name='blogdesti'),
path('readmore/<int:myid>',views.readmore,name='readmore'),
path('search',views.search,name='search'),



path('explore',views.explore,name='explore'),

path('destinationtour',views.destinationtour,name='destinationtour'),
path('about',views.about,name='about'),
path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_done"),

path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), 
     name="password_reset_confirm"),

path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
        name="password_reset_complete"),

]
