from customer.entity.customer import Customer
from customer.repository.customer_repository import CustomerRepository


class CustomerRepositoryImpl(CustomerRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    # 여기까지 싱글톤 패턴


    def create(self, nickname):
        # entity의 nickname을 받음 = 필요로함
        ## input으로 이름 지정 (나중에 여유 있으면 추가 가능) ##

        customer = Customer(nickname=nickname)
        # customer라는 객체 생성: 어떤 nickname을 가진 Customer를 생성함
        customer.save()
        # 데이터베이스에 정보 저장

        return customer # 생성한 customer 리턴

    def findById(self, id):
        return Customer.objects.get(id=id)
    # entity의 id 값을 입력으로 받아, 데이터베이스에서 해당 id와 일치하는 Customer 객체를 가져옴
    # Customer.objects.get() : "Django ORM에서 제공하는 데이터베이스 조회 메서드"




    