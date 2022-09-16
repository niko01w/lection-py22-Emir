from views import *
from registration import *
import json

class Car( LoginMixin, CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin, OrderMixin, RegisterMixin):
    def start(self):
        choice = input('Добро пожаловать!\nХотите начать работу? Да/Нет: ')
        while choice.lower() == 'да':
            print('Что бы вы хотели сделать?(1 - войти в аккаунт 2 - create, 3 - listing, 4 - retrieve, 5 - update, 6 - delete, 7 - order, 8 - exit)')
            a = int(input('Выберите действие: (1,2,3,4,5,6,7): '))
            if   a == 1: print(super().login())
            elif a == 2: print(super().create_product())
            elif a == 3: print(super().listing_products())
            elif a == 4: print(super().retrieve_data())
            elif a == 5: print(super().update_data())
            elif a == 6: print(super().delete_product())
            elif a == 7: print(super().order_car())
            elif a == 8: 
                print('Благодарим вас за работу!')
                break
            else: print('Такого действия нет!')

a = Car()
a.start()



