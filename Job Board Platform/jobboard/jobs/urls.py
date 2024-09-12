from django.urls import path
from . import views  # Import views from the current app (jobs)

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('post/', views.post_job, name='post_job'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
]
