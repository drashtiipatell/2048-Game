
import random
a= [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

def up(a):
    for i in range(4):
        l=[]
        for j in range(4):
            if a[j][i] != '.':
                l.append(a[j][i])
        if len(l)>0:
            u= 0
            while u<len(l)-1:
                if l[u] == l[u+1]:
                    l[u] *= 2
                    l.pop(u+1)
                u+=1
        if len(l)>0:
            while len(l)<4:
                    l.append('.')
                
            for k in range(4):
                a[k][i] = l[k]
    return(a)
    
def down(a):
    for i in range(4):
        l=[]
        for j in range(4):
            if a[j][i] != '.':
                l.append(a[j][i])
        if len(l)>0:
            u= len(l)-1
            while u>0:
                if l[u] == l[u-1]:
                    l[u-1] *= 2
                    l.pop(u)
                    u-=1
                u-=1
        l.reverse()
        if len(l)>0:
            while len(l)<4:
                    l.append('.')
            l.reverse()
            for k in range(4):
                a[k][i] = l[k]
    return a
def left(a):
    for i in range(4):
        l=[]
        for j in range(0,4):
            if a[i][j] != '.':
                l.append(a[i][j])
        if len(l)>0:
            u= 0
            while u<len(l)-1:
                if l[u] == l[u+1]:
                    l[u] *= 2
                    l.pop(u+1)
                u+=1
        if len(l)>0:
            while len(l)<4:
                    l.append('.')
                
            for k in range(4):
                a[i][k] = l[k]
    return(a)
def right(a):
    for i in range(4):
        l=[]
        for j in range(4):
            if a[i][j] != '.':
                l.append(a[i][j])
        if len(l)>0:
            u= len(l)-1
            while u>0:
                if l[u] == l[u-1]:
                    l[u-1] *= 2
                    l.pop(u)
                    u-=1
                u-=1
        l.reverse()

        if len(l)>0:
            while len(l)<4:
                    l.append('.')
            l.reverse()
            for k in range(4):
                a[i][k] = l[k]
    return a
def getempty(a):
    s  = []
    for i in range(4):
        for j in range(4):
            if a[i][j] == '.':
                s.append([i,j])
    return s
def printt(m):
    for i in range(len(m)):
        print(m[i])
def generaterandomind(s):
    return random.randint(0,len(s)-1)
def get2048(a):
    for i in range(4):
        for j in range(4):
            if a[i][j] == 2048:
                return True
    return False

def game(a):    
    p = input("Enter 'a' for left , 's' for down, 'd' for right , 'w' for up.........: \n " )
    if p == 'a':
        a = left(a)

    elif p == 's':
        a = down(a)
    elif p == 'd':
        a = right(a)
    elif p == 'w':
        a = up(a)

while get2048(a) != True :
    g = getempty(a)
    if len(g) == 0:
        print('Cells Over, better Luck Next time.')
    l  = generaterandomind(g)
    a[g[l][0]][g[l][1]] = 2
    printt(a)

    game(a)

print('You Win')
p = input()
t = getempty(a)
