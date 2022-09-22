from sys import stdin
from itertools import permutations

n,l,r = map(int,stdin.readline().split())

arr = list(permutations(range(1,n+1), n))   
# 1부터 l까지 수 나열한다고 생각

print(arr)



for p in arr:
    hidx = p.index(n) #최대 높이 건물 인덱스
    
    cnt = 1 #현재 보이는 건물개수
    ll = 0  #왼쪽에서 현재 최대 높이 건물
    lr = 0  #오른쪽에서 현재 최대 높이 건물

    for i in p:
        #print(i,end=' ')
        
        if i>ll:    # 왼쪽에서 i인덱스의 건물 높이가 ll보다 크다 = 보이는 건물개수 늘어남
            ll = i
            cnt +=1
        if i >= hidx:  #i가 왼쪽에서 부터 최대 높이 인덱스까지 증가하면 cnt은 더 안늘어남
            break
        
    # 이때 카운트가 정답과 다르면 해당 배치 p는 후보에서 삭제
    if cnt!=l:  
        arr.remove(p) 
        continue
        
    
print(arr)



