answer1 = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n'
answer2 = '"재귀함수가 뭔가요?"\n'
answer3 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'
answer4 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'
answer5 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n'
answer6 = '"재귀함수는 자기 자신을 호출하는 함수라네"\n'
answer7 = '라고 답변하였지.\n'
answer_f = '____'
r = int(input())


def teaching(n):
    s = ''
    if n == r:
        s = (answer_f * r)
        return s + answer2 + s + answer6 + s + answer7
    else:
        s = (answer_f * n)
        return s + answer2 + s + answer3 + s + answer4 + s + answer5 + teaching(n+1) + s + answer7


print(answer1 + answer2 + answer3 + answer4 + answer5 +
      teaching(1) + answer7)
