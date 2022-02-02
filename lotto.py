import random
# random
# random.sample(랜덤범위, 개수)

# 1.사용자에게 로또를 몇 개 살 건지 숫자 입력
# 2.1부터 45까지 숫자 중 6개를 랜덤으로 뽑기
# 3.사용자에게 입력받은 개수만큼 #2(1부터 45까지 중 6개의 랜덤한 숫자) 를 뽑기
# 4.오름차순으로 정렬해서 출력하기

question = int(input("몇개의 로또를 구매하실건가요? : "))
for i in range(question):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)

print("로또 종료")