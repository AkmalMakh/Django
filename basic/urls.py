from django.urls import path
from basic import views

# Template Tagging
app_name = 'basic'

urlpatterns = [
    path('relative/', views.relative, name="relative"),
    path('other/', views.other, name="other"),
]
