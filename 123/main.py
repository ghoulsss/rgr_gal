from config import *
from classes import *

mycursor = mydb.cursor()
mycursor.execute("insert into zakazu (idzakazu, usluga, cost, company)"
                 " values (1, 'gaga', 15000, 'govnoed')")
mydb.commit()