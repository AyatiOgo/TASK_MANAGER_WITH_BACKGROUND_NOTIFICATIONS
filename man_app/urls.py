from django.urls import path
from .views import *

urlpatterns = [
    path('V1/task/list/', TaskView.as_view(), name='list'),
    path('V1/task/upload/', TaskView.as_view(), name='upload'),
    path('V1/task/<int:pk>/', TaskDetailView.as_view(), name='view_task'),
    path('V1/task/<int:pk>/update/', TaskDetailView.as_view(), name='update_task'),

]
