# 변수명은 알파벳으로 시작하고, 대소문자를 구분하며, 예약어를 사용할 수 없다.
# 중간에 띄워쓰기 불가능
# 변수명은 누구든지 그 기능이다 저장된 데이터를 쉽게 알 수 있도록 하는 게 관례
# 예약어(Reserved Word) = keyword : print(X) print1(O)
# printNumber(O) : 카멜 방식, 단어를 읽기 쉽도록 두 번째 단어부터
# 첫 글자를 대문자로 표기하는 방식 -> printNumberCaption
# print_number(O) : 언더스코어 방식, 단어마다 중간 언더스코어(_)를 넣는다.
# print_number_caption
# 예약어를 출력
# 식별자(Identifiers) : 변수, 클래스, 모듈, 함수, 
import keyword
print(keyword.kwlist)