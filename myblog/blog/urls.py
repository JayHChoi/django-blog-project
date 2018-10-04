from django.urls import path, include
from .views import *

app_name = 'blog'
urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]
