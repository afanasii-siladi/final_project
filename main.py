from constants import d
q1 = 150

menu = ('картошка фри', 'бургер', 'пицца', 'кола', 'спрайт', 'фанта', 'яблочный сок', 'вишньовый сок', 'сок мултифрукт', 'йогурт', 'тортик', 'морожено')

user_name = input('Введите свое имя-> ')
print('Наше меню:')
for product in d:
        print(f"{product['product_name']} - {product['price']}")

while True:
        order_user = input('Введите свой заказ из меню -> ')
        if order_user.lower() not in menu:
                print('Вы не правельно записали заказ. Можете ввести заного свой заказ', user_name )                
        else:
                print(order_user.lower())   
                q1 += [i['price'] for i in d if i['product_name'] == order_user.lower()][0]
                              
                print('Вам нужно заплатить за заказ -> ',q1)
                q2 = input('Вам хватает средств для оплаты(да или нет) -> ')

                if q2.lower() not in ('да', 'нет'):
                        print('Вы должны ввести да или нет иначе у нас не выйдет доставить заказ')
                else:
                        if q2.lower() == 'да':
                                print('Спасибо за покупку заказ будет скоро у вас ', user_name, '.')  
                                with open('Order/order.txt', 'a', encoding='utf-8') as f:
                                        f.write(order_user)
                                а = input('Вы хотите изменить или отменить свой заказ -> ')
                                print(order_user)
                                if а.lower() not in ('отменить', 'изменить'):
                                        print('Error')
                                else:
                                        if а.lower() == 'изменить':
                                                order_user = input('Введите свой заказ из меню -> ')
                                                if order_user not in menu:
                                                        print('Error')
                                                print(order_user)
                                                with open('Order/order.txt', 'a', encoding='utf-8') as f:
                                                        f.write(order_user)     
                                        else:
                                                print('Спасибо что посетили наш сайт')       
                                                with open('Order/order.txt', 'a', encoding='utf-8') as f:
                                                        f.write(order_user)