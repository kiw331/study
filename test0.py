from sys import stdin

arrs = [list(map(int,stdin.readline().split())) for i in range(4)]

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
    idx2 = 0 
    max2 = 0
    for i in range(len(lis)):
        if i==idx1: continue   
        if lis[i]>=max2:    
            idx2=i
            max2=lis[i]
    return idx2

def winlose(w,l):
    for i in range(sum(w)):
        mw = w.index(max(w))
        ml = l.index(max(l))
        if mw!=ml:  
            w[mw]-=1
            l[ml]-=1
        else:
            secl = find2idx(l,ml)
            if l[secl]==0: return False
            w[mw]-=1
            l[secl]-=1
    if w.count(0)!=6 or l.count(0)!=6: return False
    return True

# def winlose2(w,l):
#     for i in range(6):
#         for j in range(w.pop(0)): l[j]-=1
#         l.sort(reverse=True)
#         if l[5]==-1: return False
#     if l.count(0)!=6:   return False
#     return True

for arr in arrs:        
    #2) 6이상 입력 방지
    if max(arr)>=6 or min(arr)<0:    
        print(0,end=' ')
        continue
    
    #1) 총 승리 수 = 총 패배 수
    if (sum(arr[0::3]) - sum(arr[2::3])) != 0:   
        print(0,end=' ')
        continue
    
    if sum(arr[1::3])%2 ==1:
        print(0,end=' ')
        continue
    
    #3) 각 팀당 승 무 패 개수 합은 5여야 한다
    try:
        for i in range(0,18,3):  
            if sum(arr[i:i+3:1]) != 5:
                print(0,end=' ')
                raise Exception()
    except:         #예외처리로 틀렸을 때 바로 바깥반복문에서 continue되도록
        continue
    
    if sum(arr[0::3])>15 or sum(arr[2::3])>15 or sum(arr[1::3])>30:   
        print(0,end=' ')
        continue
        
    #4) 무승부 수 맞추기
    if drw(sorted(arr[1::3],reverse=True))==False:
        print(0,end=' ')
        continue
    
    #5) 승-패 수 맞추기
    if winlose(arr[0::3],arr[2::3])==False:
        print(0,end=' ')
        continue
    # if winlose2(sorted(arr[0::3],reverse=True),sorted(arr[2::3],reverse=True))==False:
    #     print(0,end=' ')
    #     continue
        
    print(1,end=' ')    


    
    
        
    