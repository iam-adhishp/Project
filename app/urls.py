from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from support.views import bestsellers_list, cs, sampl
from app.views import map_view
# from .views import signup

urlpatterns = [
    path('', views.sample, name='sample'),
    path('home/', views.home, name='home'),
    path('fashion/', views.fashion, name='fashion'),
    path('/login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('signup/', signup, name='signup'),
    path('register/', views.new_register, name='new_register'),
    path('wish/', views.wish, name='wish'),
    path('add/', views.add_item, name='add_item'),
    path('view/', views.view_items, name='view_items'),
    path('cs/', cs, name='cs'),
    path('search/', views.search_view, name='search'),
    path('map/', map_view, name='map'),
    path('try/', sampl, name='try'),
    path('sell/', bestsellers_list, name='sell'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

