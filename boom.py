import random as r
import math as m
class coordinate(object):#坐标
    def __init__(self,lx,by,rx,ty):
        self.lx=lx
        self.by=by
        self.rx=rx
        self.ty=ty

class PeopleBody(object):#身体部位
    def __init__(self,larm,rarm,lleg,rleg,upbody,head):
        self.larm=larm
        self.rarm=rarm
        self.lleg=lleg
        self.rleg=rleg
        self.upbody=upbody
        self.head=head
    def run(self):
        pass


class People(PeopleBody):#人
    def __init__(self, name, sex, age, height, weight,attDistance,larm,rarm,lleg,rleg,upbody,head,blood=100, power=25):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.blood = blood
        self.power = power
        self.attDistance=attDistance
        super().__init__(larm, rarm, lleg, rleg, upbody, head)


    def inPeoBody(self,body,x,y):#判断坐标是否在身体部位坐标内
        if body.lx<x<body.rx and body.by<y<body.ty:
            return True
        else:
            return False


    def addBullet(self, number):#装子弹
        self.gun.addBullet(number)

    def addGun(self, gun):#配枪
        self.gun = gun
        self.power = self.gun.power
        self.attDistance=self.gun.attDistance

    def printPeoInfo(self):#打印个人信息
        if self.blood == 0:
            print('%s已经死亡！' % self.name)
        if hasattr(self, 'gun'):
            print('名字：%s,持枪:%s,血量:%d' % (self.name, self.gun.name, self.blood))
        else:
            print('名字：%s,持枪:无,血量:%d' % (self.name, self.blood))

    def death(self):#死亡
        print('%s已经被杀死！！！' % self.name)


    def bodyAtt(self, power, people):#拳头攻击
        if power >= people.blood:
            print('%s掉了%d的血量！'%(people.name,people.blood))
            people.blood = 0
            people.death()
        else:
            print('%s掉了%d的血量！' % (people.name,power))
            people.blood -= power


    def attackPeople(self, people,reduceBlood):#攻击
        if self.blood == 0:
            print('您已经死亡，不可再发动攻击！')
            return
        if people.blood == 0:
            print('目标已经死亡！！')
            return
        px = (people.upbody.lx + people.upbody.rx) / 2
        py = (people.upbody.by + people.upbody.ty) / 2
        sx = (self.upbody.lx + self.upbody.rx) / 2
        sy = (self.upbody.by + self.upbody.ty) / 2
        if self.attDistance < m.sqrt((sx - px) * (sx - px) + (sy - py) * (sy - py)):
            print('攻击距离不够！')
        else:
            x = r.randint(self.larm.lx, self.rarm.rx + 1)
            y = r.randint(self.lleg.by, self.head.ty)
            if self.inPeoBody(self.larm, x, y) or self.inPeoBody(self.rarm, x, y):
                ins = 1
            elif self.inPeoBody(self.lleg, x, y) or self.inPeoBody(self.rleg, x, y):
                ins = 2
            elif self.inPeoBody(self.upbody, x, y):
                ins = 3
            elif self.inPeoBody(self.head, x, y):
                ins = 4
            else:
                ins=5
            if hasattr(self, 'gun'):
                if self.gun.clip.capad <= 0:
                    pro = input('%s,弹夹暂无子弹，请问您要补充子弹吗？(yes/no):'%self.name)
                    if pro == 'yes':
                        self.addBullet(self.gun.clip.capacity)
                    else:
                        print('已没有子弹，未补充子弹!')
                else:
                    if ins==5:
                        self.gun.clip.capad-=1
                        self.gun.clip.bulletd.pop()
                        print('%s用枪向%s发起攻击！未打中！！' % (self.name, people.name))
                        return
                    else:
                        print('%s用枪向%s发起攻击！boom！' % (self.name, people.name),end='')
                        self.gun.fire(self.power*reduceBlood[ins], people)
            else:
                if ins == 5:
                    print('%s用拳头向%s发起攻击！未打中！！' % (self.name, people.name))
                    return
                self.bodyAtt(self.power*reduceBlood[ins],people)


class Gun:#枪        # 枪名字  重量    模式  攻击力   后坐力  攻击距离      弹夹
    def __init__(self, name, weight, mode, power, recoil, attDistance, clip):
        self.name = name
        self.weight = weight
        self.mode = mode
        self.power = power
        self.recoil = recoil
        self.attDistance = attDistance
        self.clip = clip

    def addBullet(self, bulletNumber):#装子弹
        self.clip.addBullet(bulletNumber)

    def fire(self, power, people):#开火
        self.clip.capad -= 1
        self.clip.bulletd.pop()
        if power >= people.blood:
            print('%s掉了%d的血量！'%(people.name,people.blood))
            people.blood = 0
            people.death()
        else:
            print('%s掉了%d的血量！' % (people.name,power))
            people.blood -= power



class Clip:#弹夹        #容量     子弹半径    装入的子弹列表   子弹种类  已装的个数
    def __init__(self, capacity, bulletRadius,  bulletd,    bulletF, capad=0):
        self.capacity = capacity
        self.bulletRadius = bulletRadius
        self.bulletd = bulletd
        self.bulletF = bulletF
        self.capad = capad

    def addBullet(self, bulletNumber):
        if bulletNumber > self.capacity - self.capad:
            print('弹夹存储空间不足，还可以装%d个子弹！' % (self.capacity-self.capad))
        else:
            for i in range(bulletNumber):
                self.bulletd.append(self.bulletF.name)
            self.capad += bulletNumber




class Bullet:#子弹
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


def main():
    laowang_larm=coordinate(20,140,100,160)
    laowang_rarm=coordinate(160,140,240,160)
    laowang_lleg=coordinate(100,0,120,100)
    laowang_rleg=coordinate(140,0,160,100)
    laowang_upbody=coordinate(100,100,160,160)
    laowang_head=coordinate(120,160,140,180)
    laoli_larm = coordinate(220, 240, 300, 260)
    laoli_rarm = coordinate(360, 240, 440, 260)
    laoli_lleg = coordinate(300, 100, 320, 200)
    laoli_rleg = coordinate(340, 100, 360, 200)
    laoli_upbody = coordinate(300, 200, 360, 260)
    laoli_head = coordinate(120, 260, 140, 280)
    laowang = People('老王', 'man', 30, 180, 120,20,laowang_larm,laowang_rarm,laowang_lleg,laowang_rleg,laowang_upbody,laowang_head)
    laoli = People('老李', 'man', 32, 175, 130,25,laoli_larm,laoli_rarm,laoli_lleg,laoli_rleg,laoli_upbody,laoli_head)

    laowang.printPeoInfo()
    laoli.printPeoInfo()
    print('----------------------')
    reduceBlood=[0,0.9,0.8,1,3]

    M4C = []
    AKC = []

    M4Bullet = Bullet('m4子弹', 5.56)#子弹
    AKBullet = Bullet('AK子弹', 7.62)

    M4clip = Clip(30, 5.56, M4C, M4Bullet)#弹夹
    AKclip = Clip(40, 7.62, AKC, AKBullet)

    m4a1 = Gun('M4A1', 30, '连发', 20, 15, 500, M4clip)#枪
    AK47 = Gun('AK47', 50, '连发', 40, 30, 700, AKclip)

    laowang.addGun(m4a1)#拿枪
    laoli.addGun(AK47)

    laowang.printPeoInfo()
    laoli.printPeoInfo()

    while 1:
        print('----------------------')
        laowang.attackPeople(laoli,reduceBlood)#攻击
        laoli.attackPeople(laowang,reduceBlood)
        if laowang.blood != 0 and laoli.blood != 0:
            laowang.printPeoInfo()
            laoli.printPeoInfo()
        else:
            break
    print('----------------------')
    laowang.printPeoInfo()
    laoli.printPeoInfo()
    if laowang.blood == 0:
        if laoli == 0:
            print('同归于尽！！！！！')
        else:
            print('老李获胜！！！！！')
    else:
        print('老王获胜！！！！！')

if __name__ == '__main__':
    main()
