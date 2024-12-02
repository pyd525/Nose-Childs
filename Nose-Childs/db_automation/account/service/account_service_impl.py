from db_automation.account.repository.account_repository_impl import AccountRepositoryImpl
from db_automation.account.service.account_service import AccountService


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

    def create(self):
        pass

    def findAccount(self, requsetAccountId):
        return self.__accountRepository.findById(requsetAccountId)