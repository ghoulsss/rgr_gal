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

    @staticmethod
    def info():
        print('заказ оформлен')

    @staticmethod
    def del_info():
        print('Заказ удален')


class Zakazu(Uslugi):
    def __init__(self, name):
        self.name = name  # услуга передается через наследование сюда

    def add_zakaz(self,cos, com):
        mycursor = mydb.cursor()
        usl = self.name
        cos = int(cos)
        mycursor.execute(f"insert into zakazu (usluga, cost, company)"
                         f" values ('{usl}', {cos}, '{com}')")
        mydb.commit()
        self.info()

    def remove_zakaz(self, idz):
        mycursor = mydb.cursor()
        idz = int(idz)
        mycursor.execute("delete from zakazu where idzakazu = idz")
        mydb.commit()
        self.del_info()


s = Zakazu('atefirma')
s.add_zakaz(15000, 'hi_hitler')