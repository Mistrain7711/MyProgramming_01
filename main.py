# 실행 전에 확인할 것!!!!!
# cmd에 venv 설정 되어있는지 꼭 체크하기!!!
# .\.venv\Scripts\activate
# venv 켜져 있으면 이거 치면 실행됨!!!
# python main.py

pidgeon = 9 # 변수 초기화에 타입 표기할 필요가 없음
print(pidgeon) # 세미콜론이 필요가 없음

pidgeon *= 9 # 이건 평소대로 쓰면 됨

if pidgeon > 9 : # :를 달고 들여쓰기를 하여 결과 작성, 나가려면 들여쓰기를 풀면 됨 
    print("Feeding Time")
    pidgeon //= 9 # 결과값이 정수형인 곱셈 or 나눗셈을 원하면 똑같은 기호를 2번 쓰면 됨 (**, //)

pidgeon_song = "Gu" * pidgeon # 문자열을 복사하려면 곱하기를 쓰면 된다
print (pidgeon_song) # 결과 : Gu가 9번 이어서 출력

pidgeon *= 99
pidgeon /= 9
pidgeon = int(pidgeon) # 특정 변수형으로 뭉개는 방법
pidgeon_song = "Gu " * pidgeon
print (pidgeon_song)

help(print) # print 함수에 대해 알려주세요!

def BiggerNum(num1, num2): # 함수 정의하기
    """
    예시 : BiggerNum(1333, 1234)
    결과 : 1333
    """
    # help 함수로 함수에 대한 설명을 띄우고 싶을 때 """를 이용하면 됨

    checkNum = num2 - num1
    if checkNum > 0 :
        return(num2) # 파이썬에서 리턴은 함수에용
    else : # else문은 이렇게 사용하면 된다네요
        return(num1)

print (BiggerNum(1333, 1557), BiggerNum(88484, 1557), BiggerNum(1333, 1333)) # 이런게 가능하다니

help(BiggerNum)

print ("레전드", "오브", "곡괭이", sep='-') # 여러 내용물을 한번에 출력시 sep로 중간 부분 설정 가능

def Normalization(server) :
    return(server - 100000)

def FunctionCaller(fn, arg) : # 함수를 부르는 함수 만들기
    return(fn(arg)) #이런게 가능하다니

reboot = 140000

print (reboot, "에서", reboot-FunctionCaller(Normalization, reboot), "떠나간, 그 발걸음이 너무도 무겁네~", sep=' ')