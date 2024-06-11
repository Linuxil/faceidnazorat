from django.urls import path
from .views import HomeView,LoginView,LogoutView, EmployeeDetailView,AddEmployeeView,delete_employee,mobile,capture_view,kelish_ketish,capture_view_ketish,nazorat_mobile,nazorat_jadvali_date,EditProfilView,AdminProfilView

urlpatterns = [
    path('',HomeView.as_view(), name="home"),
    # path('upload/',upload_image, name="upload_image"),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(), name="logout"),
    path('admin_settings/<int:pk>/', AdminProfilView.as_view(), name='admin_settings'),

    # path('admin_settings/',AdminSettingsView.as_view(),name='admin_settings'),
    path('employee_detail/<int:pk>',EmployeeDetailView.as_view(),name='employee_detail'),
    path('delete_employee/<int:pk>',delete_employee,name='delete_employee'),
    path('add_employee/',AddEmployeeView.as_view(),name='add_employee'),
    # For mobile users
    path('mobile/',mobile,name='mobile'),
    path('kelish_ketish/',kelish_ketish,name='kelish_ketish'),
    path('capture/', capture_view, name='capture_view'),
    path('capture_ketish/', capture_view_ketish, name='capture_view_ketish'),
    path('nazorat_mobile/', nazorat_mobile, name='nazorat_mobile'),
    path('nazorat_jadvali_date/<str:i>/', nazorat_jadvali_date, name='nazorat_jadvali_date'),
     path('profil_setting/<int:pk>/', EditProfilView.as_view(), name='profil_setting'),
]