from django.contrib.auth import views
from django.urls import path
from .views import TeacherUploadView, TeacherListView,TeacherDetailView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('importteacher/', TeacherUploadView.as_view(), name='importteacher'),
    path('teachers/', TeacherListView.as_view(), name='get_teacher_list'),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='get_teacher_detail')

]
