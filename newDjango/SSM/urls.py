
from django.urls import path
from . import views

#localHost: 8000/SSM
#localHost: 8000/SSM/order
urlpatterns = [
    path('', views.all_SSM, name='all_SSM'), 
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    # path('order/', views.order, name='order'),
]