from constants import d
q1 = 150

menu = ('картошка фри', 'бургер', 'пицца', 'кола', 'спрайт', 'фанта', 'яблочный сок', 'вишньовый сок', 'сок мултифрукт', 'йогурт', 'тортик', 'морожено')

user_name = input('Введите свое имя-> ')
print('Наше меню:')
print(d)
while True:
        order_user = input('введите свой заказ из меню -> ')
        if order_user.lower() not in menu:
                print('вы не правельно записали заказ. Можете ввести заного свой заказ')                
        else:
                print(order_user)          
                if order_user.lower() == 'картошка фри':
                        q1 += 45
                elif order_user.lower() == 'бургер':
                        q1 += 135
                elif order_user.lower() == 'пицца':
                        q1 += 95
                elif order_user.lower() == 'кола':
                        q1 += 29
                elif order_user.lower() in ('спрайт', 'фанта'):
                        q1 += 39       
                elif order_user.lower() in ('яблочный сок', 'вишньовый сок', 'сок мултифрукт'):
                        q1 += 20
                elif order_user.lower() == 'йогурт':
                        q1 += 45
                elif order_user.lower() == 'тортик':
                        q1 += 55
                elif order_user.lower() == 'морожено':
                        q1 += 15

                print('Вам нужно заплатить за заказ -> ',q1)
                q2 = input('вам хватает средств для оплаты(да или нет) -> ')

                if q2.lower() not in ('да', 'нет'):
                        print('Вы должны ввести да или нет иначе у нас не выйдет доставить заказ')
                else:
                        if q2.lower() == 'да':
                                print('спасибо за покупку заказ будет скоро у вас.')  
                                with open('Order/order.txt', 'a', encoding='utf-8') as f:
                                        f.write(order_user)
                                а = input('Вы хотите изменить или отменить свой заказ -> ')
                                print(order_user)
                                if а.lower() not in ('отменить', 'изменить'):
                                        print('Error')
                                else:
                                        if а.lower() == 'изменить':
                                                order_user = input('введите свой заказ из меню -> ')
                                                if order_user not in menu:
                                                        print('Error')
                                                print(order_user)
                                                with open('Order/order.txt', 'a', encoding='utf-8') as f:
                                                        f.write(order_user)     
                                        else:
                                                print('Спасибо что посетили наш сайт')       
                                                with open('Order/order.txt', 'a', encoding='utf-8') as f:
                                                        f.write(order_user)