from sys import stdin


arrs = [list(map(int,stdin.readline().split())) for i in range(4)]

"""
무승부 개수만 리스트로 가장 큰원소(팀)의 경기를 차례로 지워서 최종적으로 [0] 형태가 나올수 있어야함.
ex) 
[5,4,1,0,0,0] -> 5무승부인 팀과 무승부가 0인팀이 같이 있을 수 없으므로 처음부터 불가능한 형태
[4,4,2,1,1,0] -> [3,1,0,0,0] -> 3과 함께 지울수 있는 경기가 다른팀에 없으므로 불가능한 형태(무승부 수는 )
"""
def drw(lis):
    print(lis)
    for i in range(5):
        p = lis.pop(0)
        if p>len(lis):  return False    #런타임 오류방지, 오답 입력되면 리스트범위 넘어갈수있음
        for j in range(p):     #0부터 첫번째 원소값 만큼 리스트 원소들 --
            lis[j]-=1
        lis.sort(reverse=True)
        print(lis)  ###################################################################
        if -1 in lis:   return False
    if lis[0]!=0: return False
    return True

"""
함수 drw처럼  승,패 리스트를 받아서 
승리 리스트를 pop 하면서 패배리스트 원소 --
최종적으로 패배 리스트는 [0,0,0,0,0,0] 형태가 되야함
"""
def winlose(w,l):
    for i in range(6):
        print(w,l,end=" ->")
        for j in range(w.pop(0)): l[j]-=1
        l.sort(reverse=True)
        print(l)
        if l[5]==-1: return False
    
    if l.count(0)!=6:   return False
    return True

for arr in arrs:        
    
    #1) 총 승리 수 = 총 패배 수
    if (sum(arr[0::3]) - sum(arr[2::3])) != 0:   
        print(0,end='<1번>')
        continue
    
    #2) 6이상 입력 방지
    if max(arr)>=6:    
        print(0,end='<2번>')
        continue
    
    #3) 각 팀당 승 무 패 개수 합은 5여야 한다
    try:
        for i in range(0,18,3):  
            if sum(arr[i:i+3:1]) != 5:
                print(0,end='<3번 승무패5> ')
                raise Exception()
    except:         #예외처리로 틀렸을 때 바로 바깥반복문에서 continue되도록
        continue
    
    #4) 무승부 수 맞추기
    if drw(sorted(arr[1::3],reverse=True))==False:
        print(0,end='<4번 무승부수>\n ')
        continue
    
    #5) 승-패 수 맞추기
    if winlose(sorted(arr[0::3],reverse=True),sorted(arr[2::3],reverse=True))==False:
        print(0,end='<5번 승패수>\n ')
        continue
        
    else:
        print(1,end=' ')    

#왜 안되
    
    
        
    