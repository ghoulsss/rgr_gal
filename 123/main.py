from classes import *

menu = ['1 : Просмотр услуг\n', '2 : Сделать заказ\n', '3 : Показать статус заказа\n', '4 : Отменить заказ\n']
if __name__ == '__main__':
    while True:
        choice_user = input('\n1 : покупатель\n2 : админ\n')
        match choice_user:
            case '1':
                choice = input(f'Меню : \n{"".join(menu)}')
                match choice:
                    case '1':
                        Zakazu.show_all()
                    case '2':
                        Zakazu.add_zakaz()
                    case '3':
                        Zakazu.show_status()
                    case '4':
                        Zakazu.remove_zakaz()
                    case _:
                        print("Введите число еще раз")
            case '2':
                lo = input('\n1 : Авторизация\n2 : Регистрация\n')
                match lo:
                    case '1':
                        if Reg.log():
                            AdminPanel.change_status()
                    case '2':
                        Reg.reg()
                    case _:
                        print('Введите число еще раз')
            case _:
                print("Введите число еще раз")
