# 1. 타겟넘버
### bfs
from collections import deque
def solution(numbers, target):
    answer = 0
    
    # queue
    q = deque()
    
    # 시작
    q.append((0,0))
    
    while q:
        current_sum, count = q.popleft()
        if count == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            next_num = numbers[count]
            q.append((current_sum + next_num, count + 1))
            q.append((current_sum - next_num, count + 1))
    
    return answer
    
### dfs
def solution(numbers, target):
    def dfs(index, current_sum):
        # 모든 숫자를 사용했을 때
        if index == len(numbers):
            # 현재 합계가 타겟 넘버와 동일한 경우
            if current_sum == target:
                return 1
            else:
                return 0
        # 현재 숫자를 더하거나 빼는 경우를 모두 고려
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])
    
    # dfs 함수 시작
    answer = dfs(0, 0)
    return answer

# 2. 네트워크
def solution(n, computers):
    answer = 0
    # 제약조건
    if n == 1:
        return 1
    
    # visited 리스트 만들기
    visited = [[ False for _ in range(n)] for _ in range(n)]
    
    def dfs(x, y):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        visited[x][y] = True
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            # 범위 걸림? 방문 기록?
            if next_x < n and next_x > -1 and next_y < n and next_y > -1:
                if not visited[next_x][next_y] and computers[next_x][next_y] == 1:
                    # visited[next_x][next_y] = True
                    dfs(next_x, next_y)
                    
    # 모든 원소를 넘어가면서
    for i in range(n):
        for j in range(n):
        # 만약에 1이고 방문을 안했다면
            if computers[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                answer += 1
    return answer
def solution(n, computers):
    answer = 0
    # 각 컴퓨터의 방문 여부를 기록하는 일차원 리스트
    visited = [False] * n
    
    def dfs(computer):
        visited[computer] = True
        # 주변 컴퓨터들을 확인한다.
        for connect in range(n):
		        # 인접리스트를 전부 볼 필요가 없이 노드끼리 연결되어있는지의 여부만 확인한다.
		        # 방문처리해준다.
            if computers[computer][connect] == 1 and not visited[connect]:
                dfs(connect)
                
    for i in range(n):
        if not visited[i]:
		        # 네트워크를 확인한다.
            dfs(i)
            answer += 1
            
    return answer


