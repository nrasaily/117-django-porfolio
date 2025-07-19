from django.urls import path
from portfolio import views


urlpatterns = [
  path('', views.about_me_view, name='about_me'),

  path('experience/', views.experience, name='experience'),

  path('contact/', views.contact_view, name='contact'),
]