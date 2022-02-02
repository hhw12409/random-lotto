import sys
import random

question = int(sys.stdin.readline())
for i in range(question):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)

print("로또 종료")