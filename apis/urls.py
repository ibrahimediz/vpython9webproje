from django.urls import path
# from .views import ListToDo,DetailToDo


# urlpatterns = [
#     path('',ListToDo.as_view()),
#     path('<int:pk>/',DetailToDo.as_view())
# ]

from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('',TodoViewSet,base_name='todos')
urlpatterns=router.urls