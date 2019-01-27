import shelve
import uuid
from datetime import date
user = shelve.open('user')
users = shelve.open('user')
class User:

    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''
        self.__re_password = ''

    def get_id(self):
        return self.__id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password
    def set_re_password(self, re_password):
        self.__re_password = re_password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
    def get_re_password(self):
        return self.__re_password




def create_user(username, password, re_password):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_password(password)
    user.set_re_password(re_password)
    if user.get_password() == user.get_re_password() :
        users[id] = user
    else:
        print("Password has been wrongly entered")

def get_user(username, password):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), user.get_password())
        if user.get_username() == username and user.get_password() == password :
            return user
    return None

def update_user(id, user):
    users[id] = user
    return users[id]

def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]



def add_user(user):
    users[user.get_id()] = user

# *****Goals*****

Goals = shelve.open('goal')
class Goal:
    def __init__(self, id):
        self.id = id
        self.username = ''
        self.title = ''
        self.body = ''
        self.created = ''
        self.Due = ''
        self.description = ''
        self.value = ''
        self.percentage = ''
        self.value = 0


def create_goal(username, title, body,Due,description,value,percentage):
    id = str(uuid.uuid4())
    goal = Goal(id)
    goal.title = title
    goal.username = username
    goal.body = body
    goal.Due = Due
    goal.description = description
    goal.value = value
    goal.percentage = percentage
    goal.created = str(date.today())
    Goals[id] = goal

def get_body(id,body):
    i = Goal(id)
    i.body = body
    Goals[id] = i
def Save_body(id,body):
    if id in Goals:
        i = Goals[id]
        del Goals[id]
    else:
        i = Goal(id)
    Goals[id] = i
    i.body = body
def GetBody(id):
    if id in Goals:
        return Goals[id].body
    else:
        return 0
def GetPercentage(id):
    l = []
    try:
        i = GetBody(id)
        j = getInfo(id)
        a = ((int(j)/int(i))*100)
        l.append(a)
        y = sum(l)
        return y
    except ZeroDivisionError:
        return 0

def update_goal(goal):
    Goals[goal.id] = goal

def delete_goal(id):
    if id in Goals:
        del Goals[id]

def get_goals():
    klist = list(Goals.keys())
    x = []
    for i in klist:
        x.append(Goals[i])
    return x

def get_goal(id):
    if id in Goals:
        return Goals[id]

def clear_goal():
    klist = list(Goals.keys())
    for key in klist:
        del Goals[key]
def init_db():
    clear_user()
    clear_goal()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i), 're_pass'+str(i))
        create_goal('user'+str(i), 'title'+str(i), 'body'+str(i), 'Due'+str(i),'description'+str(i),'value'+str(i),'percentage'+str(i))



#print(percentage(10))

class Amount:
    def __init__(self,id):
        self.id = id
        self.money = ''



Value = shelve.open("Rate")


def saveInfo(id,money):
    i = Amount(id)
    i.money = money
    Value[id] = i

def saveMoney(id,money):
    if id in Value: # retrieve record
        i = Value[id]
        del Value[id]
    else: # new record
        i = Amount(id)
    Value[id] = i
    i.money = money


def getInfo(id):
    if id in Value:
        i =  Value[id].money
        return int(i)
    else:
        return 0








'''
get_body("184124U",100)
Save_body("184124U",100)
GetPercentage("184124U")
saveInfo("184124U",50)
saveMoney("184124U",50)
print(getInfo("184124U"))
print(GetPercentage("184124U"))
'''

#Total
class Total:
    def __init__(self,id):
        self.id =id
        self.T_Goal = ''
        self.A_Money = ''
        self.A = ''
def GetT_Goal():
    klist = list(Goals.keys())
    x = []
    for i in klist:
        x.append(int(Goals[i].body))
    return sum(x)

def GetA_Money():
    klist = list(Value.keys())
    l = []
    for i in klist:
        l.append(int(Value[i].money))
    return sum(l)


print(GetT_Goal())
print(GetA_Money())






        
'''      

def get_amounts():
    klist = list(Goals.keys())
    x = []
    for i in klist:
        x.append(Goals[i].body)
    return x  
#********************** decrease value of saving *********************************

class MoneyData:
    def __init__(self,value):
        self.value = value

Value = shelve.open("Money")
def saveAim():
    Aim = Top

#************ Progress bar ***************
class Values(User):
    def __init__(self,id,val1,val2):
        super().__init__(id)
        self.val1 = val1
        self.val2 = val2
    def set_val1(self,val1):
        self.val1 = val1

    def set_val2(self, val2):
        self.val2 = val2
    def set_total(self,total):
        self.total = total
    def get_val1(self):
        return self.val1
    def get_val2(self):
        return self.val2


class calculate(Values):
    tlist = []
    def __init__(self,id,val1,val2):
        super().__init__(id,val1,val2)
    def subtraction(self,id):
        self.val1 = getInfo(id)
        self.val2 = getGoal(id)
        i = self.val2- self.val1
        return i
    def percentage(self,id):
        try:
            self.val1 = getInfo(id)
            self.val2 = getGoal(id)
            i = ((self.val1/self.val2)*100)
            return i
        except ZeroDivisionError:
            return 0
    def Total_1(self,id):
        self.val1 = getInfo(id)
        self.__class__.tlist.append(self.val1)
        sum1 = sum(self.__class__.tlist)
        return sum1


Aim = shelve.open("Aim")
def SaveGoal(id,body):
    i = Goal(id)
    i.body = body
    Aim[id] = i
def SaveBody(id,money):
    if id in Aim:
        i = Aim[id]
        del Aim[id]
    else:
        i = Goal(id)
    Aim[id] = i
    i.body = money
def getGoal(id):
    if id in Aim:
        return Aim[id].body
    else:
        return 0

plist = []

Value = shelve.open("Money")
class Amount:
    def __init__(self, id):
        self.id = id
        self.body = 0
a = Amount("QUEEN")
def create_amount(body):
    id = str(uuid.uuid4())
    amt = Amount(id)
    i = Goal(id)
    i.body = body
    amt.value =  body
    Value[id] = i

def get_amount(id):
    if id in Value:
        return Value[id]

def clear_amount():
    klist = list(Value.keys())
    for key in klist:
        del Value[key]



class Money_input():
    def __init__(self,id):
        self.id = id
        self.money = 0

Aim = shelve.open("Rate")

def SaveBody(id,money):
    if id in Aim:
        i = Aim[id].money
        del Aim[id].money
    else:
        i = Money_input(id)
    Aim[id] = i
    i.money = money
def getGoal(id):
    if id in Aim:
        i = Aim[id].money
        return i
    else:
        return 0
def SaveGoals(id,body):
    if id in Goals:
        i = Goals[id]
        del Goals[id]
    else:
        i = Goal(id)
    i.body = body
    return i.body
def GetInfo(id):
    if id in Goals:
        i = Goals[id].body
        return i
    else:
        return 0
print(SaveGoals("184124U",40))
print(GetInfo("184124U"))








def saveInfo(id,amount):
    i = Goal(id)
    i.Goals = amount
    Goals[id] = i

def saveMoney(id,amount):
    if id in Goals: # retrieve record
        i = Goals[id]
    else: # new record
        i = Goal(id)

    i.value = amount
    Goals[id] = i

def getInfo(id):
    if id in Goals:
        i =  Goals[id].value
        return i

    else:
        return 0
def getInfos():
    vlist = list(Goals.keys())
    x = []
    for i in vlist:
        x.append(Goals[i].value)
    return x






def percentage_1():
    k = []
    j = getInfos()
    for i in get_amounts():
        for j in getInfos():
            j = (int(j) / int(i)) * 100
        k.append(j)
    return k

print(percentage_1())

def addition(num):
    l = []
    for i in get_amounts():
        j = int(i) + num
        l.append(j)

    return l



Aim = shelve.open("Aim")
def SaveGoal(id,body):
    i = Goal(id)
    i.body = body
    Aim[id] = i
def SaveBody(id,money):
    if id in Aim:
        i = Aim[id]
        del Aim[id]
    else:
        i = Goal(id)
    Aim[id] = i
    i.body = money
def getGoal(id):
    if id in Aim:
        return Aim[id].body
    else:
        return 0




'''












