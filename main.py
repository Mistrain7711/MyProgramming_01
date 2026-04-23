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
    return(fn(arg)) # 이런게 가능하다니

reboot = 140000
normalizationNum = reboot-FunctionCaller(Normalization, reboot)

print (reboot, "에서", normalizationNum, "떠나간, 그 발걸음이 너무도 무겁네~", sep=' ')

# 여기까지가 4월 15일 분량

isThisReal = True # Boolean형 변수
print (isThisReal)

print (reboot > normalizationNum, '140000' == reboot)

def RealCheck(num1, num2) :
    if (num2 > num1 - num2 and num2 > 0) : # && → and, || → or
        return '역시 정상화는 신창섭'
    else :
        return '과징금 크악'

def MultiCheck (num1, num2) :
    if (num2 > num1 - num2 or num2 > 0 and num1 < 0) : # and와 or의 연산순서 체크
        return '드디어 대창섭이 메이플을 정상화하네' # and를 먼저 연산하고 그 다음에 or을 연산함
    else :
        return '바로 리부트 정상화'

print (RealCheck(reboot, normalizationNum), MultiCheck(reboot, normalizationNum))

mevenPow = 50000000 

def ElifTest (num1) :
    if (num1 >= 500000000) :
        return '하지만'
    elif (num1 >= 250000000) : # else if는 줄여서 elif로 쓴다
        return '여길봐도'
    elif (num1 >= 100000000) :
        return '저길봐도'
    elif (num1 >= 50000000) :
        return '오천플마단밖에 없네'
    else :
        return '인장주작은 뭐야'

print (ElifTest(mevenPow))

servers = ['스카니아', '리부트', '노바']
print (servers[0], servers[1], servers[2], servers[-1], servers[-2]) #index값을 음수로 먹일 수 있다. 그 경우에는 index 값만큼 역순으로 센 값이 나온다.
print (servers[1:2], servers[:3], servers[-1:3], servers[0:-1])

servers[1] = '에오스'
print (servers[:3], len(servers)) #len = 리스트 길이를 반환하는 함수
print (sorted(servers)) # sorted = 배열을 알파벳순으로 재정렬

ages = [22, 27, 35, 99]
print (sum(ages), max(ages)) # 둘다 기본함수임

servers.append('엘리시움') # 리스트 맨 마지막 자리에 내용물 추가
print(servers.pop()) # 리스트 맨 마지막에 있는 내용물을 제거 및 리턴
print(servers.index('스카니아'))
servers.append('헬리오스')

def IsRebootAlive() :
    if (not '리부트' in servers) :
        print ("1명을 죽이면 살인자, 100명을 죽이면 학살자, ")
    if ('에오스' in servers and '헬리오스' in servers) :
        print ("10000명을 죽이면 정복자, 10만을 죽이면 신창섭")

IsRebootAlive()
print (servers)

testTuples = '정상화', '정상화', '정상화' #tuple : 인덱스를 지정해서 값을 바꾸기는 불가능
print (testTuples)

testNum = 0.25
testTuples2 = testNum.as_integer_ratio() # 소수를 분자, 분모로 나누는 함수
print (testTuples2)
numerator, denominator = testTuples2 # 이런게 가능하다니
print (numerator, denominator, numerator / denominator)

numerator, denominator = denominator, numerator # tuple을 이용해 두 변수값 바꾸기를 한줄로 처리할 수 있음
print (numerator, denominator, numerator / denominator)

numerator, denominator = testTuples[0], testTuples[1]
print (numerator, denominator)
# 여기까지가 4월 16일 분량

for server in servers:
    print(server)

for i in range(8):
    print(i)

plusTwo = [n+2 for n in range(22)]
print(plusTwo, sep=' ')

servers = ['스카니아', '리부트', '노바']
funServers = [server for server in servers if server == '리부트']
print(funServers, sep=' ')

normServers = ['정상화' for server in servers]
print(normServers, sep=' ')

# 여기까지가 4월 21일 분량

print('\"리부트 서버\"는\n 그저 본보기였을 뿐 /\\') # string에서 특수기호 사용하기
lyric = "더는참지않겠다"
print ([char+'!' for char in lyric])

sampleText = 'Memento Mori'
print (sampleText.upper() + sampleText.lower())
print (lyric.index('참'))
print (sampleText.startswith('Memento'))
print (sampleText.endswith('oMori'))

sampleWords = sampleText.split()
print (sampleWords)
print ('❗️'.join([char for char in lyric]))

dateStr = '2024-01-08'
year, month, day = dateStr.split('-') # -를 기점으로 3등분하기
print('/'.join([month, day, year]))

trueHero = '아이언맨'
amount = 3000
print (trueHero + ', ' + str(amount) + '만큼 사랑해') # 문자가 아닌 값을 문자열에 합하려면 문자열로 바꿔야 함
print ('{}, {}만큼 사랑해'.format(trueHero, amount)) # 이렇게도 가능
print ('{1}, {0}만큼 사랑해'.format(trueHero, amount)) # 중괄호 안에 인덱스값 먹여서 조정도 가능

dictServers = {'스카니아':1, '리부트':2, '루나':3}
print (dictServers['리부트'])
dictServers['엘리시움'] = 4
print (dictServers)

serversToInitial = {server : server[0] for server in servers} # 문자열의 첫번째 자리를 dictionary의 인덱스값으로 설정
print (serversToInitial)

for i in dictServers:
    print ("{}는 아마도 {}번째 서버".format(i,dictServers[i]))

import math # 외부 라이브러리 불러오기
print (format(type(math)))
print ("파이를 소숫점 아래 10번째 자리까지 외워보자 = {:.11}".format(math.pi))
print ("{}는 {}의 {}제곱이에요".format(32,2,int(math.log(32,2))))

import math as mt # 외부 라이브러리에 별명붙여서 불러오기
print (format(type(mt)))
print ("파이를 소숫점 아래 10번째 자리까지 외워보자 = {:.11}".format(mt.pi))
print ("{}는 {}의 {}제곱이에요".format(32,2,int(mt.log(32,2))))

# 여기까지가 4월 22일 분량

sampleList = [1, 2, 3, 4, 5]
squareMap = map(lambda x: pow(x, 2), sampleList) # map 함수 : 왼쪽에는 함수, 오른쪽에는 iterable 자료형을 넣는다
print (list(squareMap)) # 출력할때는 List형으로 바꿔야 출력할 수 있다

sampleList2 = [2, 3, 4, 5, 6]
sumMap = map(lambda x, y: x+y, sampleList, sampleList2)
print (list(sumMap))

oddMap = filter(lambda x: True if (x % 2 == 1) else False, sampleList) # 가독성 생각하면 lambda 안쓰는게 좋을지도?
print (list(oddMap))

def IsEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

evenMap = filter(IsEven, sampleList) # lambda 안 쓴 버전
print (list(evenMap))

sampleZip = zip(sampleList, sampleList2) # 작은 size를 가지는 list에 맞춰서 자료형을 묶어줌
print (list(sampleZip))

sampleDict = {}
for sampleList, sampleList2 in zip(sampleList, sampleList2): # Zip을 활용한 Dictionary 만들기
    sampleDict[sampleList] = sampleList2
print (sampleDict)

for indexNum, value in enumerate(servers, start=1): # iterable형 자료를 index 값을 포함한 객체로 만들기
    print ("index: " + str(indexNum) + ", value: " + value)

# 여기까지가 4월 23일 분량