from config import *
from abc import ABC, abstractmethod


class Uslugi:
    uslugi = {1: ['Проведение рекламной компании', 15000],
              2: ['Определение прибыльных маркетинговых целей', 5000],
              3: ['Маркетинговая стратегия для вашей компании', 50000],
              4: ['Создание и продвижение товара', 30000],
              5: ['План распределения бюджета компании', 25000],
              }

    @staticmethod
    def info():
        print('заказ оформлен\n')

    @staticmethod
    def del_info():
        print('Заказ удален\n')

    @staticmethod
    def change_info():
        print('Статус заказа изменен\n')

    @staticmethod
    def log_info():
        print('Вы успешно зарегистрировались\n')


class Zakazu(Uslugi):
    @classmethod
    def add_zakaz(cls):
        mycursor = mydb.cursor()
        com = input('Наименование компании : ')
        cls.check(com)
        for k, v in cls.uslugi.items():
            print(k, v[0], sep=' : ', end='\n')

        n = int(input('Выберите услугу : '))
        usl = cls.uslugi[n][0]
        cos = cls.uslugi[n][1]

        mycursor.execute(f"insert into zakazu (usluga, cost, company, status)"
                         f" values ('{usl}', {cos}, '{com}', 'в обработке')")
        mydb.commit()
        cls.info()

    @abstractmethod
    def change_status(self):
        pass

    @classmethod
    def show_status(cls):
        mycursor = mydb.cursor()
        n = int(input('Введите id заказа для информации о статусе доставки : '))
        cls.check(n)
        mycursor.execute(f"select idzakazu from zakazu")
        zakaz = list(list(i)[0] for i in mycursor.fetchall())
        if n not in zakaz:
            print("id заказа не существует")
            exit()
        mycursor.execute(f"select usluga, status from zakazu where idzakazu like '{n}'")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"Услуга : {i[0]}, статус заказа : {i[1]}")

    @classmethod
    def remove_zakaz(cls):
        mycursor = mydb.cursor()
        n = input('Введите наименование компании : ')
        cls.check(n)
        mycursor.execute("select company from zakazu")
        zakaz = mycursor.fetchall()
        if n not in zakaz:
            print('Компания не найдена')
            pass
        mycursor.execute(f"select * from zakazu where company like '{n}'")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"id : {i[0]}, компания : {i[3]}, услуга - {i[1]}, по цене : {i[2]} руб., статус заказа : {i[4]}")
        n = int(input('Выберите id заказа который хотите отменить : '))
        if n not in [i[0] for i in zakaz]:
            print("id заказа не существует")
            pass
        mycursor.execute(f"delete from zakazu where idzakazu = {n}")
        mydb.commit()
        cls.del_info()

    @classmethod
    def show_all(cls):
        mycursor = mydb.cursor()
        mycursor.execute(f"select * from zakazu")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"id : {i[0]}, компания : {i[3]}, услуга - {i[1]}, по цене : {i[2]} руб., статус заказа : {i[4]}")

    @classmethod
    def check(cls, obj):
        if obj == '':
            print('пустое поле')
            exit()


class AdminPanel(Zakazu):
    @classmethod
    def change_status(cls):
        mycursor = mydb.cursor()
        mycursor.execute("select * from zakazu")
        zakaz = mycursor.fetchall()
        for i in zakaz:
            print(f"id : {i[0]}, компания : {i[3]}, услуга - {i[1]}, по цене : {i[2]} руб.")
        n = input('Выберите id заказа, статус которого хотите поменять : или 0 если хотите выйти')
        cls.check(n)
        n = int(n)
        if n not in [i[0] for i in zakaz]:
            print("id заказа не существует")
            return cls.change_status()
        status1 = ['в обработке', 'в процессе', 'Выполнен'][
            int(input("1 : В обработке\n2 : В процессе\n3 : Выполнен\n")) - 1]
        mycursor.execute(f"update zakazu set status = '{status1}' where idzakazu like {n}")
        mydb.commit()
        cls.change_info()


class Reg:
    @staticmethod  # создать аккаунт для админов(новых)
    def reg():
        mycursor = mydb.cursor()
        mycursor.execute(f"select login from admins")
        logins = list(list(i)[0] for i in mycursor.fetchall())
        logi = input('Введите логин : ')
        if logi in logins:
            print("логин уже существует")
            exit()
        passw = input('Введите пароль : ')
        Zakazu.check(logi)
        # Zakazu.check(passw) проверка на пустой пароль
        if logi not in logins:
            mycursor = mydb.cursor()
            mycursor.execute(f"insert into admins (login, password) values ('{logi}', '{passw}')")
            mydb.commit()
            Uslugi.log_info()

    @staticmethod
    def log():  # возвращает тру если логин прошел
        mycursor = mydb.cursor()
        mycursor.execute(f"select login from admins")
        logins = list(list(i)[0] for i in mycursor.fetchall())
        logi = input('Введите логин : ')
        if logi not in logins:
            print("логин не найден")
            exit()
        passw = input('Введите пароль : ')
        Zakazu.check(logi)
        # Zakazu.check(passw) проверка на пустой пароль
        mycursor = mydb.cursor()
        mycursor.execute(f"select login from admins")
        logins = list(list(i)[0] for i in mycursor.fetchall())
        if logi in logins:
            mycursor = mydb.cursor()
            mycursor.execute(f"select * from admins")
            check = mycursor.fetchall()
            p = check[0][1]
            return True if passw == p else False
