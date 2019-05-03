from django.urls import include, path
from .views import index, student_details 

urlpatterns = [
    path('', index, name='index'),
    path('<int:_id>/', student_details, name='student_details')
]