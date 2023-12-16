from classes import *


menu = ['1 : Просмотр услуг\n', '2 : Сделать заказ\n', '3 : Показать статус заказа\n', '4 : Отменить заказ\n']


def main():
    lo = input('\n1 : Авторизация\n2 : Регистрация\n')
    ob = Company().User(input('Логин : '), input('Пароль : '))
    ma = auth_in(ob, lo)
    if ma:
        while True:
            choice_1 = input(f'Меню : \n{"".join(menu)}')
            match choice_1:
                case '1':
                    for k, v in Company.uslugi.items():
                        print(v[0], f'{v[1]} руб.', sep=' : ', end='\n')
                case '2':
                    Zakazu.add_zakaz()
                case '3':
                    Zakazu.show_status()
                case '4':
                    Zakazu.remove_zakaz()
                case _:
                    print("Введите число еще раз")


def auth_in(ob, lo):
    match lo:
        case '1':
            if ob.log():
                return True
            else:
                print('ты не пройдешь, неверный логин или пароль!')
                exit()
        case '2':
            if ob.reg():
                return True
            else:
                exit()
        case _:
            print('Введите число еще раз')


if __name__ == '__main__':
    main()
