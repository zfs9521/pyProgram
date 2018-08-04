# -*- coding: utf-8 -*-
import os
def insertGoods():
    pass
def deleteGoods():
    pass
def changePrice():
    pass
def superAct():
    pass
def moneyToVip():
    pass

def printMenu():
    print("********张峰硕大礼包**********")
    print("   1.   进入用户系统         ")
    print("   2.  进入管理员系统        ")
    print("   3.     退出系统           ")
    print("****************************")



def printUserMenu():
    print("******欢迎来到用户系统*******")
    print("   1.   超土豪咖啡     8元  ")
    print("   2. 宇宙无敌大榴莲   12元  ")
    print("   3. 自动翻译笔记本   15元  ")
    print("   4. 科比签名篮球    500元  ")
    print("   5.   路飞草帽     1000元  ")
    print("   6.     结账               ")
    print("   7.     离开               ")
    print("****************************")



def printAdMenu():
    print("******欢迎来到管理员系统*******")
    print("   1. 查看用户会员卡信息       ")
    print("   2.  查看用户消费信息        ")
    print("   3.    注册会员卡            ")
    print("   4.    注销会员卡            ")
    print("   5.  退出管理员系统          ")
    print("******************************")



def regVipInfo(userVipID):
    isD = input('要办一张会员卡吗？(yes/no):')
    if isD == 'yes':
        while 1:
            userTel = input('请输入手机号：')
            if len(userTel)!=11:
                prob=input('手机号非11位，请问您要重新输入嘛？(yes/no):')
                if prob!='yes':
                    break
                else:
                    continue
            userVipId = input('请输入想办理的会员卡号:')
            if userVipId in userVipID.keys():
                tt = input('会员卡号已存在，是否继续？(yes/no):')
                if tt == 'yes':
                    continue
                else:
                    break
            else:
                userVipId1 = input('请确认想办理的会员卡号:')
                if userVipId==userVipId1:
                    userVipID[userVipId] = userTel
                    with open('D:\\vip.txt','a') as f:
                        f.write(userVipId+','+userTel+'\n')
                    f.close()
                    print('恭喜办理成功会员卡，下次购物生效！')
                    break
                else:
                    tt=input('两次输入不一致，是否重新注册？(yes/no):')
                    if tt=='yes':
                        continue
                    else:
                        break



def LogoutVipInfo(userVipID):
    while 1:
        userVipId = input('请输入要注销的会员卡号(#号退出):')
        if userVipId=='#':
            break
        if userVipId in userVipID.keys():
            print('手机号：', userVipID[userVipId], '\t卡号:',userVipId )
            userVipId1 = input('确认注销会员信息？(yes/no):')
            if userVipId1 == 'yes':
                userVipID.pop(userVipId)
                with open('D:\\vip.txt', 'w') as f:
                    for id,tel in userVipID.items():
                        f.write(id+','+tel+'\n')
                f.close()
                temp = input('注销成功，是否继续注销？(yes/no):')
                if temp == 'yes':
                    continue
                else:
                    break
            else:
                temp = input('是否继续注销？(yes/no):')
                if temp=='yes':
                    continue
                else:
                    break
        else:
            print('您输入的会员卡号不存在！')
            temp = input('是否继续？(yes/no):')
            if temp == 'yes':
                continue
            else:
                break



def useVipCard(userVipID,userVipN):
    flag = False
    while 1:
        inputVipId = input('请输入您的会员卡号:')
        if inputVipId in userVipID.keys():
            flag = True
            userVipN=inputVipId
            break
        else:
            isR = input('卡号信息错误，是否要重新使用会员卡？(yes/no):')
            if isR == 'yes':
                continue
            else:
                break
    return flag,userVipN




def printUserBuyInfo(flag,userVipN, num, menu, price, allUserBuyInfo, sum,allUserBuyInfoGoodsId):
    userBuyInfo=[]
    userBuyInfoGoodsId=set()
    print("{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}".format('货品种类', '数目', '单价', '总价'))
    for i in range(0, 6):
        if num[i] != 0:
            userBuyInfo.append(menu[i])
            userBuyInfo.append('数目:'+str(num[i]))
            if i!=0:
                userBuyInfoGoodsId.add(i)
            print("{0:^10}\t{1:^10}\t{2:^10}\t{3:^10}".format(menu[i], num[i], price[i], num[i] * price[i]))
            num[i]=0
    if flag:
        print("  \t\t\t\t\t\t\t\t\t总价:  ", sum)
        print("\t\t\t\t\t\t\t\t\t会员价:", sum * 0.9)
        pri1='总价:'+str(sum)
        pri2='会员价:' + str(sum*0.9)
        userBuyInfo.append(pri1)
        userBuyInfo.append(pri2)
        userBuyInfo.append('会员卡号:'+userVipN)
    else:
        print("  \t\t\t\t\t\t\t\t\t总价:  ", sum)
        pri='总价:'+str(sum)
        userBuyInfo.append(pri)
    s=''
    for temp in userBuyInfo:
        s+=temp+','
    s=s[:-1]
    with open('D:\\buyInfo.txt','a') as f:
        f.write(s+'\n')
    f.close()
    allUserBuyInfo.append(userBuyInfo)
    if len(userBuyInfoGoodsId)!=0:
        allUserBuyInfoGoodsId.append(userBuyInfoGoodsId)



def pushBuy(buyGoods,allUserBuyInfoGoodsId,menu,price,num):
    sum=0
    if len(allUserBuyInfoGoodsId)!=0:
        temp=set()
        sub=10
        for sets in allUserBuyInfoGoodsId:
            length=len(buyGoods ^ sets)
            if length!=0 and length<sub:
                sub=length
                temp=sets-buyGoods
        if len(temp)!=0:
            MAX=max(temp)
            isB=input('请问您想购买'+menu[MAX]+'吗？(yes/no):')
            if isB=='yes':
                isN = int(input('请输入您想购买的数目:'))
                if isN>=1:
                    num[MAX]+=isN
                    sum=isN*price[MAX]
    return sum


def userFeatures(count,n,price, userVipID, num, menu, allUserBuyInfo,allUserBuyInfoGoodsId):
    sum=0
    if count == 12:
        print('今日已闭店，欢迎您明天光临！')
        return count
    print('您是今天第', count, '位客户！')#m元
    isBuyZ=input('请问您想不想购买本店最新的爆款产品周杰伦演唱会门票呢？(yes/no):')
    if isBuyZ=='yes':
        isZ=int(input("请输入您想购买的数目:"))
        if isZ>=1:
            num[0]=isZ
            sum+=1500*isZ
    buyGoods=set()
    per=1
    while 1:
        printUserMenu()
        select = int(input('请输入选项:'))
        if 1 <= select <= n:
            number = int(input("请输入您想购买的数目:"))
            if number>=1:
                sum += price[select] * number
                num[select] += number
                buyGoods.add(select)
                print(buyGoods)
        elif select == n+1:
            if len(buyGoods)!=0 and per!=2:
                sum+=pushBuy(buyGoods,allUserBuyInfoGoodsId,menu,price,num)
                buyGoods.clear()
            if sum==0:
                print('\n您的购物车为空!\n')
                continue
            flag = False
            userVipN='无'
            print("---------------------------------------------")
            isV = input("请问您是VIP嘛？(yes/no):")
            if isV == 'yes':
                flag,userVipN= useVipCard(userVipID,userVipN)
            else:
                regVipInfo(userVipID)
            printUserBuyInfo(flag,userVipN, num, menu, price, allUserBuyInfo, sum,allUserBuyInfoGoodsId)

            print('\n')
            sum = 0
            per=2
        elif select == n+2:
            if sum != 0:
                print('\n您还有物品未结账！\n')
            else:
                print('\n欢迎下次光临！！\n')
                break
        else:
            print("Woops! 我们只售卖以上五种商品哦！新货品敬请期待！")
    count += 1
    return count



def adFeatures(userVipID,allUserBuyInfo):
    while 1:
        printAdMenu()
        select = int(input('请输入选项:'))
        if select==1:
            for i,j in userVipID.items():
                print('手机号：',j,'\t卡号:',i)
        elif select==2:
            for i in allUserBuyInfo:
                print(i)
        elif select == 3:
            regVipInfo(userVipID)
        elif select == 4:
            LogoutVipInfo(userVipID)
        elif select == 5:
            break
        else:
            print('输入有误，请重新输入！')



def main():
    price = [1500, 8, 12, 15, 500, 1000]
    menu = ['周杰伦演唱会票', '超土豪咖啡', '宇宙无敌大榴莲', '自动翻译笔记本', '科比签名篮球', '路飞草帽']
    num = [0, 0, 0, 0, 0, 0]
    userVipID = {}
    allUserBuyInfo = []
    vipPath='D:\\vip.txt'
    buyInfoPath = 'D:\\buyInfo.txt'
    with open(vipPath,'r') as f:
        for line in f:
            i,j=line.rstrip().split(',')
            userVipID[i]=j
    f.close()
    # with open(buyInfoPath,'a') as f:
    #     for id,tel in userVipID:
    #         f.write(id+','+tel)
    with open(buyInfoPath,'r') as f:
        for line in f:
            temp=line.rstrip().split(',')
            allUserBuyInfo.append(temp)
    f.close()

    allUserBuyInfoGoodsId=[]
    count = 1
    n=5
    while 1:
        printMenu()
        selNum = int(input('请输入您想进入的系统：'))
        if selNum == 1:
            count=userFeatures(count,n,price, userVipID, num, menu, allUserBuyInfo,allUserBuyInfoGoodsId)
        elif selNum == 2:
            adFeatures(userVipID,allUserBuyInfo)
        elif selNum == 3:
            break
        else:
            print('输入有误，请重新输入！')



if __name__ == '__main__':
    main()