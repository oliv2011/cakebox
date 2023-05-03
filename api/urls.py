from django.urls import path
from api import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter




router=DefaultRouter()
router.register("register",views.UserView,basename="register")
router.register("cakes",views.CakeView,basename="cakes")

urlpatterns = [
    path("token/",ObtainAuthToken.as_view())
    

]+router.urls