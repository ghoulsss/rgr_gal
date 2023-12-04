from config import *


class Uslugi:
    uslugi = {1: ['Проведение рекламной компании', 15000],
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
    # def __new__(cls, *args, **kwargs):
    #     print('Введите имя компании : ')
    #     return super().__new__(cls)

    @classmethod
    def add_zakaz(cls):
        mycursor = mydb.cursor()
        com = input('Наименование компании : ')
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
        mycursor.execute("select * from zakazu")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"id : {i[0]}, компания : {i[3]}, услуга - {i[1]}, по цене : {i[2]} руб.")
        n = int(input('Выберите id заказа который хотите удалить : '))
        mycursor.execute(f"delete from zakazu where idzakazu = {n}")
        mydb.commit()
        cls.del_info()


#  vuvod = [(1, 'Определение прибыльных маркетинговых целей', 5000, 'gogo'),
#         (2, 'Определение прибыльных маркетинговых целей', 5000, 'gogo2'),
#         (3, 'Создание и продвижение товара', 30000, 'gogo3')]

Zakazu.remove_zakaz()
