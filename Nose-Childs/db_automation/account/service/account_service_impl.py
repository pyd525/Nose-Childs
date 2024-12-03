from account.repository.account_repository_impl import AccountRepositoryImpl
from account.service.account_service import AccountService


class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createName(self):
        return self.__accountRepository.createName()
    # .createName을 통해서 self.__accountRepository한테 name을 만들고 DB에 저장하라고 시킴ㅇㅇ

    def findAccount(self, requsetAccountId):
        # requestAccountId는 어디서 나왔지 : controller에서 옴
        return self.__accountRepository.findById(requsetAccountId)
        # account_controller에서 받은 requestAccountId로 DB에서 찾으라고 시킴

## 질문 ##
# account_service에서  cls.__instance.__accountRepository = accountRepositoryImpl.getInstance()를 통해
# AccountRepositoryImpl에 있는 매소드(?)를 사용할 수 있게 됨 -> 정확히 말하면 사용은 하는데 여기서 쓰는게 아니라 하라고 시키는 것
# 혹시 상속을 받으면 dice 디렉토리의 repositoryimpl를 account 디렉토리의 service에서 사용이 가능한가?
