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

    @staticmethod
    def change_info():
        print('Статус заказа изменен')


class Zakazu(Uslugi):
    # def __new__(cls, *args, **kwargs):
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

        mycursor.execute(f"insert into zakazu (usluga, cost, company, status)"
                         f" values ('{usl}', {cos}, '{com}', 'в обработке')")
        mydb.commit()
        cls.info()

    @classmethod
    def change_status(cls):
        mycursor = mydb.cursor()
        mycursor.execute("select * from zakazu")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"id : {i[0]}, компания : {i[3]}, услуга - {i[1]}, по цене : {i[2]} руб.")
        n = int(input('Выберите id заказа, статус которого хотите поменять : '))
        if n not in [i[0] for i in zakaz]:
            print("id заказа не существует")
            pass
        status1 = ['в обработке', 'в процессе', 'Выполнен'][int(input("1 : В обработке"
                                                                      "\n2 : В процессе\n3 : Выполнен\n")) - 1]
        mycursor.execute(f"update zakazu set status = '{status1}' where idzakazu like {n}")
        mydb.commit()
        cls.change_info()

    @classmethod
    def remove_zakaz(cls):
        mycursor = mydb.cursor()
        n = input('Введите наименование компании : ')
        mycursor.execute("select company from zakazu")
        zakaz = mycursor.fetchall()
        if n not in zakaz:
            print('Компания не найдена')
            pass
        mycursor.execute(f"select * from zakazu where company like '{n}'")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"id : {i[0]}, компания : {i[3]}, услуга - {i[1]}, по цене : {i[2]} руб., статус заказа : {i[3]}")
        n = int(input('Выберите id заказа который хотите удалить : '))
        mycursor.execute(f"delete from zakazu where idzakazu = {n}")
        mydb.commit()
        cls.del_info()

    @classmethod
    def show_all(cls):
        mycursor = mydb.cursor()
        mycursor.execute(f"select * from zakazu")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"id : {i[0]}, компания : {i[3]}, услуга - {i[1]}, по цене : {i[2]} руб., статус заказа : {i[3]}")

    @classmethod
    def show_status(cls):
        n = int(input('Введите id заказа для информации о статусе доставки : '))
        mycursor = mydb.cursor()
        mycursor.execute(f"select usluga, status from zakazu where idzakazu like '{n}'")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"Услуга : {i[0]}, статус заказа : {i[1]}")


s = Zakazu()
s.add_zakaz()
s.change_status()
s.remove_zakaz()
s.show_status()
s.show_all()

