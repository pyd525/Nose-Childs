from customer.repository.customer_repository_impl import CustomerRepositoryImpl
from customer.service.customer_service import CustomerService


class CustomerServiceImpl(CustomerService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__customerRepository = CustomerRepositoryImpl.getInstance()
            # self.__customerRepository를 하면 CustomerRepositoryImpl의 기능들을 쓸 수 있음

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    # 여기까지 싱글톤 패턴


    def createCustomer(self, nickname):
        self.__customerRepository.create(nickname)
    # 말그대로 create Customer함.
    # nickname을 받아서 -> customer_controller의 'John'을 기억하기
    # CustomerRepositoryImpl에 가서 nickname(='John')이란 customer를 create() 생성 하고 와라 이런뜻임.
    # 이 코드로 객체 (customer 'John')가 생성되고 데이터베이스에 id는 1이겠고, nickname 'John'이라고 저장이 되는 것임.



    # findId 혹은 FindNikcname 같은 코드를 더 추가해야 할 수도 있음. 왜냐하면 데이터베이스는 검색해서 출력하는게 중요함.
    # 선생님 Django에 Player, Dice, Game 코드 참고하기  *흐름 이해가 중요*