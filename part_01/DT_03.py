#리스트 데이터 타입

students = ["egoing","sunk","star"]
grades = [2, 1, 4]

print(students[1]) #원소는 0부터 시작

print("students의 원소 갯수는?",len(students))

print("students의 가장 작은 값은?",min(grades))
print("students의 가장 큰 값은?",max(grades))

# 통계
import statistics

print("grades의 평균값은?",statistics.mean(grades))

import random

print("students의 원소를 랜덤으로 뽑아보세요.",random.choice(students))