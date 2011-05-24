#!/usr/bin/python
#Author:xudifsd; Time:2009/11/18; License:GPLv3; Version:2.02 Alpha
#Define function
import cPickle as cp
import sys
def Judge():
    global wrong
    if a1<0 or a1>=15 or a2<0 or a2>=15:
            print'Wrong input!'
            wrong=1
    elif pool[a1][a2]!=0:
            print'This position has been occupanted!'
            wrong=2
def Pass():
#across calculate
    global store
    if a2<4:
        for i in range(0,a2+1):
            store[1]=pool[a1][i]
            store[2]=pool[a1][i+1]
            store[3]=pool[a1][i+2]
            store[4]=pool[a1][i+3]
            store[5]=pool[a1][i+4]
            Calculate()
    elif a2>10:
        for i in range(a2-4,11):
            store[1]=pool[a1][i]
            store[2]=pool[a1][i+1]
            store[3]=pool[a1][i+2]
            store[4]=pool[a1][i+3]
            store[5]=pool[a1][i+4]
            Calculate()
    else:
        for i in range(a2-4,a2+1):
            store[1]=pool[a1][i]
            store[2]=pool[a1][i+1]
            store[3]=pool[a1][i+2]
            store[4]=pool[a1][i+3]
            store[5]=pool[a1][i+4]
            Calculate()
#vertical calculate
    if a1<4:
        for i in range(0,a1+1):
            store[1]=pool[i][a2]
            store[2]=pool[i+1][a2]
            store[3]=pool[i+2][a2]
            store[4]=pool[i+3][a2]
            store[5]=pool[i+4][a2]
            Calculate()
    elif a1>10:
        for i in range(a1-4,11):
            store[1]=pool[i][a2]
            store[2]=pool[i+1][a2]
            store[3]=pool[i+2][a2]
            store[4]=pool[i+3][a2]
            store[5]=pool[i+4][a2]
            Calculate()
    else:
        for i in range(a1-4,a1+1):
            store[1]=pool[i][a2]
            store[2]=pool[i+1][a2]
            store[3]=pool[i+2][a2]
            store[4]=pool[i+3][a2]
            store[5]=pool[i+4][a2]
            Calculate()
#left slanting
    if a2<4:
        if a1<4:
            if a1>a2:
                for i in range(a1-a2,a1+1):
                    store[1]=pool[i][i-a1+a2]
                    store[2]=pool[i+1][i-a1+a2+1]
                    store[3]=pool[i+2][i-a1+a2+2]
                    store[4]=pool[i+3][i-a1+a2+3]
                    store[5]=pool[i+4][i-a1+a2+4]
                    Calculate()
            elif a2>a1:
                for i in range(a2-a1,a2+1):
                    store[1]=pool[i-a2+a1][i]
                    store[2]=pool[i-a2+a1+1][i+1]
                    store[3]=pool[i-a2+a1+2][i+2]
                    store[4]=pool[i-a2+a1+3][i+3]
                    store[5]=pool[i-a2+a1+4][i+4]
                    Calculate()
            else:
                for i in range(0,a1+1):
                    store[1]=pool[i][i]
                    store[2]=pool[i+1][i+1]
                    store[3]=pool[i+2][i+2]
                    store[4]=pool[i+3][i+3]
                    store[5]=pool[i+4][i+4]
                    Calculate()
        elif a1>10:
            if a1==a2+10:
                store[1]=pool[10][0]
                store[2]=pool[11][1]
                store[3]=pool[12][2]
                store[4]=pool[13][3]
                store[5]=pool[14][4]
                Calculate()
            elif a1<a2+10:
                for i in range(a1-a2,11):
                    store[1]=pool[i][i-a1+a2]
                    store[2]=pool[i+1][i-a1+a2+1]
                    store[3]=pool[i+2][i-a1+a2+2]
                    store[4]=pool[i+3][i-a1+a2+3]
                    store[5]=pool[i+4][i-a1+a2+4]
                    Calculate()
        else:
            for i in range(a1-a2,a1+1):
                store[1]=pool[i][i-a1+a2]
                store[2]=pool[i+1][i-a1+a2+1]
                store[3]=pool[i+2][i-a1+a2+2]
                store[4]=pool[i+3][i-a1+a2+3]
                store[5]=pool[i+4][i-a1+a2+4]
                Calculate()
    elif a2>10:
        if a1<4:
            if a2-10<=a1:
                for i in range(a2-a1,11):
                    store[1]=pool[i-a2+a1][i]
                    store[2]=pool[i-a2+a1+1][i+1]
                    store[3]=pool[i-a2+a1+2][i+2]
                    store[4]=pool[i-a2+a1+3][i+3]
                    store[5]=pool[i-a2+a1+4][i+4]
                    Calculate()
        elif a1>10:
            if a2>a1:
                for i in range(a2-a1+8,11):
                    store[1]=pool[i-a2+a1][i]
                    store[2]=pool[i-a2+a1+1][i+1]
                    store[3]=pool[i-a2+a1+2][i+2]
                    store[4]=pool[i-a2+a1+3][i+3]
                    store[5]=pool[i-a2+a1+4][i+4]
                    Calculate()
            elif a1==a2:
                for i in range(a1-4,11):
                    store[1]=pool[i][i]
                    store[2]=pool[i+1][i+1]
                    store[3]=pool[i+2][i+2]
                    store[4]=pool[i+3][i+3]
                    store[5]=pool[i+4][i+4]
                    Calculate()
            else:
                for i in range(a1-4,11):
                    store[1]=pool[i][i-a1+a2]
                    store[2]=pool[i+1][i-a1+a2+1]
                    store[3]=pool[i+2][i-a1+a2+2]
                    store[4]=pool[i+3][i-a1+a2+3]
                    store[5]=pool[i+4][i-a1+a2+4]
                    Calculate()
        else:#a2>10 and 3<a1<11
            for i in range(a2-4,11):
                    store[1]=pool[i-a2+a1][i]
                    store[2]=pool[i-a2+a1+1][i+1]
                    store[3]=pool[i-a2+a1+2][i+2]
                    store[4]=pool[i-a2+a1+3][i+3]
                    store[5]=pool[i-a2+a1+4][i+4]
                    Calculate()
    else:#a<=a2<=10
        if a1<4:
            for i in range(0,a1+1):
                store[1]=pool[i][i+a2-a1]
                store[2]=pool[i+1][i+a2-a1+1]
                store[3]=pool[i+2][i+a2-a1+2]
                store[4]=pool[i+3][i+a2-a1+3]
                store[5]=pool[i+4][i+a2-a1+4]
                Calculate()
        elif a1>10:#4<=a2<=10
            for i in range(a1-4,11):
                store[1]=pool[i][i-a1+a2]
                store[2]=pool[i+1][i-a1+a2+1]
                store[3]=pool[i+2][i-a1+a2+2]
                store[4]=pool[i+3][i-a1+a2+3]
                store[5]=pool[i+4][i-a1+a2+4]
                Calculate()
        else:
            for i in range(a1-4,a1+1):
                store[1]=pool[i][i-a1+a2]
                store[2]=pool[i+1][i-a1+a2+1]
                store[3]=pool[i+2][i-a1+a2+2]
                store[4]=pool[i+3][i-a1+a2+3]
                store[5]=pool[i+4][i-a1+a2+4]
                Calculate()
#right slanting
    if 4<=a2<=10:
        if 4<=a1<=10:
            for i in range(a2-4,a2+1):#1
                store[1]=pool[a1+a2-i][i]
                store[2]=pool[a1+a2-i-1][i+1]
                store[3]=pool[a1+a2-i-2][i+2]
                store[4]=pool[a1+a2-i-3][i+3]
                store[5]=pool[a1+a2-i-4][i+4]
                Calculate()
    if a2<4:
        if 4<=a1+a2<=14:
            if a1>3:
                for i in range(0,a2+1):#2
                    store[1]=pool[a1+a2-i][i]
                    store[2]=pool[a1+a2-i-1][i+1]
                    store[3]=pool[a1+a2-i-2][i+2]
                    store[4]=pool[a1+a2-i-3][i+3]
                    store[5]=pool[a1+a2-i-4][i+4]
                    Calculate()
    if a1>10:
        if 15<=a1+a2<=24:
            if a2<11:
                for i in range(a1,15):#3
                    store[1]=pool[i][a1+a2-i]
                    store[2]=pool[i-1][a1+a2-i+1]
                    store[3]=pool[i-2][a1+a2-i+2]
                    store[4]=pool[i-3][a1+a2-i+3]
                    store[5]=pool[i-4][a1+a2-i+4]
                    Calculate()
    if a2>10:
        if 15<=a1+a2<=24:
            if a1<11:
                for i in range(a2-4,11):#4
                    store[1]=pool[a1+a2-i][i]
                    store[2]=pool[a1+a2-i-1][i+1]
                    store[3]=pool[a1+a2-i-2][i+2]
                    store[4]=pool[a1+a2-i-3][i+3]
                    store[5]=pool[a1+a2-i-4][i+4]
                    Calculate()
    if a1<4:
        if 4<=a1+a2<=14:
            if a2>3:
                for i in range(4,a1+5):#5
                    store[1]=pool[i][a1+a2-i]
                    store[2]=pool[i-1][a1+a2-i+1]
                    store[3]=pool[i-2][a1+a2-i+2]
                    store[4]=pool[i-3][a1+a2-i+3]
                    store[5]=pool[i-4][a1+a2-i+4]
                    Calculate()
    if a1<4 and a2<4:
        if 4<=a1+a2<=6:
            for i in range(0,a1+a2-3):#6
                store[1]=pool[a1+a2-i][i]
                store[2]=pool[a1+a2-i-1][i+1]
                store[3]=pool[a1+a2-i-2][i+2]
                store[4]=pool[a1+a2-i-3][i+3]
                store[5]=pool[a1+a2-i-4][i+4]
                Calculate()
    if a1>10 and a2>10:
        if 22<=a1+a2<=24:
            for i in range(a1+a2-14,11):#7
                store[1]=pool[a1+a2-i][i]
                store[2]=pool[a1+a2-i-1][i+1]
                store[3]=pool[a1+a2-i-2][i+2]
                store[4]=pool[a1+a2-i-3][i+3]
                store[5]=pool[a1+a2-i-4][i+4]
                Calculate()
def Calculate():
    global winer
    if store[1]==store[2]==store[3]==store[4]==store[5]==1:
        winer=1
    elif store[1]==store[2]==store[3]==store[4]==store[5]==2:
        winer=2
def GUI():
    sys.stdout.write('  ')
    for firstline in range(1,16):
        if firstline<10:
            sys.stdout.write('|%d '%firstline)
        else:
            sys.stdout.write('|%d'%firstline)
    print'\n',
    for upright in range(0,15):
        if upright<9:
            sys.stdout.write('%d '%(upright+1))
        else:
            sys.stdout.write('%d'%(upright+1))
        for across in range(0,15):
            sys.stdout.write('|_%s'%symbol[upright][across])
            if across==14:
                print'\n',
def Console():
    while True:
        try:
            x=raw_input("Now you are in the console,input 'wq' for save game and quit,input 'q' for quit whitout save game,input 'r' for return game:\n")
        except:
            print"Wrong input,you can only input 'wq','q'and'r'!"
        else:
            if x in ['wq','WQ']:
                f=file('save.txt','w')
                cp.dump(pool,f)
                cp.dump(symbol,f)
                cp.dump(player,f)
                sys.exit()
            elif x in ['q','Q']:
                sys.exit()
            elif x in ['r','R']:
                break
            else:
                print"Wrong input! You can only input 'wq','q'and'r'!"
#Main
print'This is the Five Points Chess!'
print"Version:2.02 Alpha This program'license is GPL,you can visit http://www.gnu.org for more information."
print'First player is represent by "*",and second player is represent by "#"'
print'Author is xudifsd,you can contract with him by E-mail address:"xudifsd@gmail.com"'
#clean game pool
a=[];b=[];pool=[];symbol=[]
for times in range(1,16):
    a.append(0)
for times in range(1,16):
    pool.append(a[:])
for times in range(1,16):
    b.append('_')
for times in range(1,16):
    symbol.append(b[:])
#inital
wrong=0
winer=0
store=[0,0,0,0,0,0]
player=0
#test and load save
try:
    f=file('save.txt')
except IOError:
    save=0
else:
    while True:
        try:
            c=raw_input('There seem to have a save file,do you want to load them?(y/n)\n')
        except:
            print"Wrong input,you can only input 'y'and'n'!"
        else:
            if c in ['y','Y']:
                pool=cp.load(f)
                symbol=cp.load(f)
                player=cp.load(f)
                break
            elif c in ['n','N']:
                break
            else:
                print"You can only input 'y' and 'n'!"
                continue
#main
while True:
    while player==0:
        GUI()
        player=1
    while player==1:
        wrong=0
        while True:
            try:
                a1=int(raw_input('First Player,First Coordinat:\n'))
                a2=int(raw_input('First Player,Second Coordinat:\n'))
            except ValueError:
                Console()
                continue
            except:
                print'Wrong input!'
            else:
                break
        a1=a1-1;a2=a2-1
        Judge()
        if wrong!=0:
            continue
        pool[a1][a2]=1
        symbol[a1][a2]='*'
        Pass()
        if winer!=0:
            break
        GUI()
        player=2
    if winer!=0:
        break
    while player==2:
        wrong=0
        while True:
            try:
                a1=int(raw_input('Scond Player,First Coordinat:\n'))
                a2=int(raw_input('Scond Player,Second Coordinat:\n'))
            except ValueError:
                Console()
                continue
            except:
                print'Wrong input!'
            else:
                break
        a1=a1-1;a2=a2-1
        Judge()
        if wrong!=0:
            continue
        pool[a1][a2]=2
        symbol[a1][a2]='#'
        Pass()
        if winer!=0:
            break
        GUI()
        player=1
    if winer!=0:
        break
if winer==1 :
    print'Winer is First Player!'
else:
    print'Winer is Second Player!'