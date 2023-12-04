from config import *


class Uslugi:
    uslugi = {'Провести рекламную компанию': 15000,
              'Определение прибыльных маркетинговых целей': 5000,
              'Маркетинговая стратегия для вашей компании': 50000,
              'Создание и продвижение товара': 30000,
              'План распределения бюджета компании': 25000,
              }
    # объявить здесь конструктор принимает имя компании и при этом наследуется вниз
    # еще может что-то добавить сюда


class Zakazu(Uslugi):
    def __init__(self, name):
        self.name = name  # услуга передается через наследование сюда

    def add_zakaz(self, idz, cos, com):
        mycursor = mydb.cursor()
        usl = self.name
        idz = int(idz)
        cos = int(cos)
        mycursor.execute(f"insert into zakazu (idzakazu, usluga, cost, company)"
                         f" values ({idz}, '{usl}', {cos}, '{com}')")
        mydb.commit()

    def remove_zakaz(self, idz):
        mycursor = mydb.cursor()
        idz = int(idz)
        mycursor.execute("delete from zakazu where idzakazu = idz")
        mydb.commit()


s = Zakazu('atefirma')
s.add_zakaz(1, 15000, 'hi_hitler')
