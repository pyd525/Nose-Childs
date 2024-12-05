from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.response import Response

from customer.service.customer_service import CustomerService
from customer.service.customer_service_impl import CustomerServiceImpl
                                                # Customer_Service_Impl 필요해서 import함


class CustomerController(viewsets.ViewSet):
    customerService = CustomerServiceImpl.getInstance()
    # CustomerServiceImpl을 가져와서 customerService에 대입

    def requestCreateCustomer(self, request):
    # 특정 요청(request)을 받아 새로운 고객(customer)을 생성하고 응답(Response)을 반환하는 동작을 수행

        requestGetData = request.GET
        # request.GET: 요청된 URL 쿼리 문자열의 데이터를 딕셔너리 형태로 반환함
        # e.g)  클라이언트가 GET /createCustomer?nickname=John 요청 시, request.GET은 {'nickname': 'John'}을 포함
        # createCustomer?nickname=John 이게 무슨뜻인지 모르겠다면 https://www.notion.so/eddi-robot-academy/Django-Based-Dice-Game-with-DDD-153694fe05958050a036db7ee715a33c 참고

        requestNickname = requestGetData.get('nickname')
        # requestGetData.get('nickname'): {'nickname': 'John'}에서 'John'을 추출해서 requestNickname에 저장

        customer = self.customerService.createCustomer(requestNickname)
        # self.customerService = CustomerServiceImpl.getInstance()/ 내부에 있어서 self.
        #  동작 흐름: 1) 전달받은 requestNickname 값을 확인함 = 'John'
        #            2) 새 고객 생성: 데이터베이스에 접근하여 새로운 고객 객체 ('John')를 생성하고 customer에 저장
        #            3) customer가 데이터베이스에 입력되고 return함.


        return Response(customer, status=status.HTTP_200_OK)
        # Response() : 클라이언트에게 HTTP 응답을 보냄
        # status=status.HTTP_200_OK: HTTP 상태 코드 200(요청 성공)을 함께 반환



    # CustomerRepositoryImpl에 있길래 내가 추가함.
    def requestFindCustomer(self, request):
        requestGetData = request.GET
        requestCustomerId = requestGetData.get('id')
        # id(기본키)로 검색해서 customer 정보를 추출

        foundCustomer = self.customerService.findDice(requestCustomerId)
        # 나도 왜 얘는 굳이 foundCustomer로 저장한건지 모름, 알아보고 쓰겠음.

        return Response(model_to_dict(foundCustomer),status=status.HTTP_200_OK)
        # 데이터베이스는 dictionary 형태로 저장함.  model_to_dict()이걸로 저장함



# FindEveryCustomer도 필요한지 고민중임....