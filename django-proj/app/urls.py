from django.urls import path 

from . import views 

urlpatterns=[
    path('form/',views.quote_form_view,name='quote-form'),
    path('submit/',views.submit_quote, name='submit_quote'),
    path('quote/', views.get_quotes, name='get_quote'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
 
    
]