
from django.urls import path
from .views import detaillist,adminlist

urlpatterns = [
    path('', adminlist.as_view()),
    path('<int:pk>/',detaillist.as_view())  
]
