from config import *

class Uslugi:
    uslugi = {'Провести рекламную компанию': 15000,
              'Определение прибыльных маркетинговых целей': 5000,
              'Маркетинговая стратегия для вашей компании': 50000,
              'Создание и продвижение товара': 30000,
              'План распределения бюджета компании': 25000,
              }
    pass


class Zakazu(Uslugi):
    def __init__(self, name):
        self.name = name


s = Zakazu(input('name type pls'))
print(s.name)
