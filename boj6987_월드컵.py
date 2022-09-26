from sys import stdin


arrs = [list(map(int,stdin.readline().split())) for i in range(4)]

"""
무승부 개수 리스트로 가장 큰원소(팀)의 경기를 차례로 지워서 최종적으로 [0] 형태가 나올수 있어야함.
ex) 
[5,4,1,0,0,0] -> 5무승부인 팀과 무승부가 0인팀이 같이 있을 수 없으므로 처음부터 불가능한 형태
[4,4,2,1,1,0] -> [3,1,0,0,0] -> 3과 함께 지울수 있는 경기가 다른팀에 없으므로 불가능한 형태
"""
def drw(lis):
    for i in range(5):
        p = lis.pop(0)
        if p>len(lis):  return False    #런타임 오류방지, 오답 입력되면 리스트범위 넘어갈수있음
        for j in range(p):     #0부터 첫번째 원소값 만큼 리스트 원소들 --
            lis[j]-=1
        lis.sort(reverse=True)
        if -1 in lis:   return False
    if lis[0]!=0: return False
    return True

def find2idx(lis,idx1): #리스트에서 두번째로 큰수의 인덱스 반환
    idx2 = 0 ; max2=0
    for i in range(len(lis)):
        if i==idx1: continue   
        if lis[i]>=max2:    
            idx2=i
            max2=lis[i]
    return idx2
    

"""
승리수리스트, 패배수리스트를 받아
승리수와 타팀의 패배수를 하나씩 깜
최종적으로 두리스트 모두 [0,0,0,0,0,0] 형태가 되야함
"""

# 수정필요
# 하니씩 빼고 정렬하니까 같은 팀에서 2번 뺄수도 있음
# 반례: 5 0 0 5 0 0 5 0 0 0 0 5 0 0 5 0 0 5 -> 1
def winlose(w,l):
    for i in range(sum(w)):
        mw = w.index(max(w))
        ml = l.index(max(l))
        if mw!=ml:  
            w[mw]-=1
            l[ml]-=1
        else:
            secl = find2idx(l,ml)
            if l[secl]==0: 
                print("0이다")
                return False
            w[mw]-=1
            l[secl]-=1
        print("w l",w,l)
    if w.count(0)!=6 or l.count(0)!=6: return False
    return True


for arr in arrs:        
    #1) 총 승리 수 = 총 패배 수
    if (sum(arr[0::3]) - sum(arr[2::3])) != 0:   
        print(0,end='<1번>\n')
        continue
    
    #2) 6입력방지 
    if 6 in arr:    
        print(0,end='<2번>\n')
        continue
    
    #3) 각 팀당 승 무 패 개수 합은 5여야 한다
    try:
        for i in range(0,18,3):  
            if sum(arr[i:i+3:1]) != 5:
                print(0,end='<3번 승무패5>\n')
                raise Exception()
    except:         #예외처리로 틀렸을 때 바로 바깥반복문에서 continue되도록
        continue
    
    #4) 무승부 수 맞추기
    if drw(sorted(arr[1::3],reverse=True))==False:
        print(0,end='<4번 무승부수>\n ')
        continue
    
    #5) 승-패 수 맞추기
    if winlose(arr[0::3],arr[2::3])==False:
        print(0,end='<5번 승패수>\n ')
        continue
        
    print(1,end='\n')    

#왜 안되
    
    
        
    