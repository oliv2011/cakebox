from django.shortcuts import render
from api.serializers import Cakeserializer,UserSerializer
from api.models import Cakes,User
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework import authentication,permissions
# Create your views here.


class CakeView(ModelViewSet):
    model=Cakes
    queryset=Cakes.objects.all()
    serializer_class=Cakeserializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        qs=Cakes.objects.all()

        if "layers" in self.request.query_params:
            lyr=self.request.query_params.get("layers")
            qs=qs.filter(layers=lyr)

        if "shape" in self.request.query_params:  
            shp=self.request.query_params.get("shape")
            qs=qs.filter(shape=shp)  
        
        return qs

class UserView(GenericViewSet,CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()
