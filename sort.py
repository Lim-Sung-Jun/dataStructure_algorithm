# 1. k번째 값
def solution(array, commands):
    answer = []
    # commands 돌기
    for command in commands:
        # sub list 가져오기
        sub_array = array[command[0] - 1: command[1]]
        print(sub_array)
        
        # 정렬하기
        sub_array.sort()
        
        # k값 가져오기
        k_element = sub_array[command[2] - 1]
        
        # answer에 저장
        answer.append(k_element)
    return answer
    
    ### 한줄풀이
def solution(array, commands):
    return [sorted(array[start - 1:end])[k - 1] for start, end, k in commands]

# 2. 가장 큰 수
### 시간초과 문제!
from itertools import permutations

def solution(numbers):
    # 이게 중요하다. join은 문자열에서만 된다.
    numbers = list(map(str, numbers))
    
    answer = ''
    permute_list = []
    # numbers의 순열을 만들기
    numbers_list = permutations(numbers, len(numbers))
    permute_list = list(map(int, map("".join, numbers_list)))
    
    # sort하여 가장 큰 수 answer에 담기
    permute_list.sort()
    answer = str(permute_list[-1])
    return answer
    
### 
def solution(numbers):    
    s = list(map(str,numbers))
    # 최대 세자리 수이므로 길이를 3배로 늘렸고, 앞 위치에 어떤 숫자가 들어가면 좋을지를 결정하기 위해서
    # 이러한 방법을 사용한다.
    a = sorted(s,key=lambda x: x*3,reverse=1)
    return str(int("".join(a)))

# 3. H-index
def solution(citations):
    answer = 0
    # citations 돌기
    for i in range(len(citations)):
        count = 0
        for j in range(len(citations)):
            # 만약에 count와 citations 같으면 리턴
            if citations[i] <= citations[j]:
                count += 1
        # h의 최댓값 구해서 answer
        # 이 풀이가 맞는 거니깐 문제의 정의를 올바르게 이해하자.
        if count >= citations[i]:
            answer = max(answer, citations[i])
    return answer
    
#### 잘 이해가 안간다.
def solution(citations):
    
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
        
    return len(citations)