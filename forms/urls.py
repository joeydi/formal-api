from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from forms import views

urlpatterns = [
    path('forms/', views.FormList.as_view()),
    path('forms/<int:pk>/', views.FormDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
