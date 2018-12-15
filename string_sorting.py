# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수,
# solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

def solution(s):
    import string

    answer = ''
    upper = ''
    lower = ''

    for char in s:
        if char in string.ascii_uppercase:
            upper += char
        else:
            lower += char
    upper = sorted(upper, reverse=True)
    lower = sorted(lower, reverse=True)


    for string in lower:
        answer += string
    for string in upper:
        answer += string

    return answer



def test(func):
    cases = [
        "Zbcdefg",
        "YDabdc"
    ]

    results = [
        "gfedcbZ",
        "dcbaYD"
    ]

    for index, case in enumerate(cases):
        try:
            assert func(case) == results[index]
        except AssertionError:
            print(func(case), case)
            raise
        print("success:", index)

    print("SUCCESS")

test(solution)
