import time
import csv
import random
import winsound

name = input("What is your name?")

print("Hi, "+name, "Time to play hangman game!")

print()

time.sleep(1)

print("Start Loading...")

print()

time.sleep(0.5)

# csv 단어 리스트
words =[] 

# csv 파일 로드
with open("C:/Oct_week4/part_02/word_list.csv", "r") as f:
    reader = csv.reader(f)

    #header skip
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

print()

# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ""

# 기회
turns = 10

#while loop

#찬스 카운트가 남아 있을 경우
while turns > 0:
    #실패 횟수(단어 매칭 수)
    failed = 0

    #정답 단어 반복
    for char in word:
        #정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            #추측 단어 출력
            print(char, end=" ")
        else:
            #틀린 경우 대시로 처리
            print("_", end=" ")
            failed +=1
#단어 추측이 성공 한 경우
    if failed ==0:
        print()
        print()
        #성공 사운드
        winsound.PlaySound("C:/Oct_week4/part_02/sound/good.wav", winsound.SND_FILENAME)
        print("Congratulations!")
        # while 구문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print("Hint : {}".format(q[1].strip()))
    guess = input("Guess a character.")

    # 단어 더하기
    guesses += guess
    
    # 정답 단어에 추측한 문자가 포함되어 있지 않은 경우
    if guess not in word:
        turns -=1
        #오류 메시지
        print("Wrong!")
        print("You have", turns, "more guesses!")
        
        #실패 메시지
        if turns == 0:
            #실패 사운드
            winsound.PlaySound("C:/Oct_week4/part_02/sound/bad.wav", winsound.SND_FILENAME)
            print("game over")