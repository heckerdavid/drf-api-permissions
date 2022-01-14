from django.urls import path
from .views import WriteList, WriteDetail

urlpatterns = [
    path('', WriteList.as_view(), name='write_list'),
    path('<int:pk>/', WriteDetail.as_view(), name='write_detail'),
]