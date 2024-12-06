from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fruitMart.controller.fruitMart_controller import FruitMartController

router = DefaultRouter()
router.register(r"fruitMart", FruitMartController, basename='FruitMart')


urlpatterns = [
    path('', include(router.urls)),
    path('request-Stock-Fruit', # Controller에 def requestCreateCustomer(self, request): 있었음.
         FruitMartController.as_view({ 'get': 'requestStockFruit' }),
         name='과일 재고 등록'),

    path('request-Every-Fruit',
         FruitMartController.as_view({ 'get': 'requestEveryFruit' }),
         name='Id로 과일 재고 찾기'),

]