from classes import *


menu = ['1 : Просмотр услуг\n', '2 : Сделать заказ\n', '3 : Показать статус заказа\n', '4 : Отменить заказ\n']


def contr():
    n = input('1 : назад; 0 : для выхода\n')
    if n == '0':
        pass
    else:
        choice_outer = input(f'Меню : \n{"".join(menu)}')
        match choice_outer:
            case '1':
                for k, v in Uslugi.uslugi.items():
                    print(v[0], f'{v[1]} руб.', sep=' : ', end='\n')
            case '2':
                Zakazu.add_zakaz()
            case '3':
                Zakazu.show_status()
            case '4':
                Zakazu.remove_zakaz()
            case _:
                print("Введите число еще раз")
        return contr()


def adm_contr():
    n = input('1 : назад; 0 : для выхода\n')
    if n == '0':
        pass
    else:
        adm_choice_outer = input(f'\n1 : Авторизация\n2 : Регистрация\n0 : выход')
        match adm_choice_outer:
            case '1':
                Reg.log()
            case '2':
                Reg.reg()
            case '0':
                exit()
            case _:
                print("Введите число еще раз")
        return adm_contr()


if __name__ == '__main__':
    while True:
        choice_user = input('\n1 : покупатель\n2 : админ\n0 : exit\n')
        match choice_user:
            case '1':
                choice = input(f'Меню : \n{"".join(menu)}')
                match choice:
                    case '1':
                        for k, v in Uslugi.uslugi.items():
                            print(v[0], f'{v[1]} руб.', sep=' : ', end='\n')
                        contr()
                    case '2':
                        Zakazu.add_zakaz()
                        contr()
                    case '3':
                        Zakazu.show_status()
                        contr()
                    case '4':
                        Zakazu.remove_zakaz()
                        contr()
                    case _:
                        print("Введите число еще раз")

            case '2':
                lo = input('\n1 : Авторизация\n2 : Регистрация\n')
                match lo:
                    case '1':
                        if Reg.log():
                            AdminPanel.change_status()
                            adm_contr()
                        print('Неверный пароль')
                        adm_contr()
                    case '2':
                        Reg.reg()
                        adm_contr()
                    case _:
                        print('Введите число еще раз')
            case '0':
                exit()
            case _:
                print("Введите число еще раз")
