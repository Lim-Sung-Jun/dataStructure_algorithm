# 최소직사각형
def solution(sizes):
    allWidth = []
    allHeight = []
    for size in sizes:
			  # 사이즈가 큰 게 있으면 swap한다.
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        # swap하고 큰 값은 왼쪽리스트에 작은 값은 오른쪽 리스트에 저장한다.
        allWidth.append(size[0])
        allHeight.append(size[1])

    return max(allWidth) * max(allHeight)

# 모의고사
def solution(answers):
    
    answer = []
    score = [0,0,0]
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)) :
        if answers[i] == student1[i%5] :
            score[0] += 1
        if answers[i] == student2[i%8] :
            score[1] += 1
        if answers[i] == student3[i%10] :
            score[2] += 1
        
    for idx, num in enumerate(score) :
        if num == max(score) :
            answer.append(idx +1)
    
    return answer

# 소수찾기
from itertools import permutations

def solution(n):
    prime = set()
    # 1. 모든 숫자 조합을 만든다
    for i in range(len(n)):   
		    # Set에 모든 조합을 추가한다.                                             
        prime |= set(map(int, map("".join, permutations(list(n), i + 1))))
    # 2. 소수가 아닌 수를 제외한다.
    prime -= set(range(0, 2)) # 0, 1은 포함하지 않는 것을 알아야한다.
    for i in range(2, int(max(prime) ** 0.5) + 1):
		    # Set에서 소수가 아닌 수를 제거한다.
        prime -= set(range(i * 2, max(prime) + 1, i))
    return len(prime)

print(solution("117"))