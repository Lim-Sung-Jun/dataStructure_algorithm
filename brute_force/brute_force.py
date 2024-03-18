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

# 3.18 카페 문제
from math import sqrt, ceil
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for h in range(3, total + 1):
        if total % h == 0:
            w = total/h
            if (w - 2) * (h - 2) == yellow:
                answer = [w,h]
                break
    return answer

# 3.18 피로도 문제
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    dun_len = len(dungeons)
    # permutations를 사용하면 리스트의 모든 조합을 알 수 있다. 중복 x, 순서 o
    
    for permute in permutations(dungeons, dun_len):
        hp = k
        count = 0 
        
        # 조합에 대해서 하나씩 돌아가면서 조건을 만족하는지 살펴보고 만족하면 count를 더해준다.
        for pm in permute:
            if hp >= pm[0]:
                hp -= pm[1]
                count += 1
            
            if count > answer:
                answer = count
    
    return answer

# 3.18 전력량 문제
def solution(n, wires):
    from collections import defaultdict
		
    # 트리(전력망) 구성
    graph = defaultdict(list)
    for v1, v2 in wires:
		    # 각각의 입장에서 graph를 구성해준다.
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(node, visited):
        # 재귀적 DFS로 노드(송전탑)의 개수 세기
        count = 1  # 현재 노드도 개수에 포함
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
		            # count를 더하면서 backtracking을 하면 중첩될 수 있다.
                count += dfs(neighbor, visited)
        return count

    min_diff = n  # 가능한 최대 차이로 초기화
    for v1, v2 in wires:
        # 각 전선을 끊어서 두 전력망으로 나눔
        visited = set()
        # 한 쪽 전력망의 송전탑 개수를 세어내면 다른 쪽도 알 수 있다.
        count1 = dfs(v1, visited | {v2})  # v2 방문 처리하여 끊기
        count2 = n - count1  # 나머지 전력망의 송전탑 개수
        # 두 전력망의 송전탑 개수 차이의 절대값
        diff = abs(count1 - count2)
        min_diff = min(min_diff, diff)

    return min_diff

# 주어진 예제
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))