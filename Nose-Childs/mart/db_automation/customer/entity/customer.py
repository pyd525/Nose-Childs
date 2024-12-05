from django.db import models

# Customer (고객) 클래스 정의
class Customer(models.Model):

    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, unique=True)
    # 데이터베이스 Column은 id와 nickname이 됨. -> 디스코드 단톡방 DB 그림 참고
    # id는 primary_key (기본키)라서 일단 모든 테이블에 있다고 이해하기
    # .AutoField(): customer가 'Kim'이라고 입력이 되면, 자동으로 1이 되고 이후 'Lee'가 입력이 되면 자동으로 2가 되는 것. 자동으로 숫자 증가
    # .CharField(max_length=50, unique=True): 'Char'이 문자라는 뜻. max_length는 문자 최대 길이, unique=True는 해당 값 (nickname)의 값이 데이터베이스 테이블에서 유일해야 한다는 뜻.

    def __str__(self):
        return f"id: {self.id}, nickname: {self.nickname}"

    def getId(self):
        return self.id
    # getId: 말그대로 id를 겟함 Getter

    def getNickname(self):
        return self.nickname
    # getNickname: 말그대로 Nickname를 겟함 Getter.

    class Meta:
        db_table = 'customer'
    # Meta는 테이블 명을 지정함, 따라서 Customer테이블의 이름은 customer가 됨.
