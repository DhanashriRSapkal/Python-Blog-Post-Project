import pymysql as p
def getConnection():
    return p.connect(host='localhost',user='root',password='',database='blogpost1')
    
def Addauthor(t):
    db=getConnection()
    sql='insert into authortable1(Id,Authorname,Password,Email,City) values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def Adduser(t):
    db=getConnection()
    sql='insert into usertable1(Id,Username,Password,Email,City) values(%s,%s,%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def addpost(t):
    db=getConnection()
    sql='insert into addpost(Id,Authorname,Blog) values(%s,%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()


def showpost(t):
    db=getConnection()
    sql='insert into showpost(Email,Password) values(%s,%s)'
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()
