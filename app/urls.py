from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarListView,NewCreateView,Cardetail, Updatecarview, Cardeleteview
from acconts.views import register_view, login_view,logout_view

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('cars/', CarListView.as_view(), name = 'cars_list'),
    path('car/<int:pk>/',Cardetail.as_view(), name = 'car_detail'),
    path('car/<int:pk>/update',Updatecarview.as_view(), name = 'car_update'),
    path('car/<int:pk>/delete',Cardeleteview.as_view(), name = 'car_delete'),
    path('newcar/', NewCreateView.as_view(), name = 'newcar_view'),
    path('register/',register_view, name = 'register'),
    path('login/',login_view, name = 'login'),
    path('logout/',logout_view, name = 'logout'),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)