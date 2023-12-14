from classes import *


menu = ['1 : Просмотр услуг\n', '2 : Сделать заказ\n', '3 : Показать статус заказа\n', '4 : Отменить заказ\n']

def main():
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


def log_in():
    lo = input('\n1 : Авторизация\n2 : Регистрация\n')
    match lo:
        case '1':
            if User.log:
                print('Неверный пароль')
        case '2':
            Reg.reg()
        case _:
            print('Введите число еще раз')


if __name__ == '__main__':
    main()