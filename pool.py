# -*- coding: utf-8 -*-
import random as r


class Fish(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def run(self,x,y):
        direction=r.randint(1,5)#1 上,2 下,3 左,4 右
        if direction==1:
            if self.y==y:
                    self.y-=1
            else:
                self.y+=1
        elif direction==2:
            if self.y==0:
                    self.y+=1
            else:
                self.y-=1
        elif direction==3:
            if self.x==0:
                    self.x+=1
            else:
                self.x-=1
        else:
            if self.x==x:
                    self.x-=1
            else:
                self.x+=1


class Tortoise(object):
    def __init__(self,x,y,hp=100):
        self.x=x
        self.y=y
        self.hp=hp

    def run(self,x,y):
        direction=r.randint(1,5)#1 上,2 下,3 左,4 右
        distance=r.randint(1,3)
        if direction==1:
            if self.y+distance>y:
                if self.y==y:
                    self.y=y-distance
            else:
                self.y+=distance
        elif direction==2:
            if self.y-distance<0:
                if self.y==0:
                    self.y=distance
            else:
                self.y-=distance
        elif direction==3:
            if self.x-distance<0:
                if self.x==0:
                    self.x=distance
            else:
                self.x-=distance
        else:
            if self.x+distance>x:
                if self.x==x:
                    self.x=x-distance
            else:
                self.x+=distance
        self.hp-=1

    def eatFish(self,tor,fishXY,fishAll,j):
        while tor in fishXY:
            if self.hp <= 80:
                self.hp += 20
            else:
                self.hp = 100
            fishAll.pop(fishXY.index(tor))
            fishXY.pop(fishXY.index(tor))
            print('%d条鱼已经被吃掉了' % (j + 1))
            j += 1
        return j


class Pool(object):
    def __init__(self,x=10,y=10):
        self.x = x
        self.y = y

    def play(self, n):
        tortoise=Tortoise(r.randint(0,self.x+1),r.randint(0,self.y+1))
        tor=[tortoise.x,tortoise.y]
        fishXY=[]
        fishAll=[]
        for i in range(n):
            fishc=Fish(r.randint(0,self.x+1),r.randint(0,self.y+1))
            fishXY.append([fishc.x,fishc.y])
            fishAll.append(fishc)
        j=0
        j=tortoise.eatFish(tor,fishXY,fishAll,j)
        if j == n:
            print('乌龟胜！')
            return
        while 1:
            tortoise.run(self.x,self.y)
            tor[0],tor[1] =tortoise.x,tortoise.y
            j = tortoise.eatFish(tor, fishXY, fishAll, j)
            if j == n:
                print('乌龟胜！')
                return
            if tortoise.hp==0:
                print('乌龟没体力了！鱼胜！！')
                return
            k=0
            for fi in fishAll:
                fi.run(self.x,self.y)
                fishXY[k][0],fishXY[k][1]=fi.x,fi.y
            j = tortoise.eatFish(tor, fishXY, fishAll, j)
            if j == n:
                print('乌龟胜！')
                return


def main():
    pool=Pool(10,10)
    pool.play(50)


if __name__=='__main__':
    main()