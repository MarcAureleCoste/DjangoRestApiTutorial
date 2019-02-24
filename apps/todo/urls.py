from rest_framework.routers import DefaultRouter
from .views import TodoViewset


TODO_ROUTER = DefaultRouter()
TODO_ROUTER.register(r'^', TodoViewset)
