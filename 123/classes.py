from config import *


class Uslugi:
    uslugi = {1: ['Провести рекламную компанию', 15000],
              2: ['Определение прибыльных маркетинговых целей', 5000],
              3: ['Маркетинговая стратегия для вашей компании', 50000],
              4: ['Создание и продвижение товара', 30000],
              5: ['План распределения бюджета компании', 25000],
              }

    @staticmethod
    def info():
        print('заказ оформлен')

    @staticmethod
    def del_info():
        print('Заказ удален')


class Zakazu(Uslugi):
    def __new__(cls, *args, **kwargs):
        print('Введите имя компании : ')
        return super().__new__(cls)

    @classmethod
    def add_zakaz(cls):
        mycursor = mydb.cursor()
        com = input('Наименование компании')
        for k, v in cls.uslugi.items():
            print(k, v[0], sep=' : ', end='\n')

        n = int(input('Выберите услугу : '))
        usl = cls.uslugi[n][0]
        cos = cls.uslugi[n][1]

        mycursor.execute(f"insert into zakazu (usluga, cost, company)"
                         f" values ('{usl}', {cos}, '{com}')")
        mydb.commit()
        cls.info()

    @classmethod
    def remove_zakaz(cls):
        mycursor = mydb.cursor()
        print(mycursor.execute('select * from zakazu'))
        mycursor.execute("delete from zakazu where idzakazu = idz")
        mydb.commit()
        cls.del_info()


s = Zakazu('atefirma')
s.add_zakaz()
