# Work with Python 3.6
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound

import random
import sqlite3
from sqlite3 import Error
import datetime
import time
import os.path
import requests
from asyncio import sleep
from bs4 import BeautifulSoup
#pip install requests

# 133105ccf6f146d9a907130e03820b72984c8ba71c7ed9191c235be0622a022a
fileLocation="C:\\Users\\mauri\\Downloads\\UpdatedProject_rar\\SqliteConnection\\db\\diceBot-Config.txt"
min = 0
max = 100
addFaucet=100
TOKEN = 'NzEyMTMzOTE3MzI2NzA0ODMx.XsNI4Q.HC8s-usAaGS5iT3regav-u_88lY'
#TOKEN = 'NzA5NDUwMDA0MzM0Mzc5MDA5.XrmF2A.NO7wBVbJgDBc_Bj1FQT_gHUYpIE'
file = open(fileLocation,"r")
database=file.readline()
tokens=database.split("=")
database = tokens[1][:-1]
file.readline()
temp=file.readline()
tokens=temp.split("=")
faucet=tokens[1]
addFaucet=int(faucet)
file.close()
client = commands.Bot(command_prefix='!')

def getBalance(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT bal FROM Balances WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = float(str(row).replace('(', '').replace(')', '').replace(',', '').replace("'",""))
        return temp
    except Error as e:
        print(e)

def isUserExists(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Balances WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        if len(rows)>0:
            return True
        return False
    except Error as e:
        print(e)

def istokenExists(token):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM creditdeposit WHERE token = ?", (token,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        if len(rows)>0:
            return True
        return False
    except Error as e:
        print(e)

def getIdFromCreditDeposit(token):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT uid FROM creditdeposit WHERE token = ?", (token,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
        return temp
    except Error as e:
        print(e)

def insertCredit(id,token):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into creditdeposit(uid,token) VALUES(?,?)",(id,token))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)

def insertUser(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into Balances(uid,bal) VALUES(?,?)",(id,0))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)

def getHistory(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Bets WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = ""
        list=[]
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
            list.append(temp)
        return list
    except Error as e:
        print(e)

def getidFromBets():
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT distinct uid FROM Bets")
        conn.commit()
        rows = cur.fetchall()
        temp = ""
        list=[]
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
            list.append(temp)
        return list
    except Error as e:
        print(e)

def isFloat(ans1):
    try:
        float(ans1)
    except:
        return False
    return True

def updateBalance(id,bal):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("UPDATE Balances SET bal = ? WHERE uid = ?", (bal, id))
        conn.commit()
    except Error as e:
        print(e)

def readResponse(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT response FROM Responses WHERE requestid = ?", (id,))
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = str(row).replace(',','').replace('(','').replace(')','').replace('\'','')
            print(temp)
        return temp
    except Error as e:
        print(e)

def deleteRequest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("UPDATE Requests SET deleteyesorno = ? WHERE requestid = ?", ("y", id))
        conn.commit()
    except Error as e:
        print(e)

def sendRequest(id,com):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into Requests(requestid,requestcommand,deleteyesorno) VALUES(?,?,?)",(str(id),str(com),"n"))
        conn.commit()
        print("row ",cur.lastrowid)
        return cur.lastrowid
    except Error as e:
        print(e)

def isFaucetExists(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM faucet WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        if len(rows)>0:
            return True
        return False
    except Error as e:
        print(e)

def insertFaucetTime(id,currentTime):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into faucet(uid,faucettime) VALUES(?,?)",(id,currentTime))
        conn.commit()
        print("row ",cur.lastrowid)
        return cur.lastrowid
    except Error as e:
        print(e)

def updateFaucetTime(id,currentTime):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("UPDATE faucet SET faucettime = ? WHERE uid = ?", (currentTime, id))
        conn.commit()
    except Error as e:
        print(e)

def getFaucetTime(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT faucettime FROM faucet WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
        return temp
    except Error as e:
        print(e)

def removeBetsOfRemovedUser(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("DELETE FROM Bets WHERE uid = ?", (id,))
        conn.commit()
    except Error as e:
        print(e)

#----------------------------------Test Functions------------------------------
def getBalanceTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT bal FROM testBalances WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = float(str(row).replace('(', '').replace(')', '').replace(',', '').replace("'",""))
        return temp
    except Error as e:
        print(e)

def isUserExistsTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM testBalances WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        if len(rows)>0:
            return True
        return False
    except Error as e:
        print(e)

def istokenExistsTest(token):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM testcreditdeposit WHERE token = ?", (token,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        if len(rows)>0:
            return True
        return False
    except Error as e:
        print(e)

def getIdFromCreditDepositTest(token):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT uid FROM testcreditdeposit WHERE token = ?", (token,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
        return temp
    except Error as e:
        print(e)

def insertCreditTest(id,token):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into testcreditdeposit(uid,token) VALUES(?,?)",(id,token))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)

def insertUserTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into testBalances(uid,bal) VALUES(?,?)",(id,0))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)

def getHistoryTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM testBets WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = ""
        list=[]
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
            list.append(temp)
        return list
    except Error as e:
        print(e)

def getidFromBetsTest():
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT distinct uid FROM testBets")
        conn.commit()
        rows = cur.fetchall()
        temp = ""
        list=[]
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
            list.append(temp)
        return list
    except Error as e:
        print(e)

def updateBalanceTest(id,bal):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("UPDATE testBalances SET bal = ? WHERE uid = ?", (bal, id))
        conn.commit()
    except Error as e:
        print(e)

def readResponseTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT response FROM testResponses WHERE requestid = ?", (id,))
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = str(row).replace(',','').replace('(','').replace(')','').replace('\'','')
            print(temp)
        return temp
    except Error as e:
        print(e)

def deleteRequestTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("UPDATE testRequests SET deleteyesorno = ? WHERE requestid = ?", ("y", id))
        conn.commit()
    except Error as e:
        print(e)

def sendRequestTest(id,com):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into testRequests(requestid,requestcommand,deleteyesorno) VALUES(?,?,?)",(str(id),str(com),"n"))
        conn.commit()
        print("row ",cur.lastrowid)
        return cur.lastrowid
    except Error as e:
        print(e)

def isFaucetExistsTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT * FROM testfaucet WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        if len(rows)>0:
            return True
        return False
    except Error as e:
        print(e)

def insertFaucetTimeTest(id,currentTime):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("Insert into testfaucet(uid,faucettime) VALUES(?,?)",(id,currentTime))
        conn.commit()
        print("row ",cur.lastrowid)
        return cur.lastrowid
    except Error as e:
        print(e)

def updateFaucetTimeTest(id,currentTime):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("UPDATE testfaucet SET faucettime = ? WHERE uid = ?", (currentTime, id))
        conn.commit()
    except Error as e:
        print(e)

def getFaucetTimeTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("SELECT faucettime FROM testfaucet WHERE uid = ?", (id,))
        conn.commit()
        rows = cur.fetchall()
        temp = None
        for row in rows:
            temp = str(row).replace('(', '').replace(')', '').replace(',', '').replace("'","")
        return temp
    except Error as e:
        print(e)

def removeBetsOfRemovedUserTest(id):
    conn = None
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("DELETE FROM testBets WHERE uid = ?", (id,))
        conn.commit()
    except Error as e:
        print(e)



@client.command()
async def hello(ctx):
    channel = ctx.message
    msg = 'Hello {0.author.name}'.format(ctx.message)
    await ctx.send(msg)

@client.command()
async def roll(ctx,*args):
    if len(args)!=2:
        print("Please enter valid number of arguments (only 2)")
        await ctx.send("Please enter valid number of arguments (only 2)")
        return
    if isFloat(args[0]) and isFloat(args[1]):
        if str(args[0]).find('.')!=-1 and len(str(args[0]).split('.')[1])>2:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 2)")
            return
        if str(args[1]).find('.') != -1 and len(str(args[1]).split('.')[1]) > 8:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 8)")
            return
        if float(args[1]) <= 0.0:
            print("2nd argument is not in valid range( it should be greater than zero)")
            await ctx.send("2nd argument is not in valid range( it should be greater than zero)")
            return
        if float(args[0]) < 0.0 or float(args[0]) > 100.0:
            print("1st argument is not in valid range( it should be between 0 and 100)")
            await ctx.send("1st argument is not in valid range( it should be between 0 and 100)")
            return
        else:
            amount=getBalance(ctx.message.author.id)
            print(ctx.message.author.id)
            print(amount)
            if amount>=float(args[1]):
                print("true")
                comm="!roll "+str(float(args[0]))+" "+str(float(args[1]))
                currentDT = datetime.datetime.now()
                sec = str(currentDT.year).zfill(2) + str(currentDT.month).zfill(2) + str(currentDT.day).zfill(2) + str(currentDT.hour).zfill(2) + str(currentDT.minute).zfill(2) + str(currentDT.second).zfill(2)
                uid=str(ctx.message.author.id)+"-"+str(sec)
                w=sendRequest(uid,comm)
                print("response", w)
                await sleep(1)
                response=readResponse(uid)
                print("response",response)
                await ctx.send(str(response))
                deleteRequest(uid)
            else:
                print("You do not have enough balance to place this bet. YOur current balance is",amount)
                await ctx.send("You donot have enough balance to place this bet. Your current balance is"+str(amount))
                return
    else:
        print("Please enter valid digits(integers only)")
        await ctx.send("Please enter valid digits(integers only)")
        return

@client.command()
async def balance(ctx):
    theirBalance = getBalance(ctx.message.author.id)
    msg = ctx.message.author.name + '! You currently have an Acc Balance of ' + str(theirBalance) + ' !'
    await ctx.send(msg)

@client.command()
async def again(ctx):
    updateBalance(ctx.message.author.id,1000)
    print('yeah', ctx.message.author.name ,'you got back your 1000 coins')
    await ctx.send('yeah '+ ctx.message.author.name +', you got back your 1000 coins')

@client.command()
async def deposit(ctx):
    if os.path.exists("shuffleAddresses.TRY.AGAIN.LATER.txt"):
        await ctx.send('Please try again later')
        return
    myFile = open("shuffleAddresses.yes.txt", "w")
    myFile.close()
    await sleep(1);
    fileToRead = open("addresses-text.txt", "r")
    with open("addresses-text.txt") as f:
        content = f.readlines()
    fileToRead.close()
    os.remove("shuffleAddresses.yes.txt")
    os.remove("shuffleAddresses.TRY.AGAIN.LATER.txt")
    content = [x.strip() for x in content]
    msg=""
    for i in range(0,len(content)):
        msg=msg+str(content[i])+"\n"
    await ctx.send(msg+"please deposit dogecoin to this address and return back here with the transaction id & pass it along to the !creditdeposit command :  !creditdeposit TXN-NUMBER HERE")

@client.command()
async def creditdeposit(ctx,*args):
    if len(args)!=1:
        print("Please enter valid number of arguments (only 1)")
        await ctx.send("Please enter valid number of arguments (only 1)")
        return
    URL = "https://dogechain.info/rawtx/"+str(args[0])
    response = requests.get(URL)
    if response.status_code != 200:
        await ctx.send("Please enter valid token number")
        return
    jsonResponse = response.json()
    success=jsonResponse["success"]
    if success==0:
        await ctx.send("Please enter valid token number")
        return

    with open("addresses-text2.txt") as f:
        addresses = f.readlines()
    addresses = [x.strip() for x in addresses]
    f.close()
    flag=False
    response = requests.get(URL)
    jsonResponse = response.json()
    transaction = jsonResponse["transaction"]
    outputList = transaction["outputs"]
    outputs = outputList[0]
    validAddress = outputs["address"]
    print(validAddress)

    for i in range(0, len(addresses)):
        if addresses[i]==validAddress:
            flag=True
            break
    if not flag:
        await ctx.send("The address is not valid")
        return

    if istokenExists(str(args[0])):
        uid=getIdFromCreditDeposit(args[0])
        allUsers=client.users
        for i in range(0,len(allUsers)):
            if str(allUsers[i].id)==str(uid):
                name=allUsers[i].name
                break
        await ctx.send("Sorry! " +str(name)+ " has already got credit for this deposit.")
        return
    for i in range(0,25):
        response = requests.get(URL)
        jsonResponse = response.json()
        transaction = jsonResponse["transaction"]
        confirm=transaction["confirmations"]
        print("confirm =",confirm)
        if confirm<10:
            print("waiting in loop "+ str(i)+" for verification "+str(ctx.message.author.id))
            if i==0:
                await ctx.send("Your balance will be updated after verification")
            await sleep(60)
        else:
            break
    if confirm>=10:
        outputList = transaction["outputs"]
        outputs=outputList[0]
        value=outputs["value"]
        print(value)
        updateAmount=float(getBalance(ctx.message.author.id))+float(value)
        print(updateAmount)
        updateBalance(ctx.message.author.id,updateAmount)
        insertCredit(ctx.message.author.id,args[0])
        await ctx.send("Your balance has been updated with "+str(value)+". Your new balance is " +str(updateAmount))
    else:
        print("Balance not updated")

@client.command()
async def tip(ctx,*args):
    if len(args) != 2:
        print("Please enter valid number of arguments (only 2)")
        await ctx.send("Please enter valid number of arguments (only 2)")
        return
    if isFloat(args[1]):
        if str(args[1]).find('.') != -1 and len(str(args[1]).split('.')[1]) > 8:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 8)")
            return
        if float(args[1]) <= 0.0:
            print("2nd argument is not in valid range( it should be greater than zero)")
            await ctx.send("2nd argument is not in valid range( it should be greater than zero)")
            return
        # check here if username exists
        allUsers = client.users

        flag=False
        for i in range(0, len(allUsers)):
            if str(allUsers[i].name).lower()==str(args[0].lower()):
                flag=True
                name=allUsers[i].name
                id=allUsers[i].id
                break
        if not flag:
            await ctx.send("User with this name does not exist")
            return
        if float(getBalance(ctx.message.author.id))<float(args[1]):
            await ctx.send("Sorry you do not have enough balance to give tip")
            return
        tip=float(args[1])
        updateBalance(id,getBalance(id)+tip)
        updateBalance(ctx.message.author.id, getBalance(ctx.message.author.id) - tip)
        await ctx.send("Your tip has been granted successfully. Your new balance is "+ str(getBalance(ctx.message.author.id)))
    else:
        print("Please enter valid digits(numbers only)")
        await ctx.send("Please enter valid digits(numbers only) in 2nd argument")
        return

@client.command()
async def rain(ctx,*args):
    if len(args) != 2:
        print("Please enter valid number of arguments (only 2)")
        await ctx.send("Please enter valid number of arguments (only 2)")
        return
    if isFloat(args[0]) and isFloat(args[1]):
        if str(args[0]).find('.') != -1:
            await ctx.send("Please enter valid argument(only integers allowed in first argument)")
            return
        if str(args[1]).find('.') != -1 and len(str(args[1]).split('.')[1]) > 8:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 8)")
            return
        if float(args[1]) <= 0.0:
            print("2nd argument is not in valid range( it should be greater than zero)")
            await ctx.send("2nd argument is not in valid range( it should be greater than zero)")
            return
        if float(args[0]) <= 0.0:
            print("1st argument is not in valid range( it should be greater than zero)")
            await ctx.send("1st argument is not in valid range( it should be greater than zero)")
            return
        if getBalance(ctx.message.author.id)<float(args[1]):
            print("You have not enough balance to run this command")
            await ctx.send("You have not enough balance to run this command")
            return
        else:
            amountToDistribute=float(args[1])
            usersToDistribute = float(args[0])
            list=getidFromBets()
            allUsers=client.users
            for i in range(0,len(list)):
                flag=False
                for j in range(0,len(allUsers)):
                    if str(list[i])==str(allUsers[j].id):
                        flag=True
                        break
                if flag==False:
                    removeBetsOfRemovedUser(list[i])
            list = getidFromBets()
            for i in range(0, len(list)):
                if str(list[i])==str(ctx.message.author.id):
                    list.pop(i)
                    break
            if len(list)>usersToDistribute:
                while True:
                    indexToRemove = random.randint(0, len(list)-1)
                    list.pop(indexToRemove)
                    if len(list)==usersToDistribute:
                        break
            if len(list) == 0:
                await ctx.send("There is no user in bets table to distribute amount!")
                return
            nameList=[]
            count=0
            for i in range(0, len(list)):
                for j in range(0,len(allUsers)):
                    if str(list[i])==str(allUsers[j].id):
                        nameList.insert(count,str(allUsers[j].name))
                        count=count+1
            actualUsers=len(list)
            amountPerhead=amountToDistribute/actualUsers
            amountUpdate = getBalance(ctx.message.author.id)-amountToDistribute
            updateBalance(ctx.message.author.id,amountUpdate)
            msg="Congrats! The following "+str(actualUsers) +" randomly selected Users have received "+ str(amountPerhead)+ " free coins from "+ ctx.message.author.name +"\n"
            for i in range(0, len(list)):
                amountUpdate = getBalance(list[i]) + amountPerhead
                updateBalance(list[i],amountUpdate)
                msg=msg+str(nameList[i])+"\n"
            await ctx.send(msg)
            print(msg)

@client.command()
async def faucet(ctx):
    if(isFaucetExists(ctx.message.author.id)==False):
        bal=getBalance(ctx.message.author.id)
        updateBalance(ctx.message.author.id,bal+addFaucet)
        newbalance=getBalance(ctx.message.author.id)
        msg='yeah '+ ctx.message.author.name+ '! You received a faucet of '+ str(addFaucet)+ ' coins. Your new Balance is '+ str(newbalance)
        print(msg)
        await ctx.send(msg)
        currentDT = datetime.datetime.now()
        insertFaucetTime(ctx.message.author.id,str(currentDT))
    else:
        string=getFaucetTime(ctx.message.author.id)
        year=int(string[:4])
        month =int( string[5:7])
        day = int(string[8:10])
        #print(year,month,day)

        hour = int(string[11:13])
        minute = int(string[14:16])
        second = int(string[17:19])
        #print(hour, minute, second)

        currdate = datetime.datetime.now()
        prevdate=datetime.datetime(year, month, day,hour,minute,second)
        #print("prev before hour", str(prevdate))

        prevdate=prevdate+datetime.timedelta(seconds=3600)

        #print("after hour",str(prevdate))
        #print("current date", str(currdate))

        flag=currdate > prevdate
        #print("flag", flag)
        if flag:
            bal = getBalance(ctx.message.author.id)
            updateBalance(ctx.message.author.id, bal + addFaucet)
            newbalance = getBalance(ctx.message.author.id)
            msg = 'yeah ' + ctx.message.author.name + '! You received a faucet of ' + str(
                addFaucet) + ' coins. Your new Balance is ' + str(newbalance)
            print(msg)
            currentDT = datetime.datetime.now()
            updateFaucetTime(ctx.message.author.id, str(currentDT))
            await ctx.send(msg)
        else:
            msg="Sorry! You can make only 1 faucet request in 1 hour"
            print("msg", msg)
            await ctx.send(msg)

@client.command()
async def history(ctx):
    list=getHistory(ctx.message.author.id)
    msg = ""
    if len(list)==0:
        await ctx.send("No bets to display")

    for i in range(0,len(list)):
        if len(list)-i<=5:
            msg=msg+"Bet # "+ str(i+1)+"\n"
            bet=list[i]
            betattributes=bet.split(" ")
            msg=msg+"id = "+betattributes[0]+"\n"
            msg = msg+"WinChance = " + betattributes[1] + "\n"
            msg = msg+"BetAmount = " + betattributes[2] + "\n"
            msg = msg+"Roll Result = " + betattributes[3] + "\n"
            msg = msg+"Result = " + betattributes[4] + "\n"
            if float(betattributes[3])<=float(betattributes[4]):
                msg =msg+ "Profit or loss amount = +" + betattributes[5] + "\n"
            else:
                msg = msg + "Profit or loss amount = -" + betattributes[5] + "\n"
            msg = msg+"Balance = " + betattributes[6] + "\n"
            msg=msg+"------------------------------\n"
    await ctx.send(msg)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Invalid command")
        print("Invalid command")
    else:
        pass

@client.event
async def on_member_join(member):
    flag = isUserExists(member.id)
    if not flag:
        insertUser(member.id)
    print(f'{member} joined server')
    flag = isUserExistsTest(member.id)
    if not flag:
        insertUserTest(member.id)
    print(f'{member} joined server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left server')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    allUsers=client.users
    for i in range(0,len(allUsers)):
        if not isUserExists(str(allUsers[i].id)):
            insertUser(str(allUsers[i].id))
            print("New member added in balances table with id= "+str(allUsers[i].id)+" and name= "+str(allUsers[i].name))

    for i in range(0,len(allUsers)):
        if not isUserExistsTest(str(allUsers[i].id)):
            insertUserTest(str(allUsers[i].id))
            print("New member added in testbalances table with id= "+str(allUsers[i].id)+" and name= "+str(allUsers[i].name))


#----------------------------- Test Commands------------------------------

@client.command()
async def hellotest(ctx):
    channel = ctx.message
    msg = 'Hello {0.author.name}'.format(ctx.message)
    await ctx.send(msg)

@client.command()
async def rolltest(ctx,*args):
    if len(args)!=2:
        print("Please enter valid number of arguments (only 2)")
        await ctx.send("Please enter valid number of arguments (only 2)")
        return
    if isFloat(args[0]) and isFloat(args[1]):
        if str(args[0]).find('.')!=-1 and len(str(args[0]).split('.')[1])>2:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 2)")
            return
        if str(args[1]).find('.') != -1 and len(str(args[1]).split('.')[1]) > 8:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 8)")
            return
        if float(args[1]) <= 0.0:
            print("2nd argument is not in valid range( it should be greater than zero)")
            await ctx.send("2nd argument is not in valid range( it should be greater than zero)")
            return
        if float(args[0]) < 0.0 or float(args[0]) > 100.0:
            print("1st argument is not in valid range( it should be between 0 and 100)")
            await ctx.send("1st argument is not in valid range( it should be between 0 and 100)")
            return
        else:
            amount=getBalanceTest(ctx.message.author.id)
            print(ctx.message.author.id)
            print(amount)
            if amount>=float(args[1]):
                print("true")
                comm="!roll "+str(float(args[0]))+" "+str(float(args[1]))
                currentDT = datetime.datetime.now()
                sec = str(currentDT.year).zfill(2) + str(currentDT.month).zfill(2) + str(currentDT.day).zfill(2) + str(currentDT.hour).zfill(2) + str(currentDT.minute).zfill(2) + str(currentDT.second).zfill(2)
                uid=str(ctx.message.author.id)+"-"+str(sec)
                w=sendRequestTest(uid,comm)
                print("response", w)
                await sleep(1)
                response=readResponseTest(uid)
                print("response",response)
                await ctx.send(str(response))
                deleteRequestTest(uid)
            else:
                print("You do not have enough balance to place this bet. YOur current balance is",amount)
                await ctx.send("You donot have enough balance to place this bet. Your current balance is"+str(amount))
                return
    else:
        print("Please enter valid digits(integers only)")
        await ctx.send("Please enter valid digits(integers only)")
        return

@client.command()
async def balancetest(ctx):
    theirBalance = getBalanceTest(ctx.message.author.id)
    msg = ctx.message.author.name + '! You currently have an Acc Balance of ' + str(theirBalance) + ' !'
    await ctx.send(msg)

@client.command()
async def againtest(ctx):
    updateBalanceTest(ctx.message.author.id,1000)
    print('yeah', ctx.message.author.name ,'you got back your 1000 coins')
    await ctx.send('yeah '+ ctx.message.author.name +', you got back your 1000 coins')

@client.command()
async def deposittest(ctx):
    if os.path.exists("shuffleAddresses.TRY.AGAIN.LATER.txt"):
        await ctx.send('Please try again later')
        return
    myFile = open("shuffleAddresses.yes.txt", "w")
    myFile.close()
    await sleep(1);
    fileToRead = open("addresses-text.txt", "r")
    with open("addresses-text.txt") as f:
        content = f.readlines()
    fileToRead.close()
    os.remove("shuffleAddresses.yes.txt")
    os.remove("shuffleAddresses.TRY.AGAIN.LATER.txt")
    content = [x.strip() for x in content]
    msg=""
    for i in range(0,len(content)):
        msg=msg+str(content[i])+"\n"
    await ctx.send(msg+"please deposit dogecoin to this address and return back here with the transaction id & pass it along to the !creditdeposit command :  !creditdeposit TXN-NUMBER HERE")

@client.command()
async def creditdeposittest(ctx,*args):
    if len(args)!=1:
        print("Please enter valid number of arguments (only 1)")
        await ctx.send("Please enter valid number of arguments (only 1)")
        return
    URL = "https://dogechain.info/rawtx/"+str(args[0])
    response = requests.get(URL)
    if response.status_code != 200:
        await ctx.send("Please enter valid token number")
        return
    jsonResponse = response.json()
    success=jsonResponse["success"]
    if success==0:
        await ctx.send("Please enter valid token number")
        return

    with open("addresses-text2.txt") as f:
        addresses = f.readlines()
    addresses = [x.strip() for x in addresses]
    f.close()
    flag=False
    response = requests.get(URL)
    jsonResponse = response.json()
    transaction = jsonResponse["transaction"]
    outputList = transaction["outputs"]
    outputs = outputList[0]
    validAddress = outputs["address"]
    print(validAddress)

    for i in range(0, len(addresses)):
        if addresses[i]==validAddress:
            flag=True
            break
    if not flag:
        await ctx.send("The address is not valid")
        return

    if istokenExistsTest(str(args[0])):
        uid=getIdFromCreditDepositTest(args[0])
        allUsers=client.users
        for i in range(0,len(allUsers)):
            if str(allUsers[i].id)==str(uid):
                name=allUsers[i].name
                break
        await ctx.send("Sorry! " +str(name)+ " has already got credit for this deposit.")
        return
    for i in range(0,25):
        response = requests.get(URL)
        jsonResponse = response.json()
        transaction = jsonResponse["transaction"]
        confirm=transaction["confirmations"]
        print("confirm =",confirm)
        if confirm<10:
            print("waiting in loop "+ str(i)+" for verification "+str(ctx.message.author.id))
            if i==0:
                await ctx.send("Your balance will be updated after verification")
            await sleep(60)
        else:
            break
    if confirm>=10:
        outputList = transaction["outputs"]
        outputs=outputList[0]
        value=outputs["value"]
        print(value)
        updateAmount=float(getBalanceTest(ctx.message.author.id))+float(value)
        print(updateAmount)
        updateBalanceTest(ctx.message.author.id,updateAmount)
        insertCreditTest(ctx.message.author.id,args[0])
        await ctx.send("Your balance has been updated with "+str(value)+". Your new balance is " +str(updateAmount))
    else:
        print("Balance not updated")

@client.command()
async def tiptest(ctx,*args):
    if len(args) != 2:
        print("Please enter valid number of arguments (only 2)")
        await ctx.send("Please enter valid number of arguments (only 2)")
        return
    if isFloat(args[1]):
        if str(args[1]).find('.') != -1 and len(str(args[1]).split('.')[1]) > 8:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 8)")
            return
        if float(args[1]) <= 0.0:
            print("2nd argument is not in valid range( it should be greater than zero)")
            await ctx.send("2nd argument is not in valid range( it should be greater than zero)")
            return
        # check here if username exists
        allUsers = client.users

        flag=False
        for i in range(0, len(allUsers)):
            if str(allUsers[i].name).lower()==str(args[0].lower()):
                flag=True
                name=allUsers[i].name
                id=allUsers[i].id
                break
        if not flag:
            await ctx.send("User with this name does not exist")
            return
        if float(getBalanceTest(ctx.message.author.id))<float(args[1]):
            await ctx.send("Sorry you do not have enough balance to give tip")
            return
        tip=float(args[1])
        updateBalanceTest(id,getBalanceTest(id)+tip)
        updateBalanceTest(ctx.message.author.id, getBalanceTest(ctx.message.author.id) - tip)
        await ctx.send("Your tip has been granted successfully. Your new balance is "+ str(getBalanceTest(ctx.message.author.id)))
    else:
        print("Please enter valid digits(numbers only)")
        await ctx.send("Please enter valid digits(numbers only) in 2nd argument")
        return

@client.command()
async def raintest(ctx,*args):
    if len(args) != 2:
        print("Please enter valid number of arguments (only 2)")
        await ctx.send("Please enter valid number of arguments (only 2)")
        return
    if isFloat(args[0]) and isFloat(args[1]):
        if str(args[0]).find('.') != -1:
            await ctx.send("Please enter valid argument(only integers allowed in first argument)")
            return
        if str(args[1]).find('.') != -1 and len(str(args[1]).split('.')[1]) > 8:
            await ctx.send("Please enter valid number of digits in 2nd argument(only 8)")
            return
        if float(args[1]) <= 0.0:
            print("2nd argument is not in valid range( it should be greater than zero)")
            await ctx.send("2nd argument is not in valid range( it should be greater than zero)")
            return
        if float(args[0]) <= 0.0:
            print("1st argument is not in valid range( it should be greater than zero)")
            await ctx.send("1st argument is not in valid range( it should be greater than zero)")
            return
        if getBalanceTest(ctx.message.author.id)<float(args[1]):
            print("You have not enough balance to run this command")
            await ctx.send("You have not enough balance to run this command")
            return
        else:
            amountToDistribute=float(args[1])
            usersToDistribute = float(args[0])
            list=getidFromBetsTest()
            allUsers=client.users
            for i in range(0,len(list)):
                flag=False
                for j in range(0,len(allUsers)):
                    if str(list[i])==str(allUsers[j].id):
                        flag=True
                        break
                if flag==False:
                    removeBetsOfRemovedUserTest(list[i])
            list = getidFromBetsTest()
            for i in range(0, len(list)):
                if str(list[i])==str(ctx.message.author.id):
                    list.pop(i)
                    break
            if len(list)>usersToDistribute:
                while True:
                    indexToRemove = random.randint(0, len(list)-1)
                    list.pop(indexToRemove)
                    if len(list)==usersToDistribute:
                        break
            if len(list) == 0:
                await ctx.send("There is no user in bets table to distribute amount!")
                return
            nameList=[]
            count=0
            for i in range(0, len(list)):
                for j in range(0,len(allUsers)):
                    if str(list[i])==str(allUsers[j].id):
                        nameList.insert(count,str(allUsers[j].name))
                        count=count+1
            actualUsers=len(list)
            amountPerhead=amountToDistribute/actualUsers
            amountUpdate = getBalanceTest(ctx.message.author.id)-amountToDistribute
            updateBalanceTest(ctx.message.author.id,amountUpdate)
            msg="Congrats! The following "+str(actualUsers) +" randomly selected Users have received "+ str(amountPerhead)+ " free coins from "+ ctx.message.author.name +"\n"
            for i in range(0, len(list)):
                amountUpdate = getBalanceTest(list[i]) + amountPerhead
                updateBalanceTest(list[i],amountUpdate)
                msg=msg+str(nameList[i])+"\n"
            await ctx.send(msg)
            print(msg)

@client.command()
async def faucettest(ctx):
    if(isFaucetExistsTest(ctx.message.author.id)==False):
        print("here1")
        bal=getBalanceTest(ctx.message.author.id)
        print("here1")

        updateBalanceTest(ctx.message.author.id,bal+addFaucet)
        print("here1")

        newbalance=getBalanceTest(ctx.message.author.id)
        print("here1")

        msg='yeah '+ ctx.message.author.name+ '! You received a faucet of '+ str(addFaucet)+ ' coins. Your new Balance is '+ str(newbalance)
        print("here1")

        print(msg)
        await ctx.send(msg)
        currentDT = datetime.datetime.now()
        insertFaucetTimeTest(ctx.message.author.id,str(currentDT))
    else:
        string=getFaucetTimeTest(ctx.message.author.id)
        year=int(string[:4])
        month =int( string[5:7])
        day = int(string[8:10])
        #print(year,month,day)

        hour = int(string[11:13])
        minute = int(string[14:16])
        second = int(string[17:19])
        #print(hour, minute, second)

        currdate = datetime.datetime.now()
        prevdate=datetime.datetime(year, month, day,hour,minute,second)
        #print("prev before hour", str(prevdate))

        prevdate=prevdate+datetime.timedelta(seconds=3600)

        #print("after hour",str(prevdate))
        #print("current date", str(currdate))

        flag=currdate > prevdate
        #print("flag", flag)
        if flag:
            bal = getBalanceTest(ctx.message.author.id)
            updateBalanceTest(ctx.message.author.id, bal + addFaucet)
            newbalance = getBalanceTest(ctx.message.author.id)
            msg = 'yeah ' + ctx.message.author.name + '! You received a faucet of ' + str(
                addFaucet) + ' coins. Your new Balance is ' + str(newbalance)
            print(msg)
            currentDT = datetime.datetime.now()
            updateFaucetTimeTest(ctx.message.author.id, str(currentDT))
            await ctx.send(msg)
        else:
            msg="Sorry! You can make only 1 faucet request in 1 hour"
            print("msg", msg)
            await ctx.send(msg)

@client.command()
async def historytest(ctx):
    list=getHistoryTest(ctx.message.author.id)
    msg = ""
    if len(list)==0:
        await ctx.send("No bets to display")
    for i in range(0,len(list)):
        if len(list)-i<=5:
            msg=msg+"Bet # "+ str(i+1)+"\n"
            bet=list[i]
            betattributes=bet.split(" ")
            msg=msg+"id = "+betattributes[0]+"\n"
            msg = msg+"WinChance = " + betattributes[1] + "\n"
            msg = msg+"BetAmount = " + betattributes[2] + "\n"
            msg = msg+"Roll Result = " + betattributes[3] + "\n"
            msg = msg+"Result = " + betattributes[4] + "\n"
            if float(betattributes[3])<=float(betattributes[4]):
                msg =msg+ "Profit or loss amount = +" + betattributes[5] + "\n"
            else:
                msg = msg + "Profit or loss amount = -" + betattributes[5] + "\n"
            msg = msg+"Balance = " + betattributes[6] + "\n"
            msg=msg+"------------------------------\n"
    await ctx.send(msg)


client.run(TOKEN)



