from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from . import views as user_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name = 'home'),
    path('accounts/register/', user_views.register, name ='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='django_registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', user_views.profile, name = 'profile'),
    path('add_hood/',views.uploadNeighbourhood, name = 'add_hood'),
    path('viewHood/',views.viewHood, name = 'viewHood'),
    path('hood/<int:pk>/',views.hood, name = 'hood'),
    path('add_business/',views.uploadBuisness, name = 'add_business'),
    path('bizna/',views.viewBizna, name = 'view_business'),
    path('viewbizna/<int:pk>/',views.bizna, name = 'bizna'),
    path('post/',views.create_post, name = 'post'),
    path('posts/',views.viewPost, name = 'posts'),
    path('searchbizna/', views.searchBizna, name="search_results"),
    path('searchhood/', views.searchHood, name="search_res"),
    path('join_hood/<id>', views.join_neighbourhood, name='join-hood'),
    path('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
