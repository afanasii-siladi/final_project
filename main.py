from constants import dict
delivery_cost = 50

menu = [ product['product_name'] for product in dict]

user_name = input('Введите свое имя-> ')
print('Наше меню:')
for product in dict:
        print(f"{product['product_name']} - {product['price']}")

while True:
        order_user = input('Введите свой заказ из меню -> ')
        if order_user.lower() not in menu:
                print('Вы не правельно записали заказ. Можете ввести заного свой заказ', user_name )                
        else:
                print(order_user.lower())   
                delivery_cost += [product2['price'] for product2 in dict if product2['product_name'] == order_user.lower()][0]
                              
                print('Вам нужно заплатить за заказ -> ',delivery_cost)
                pay = input('Вам хватает средств для оплаты(да или нет) -> ')

                if pay.lower() not in ('да', 'нет'):
                        print('Вы должны ввести да или нет иначе у нас не выйдет доставить заказ', user_name,)
                else:
                        def with_write_file():
                                with open('Order/order.txt', 'a', encoding='utf-8') as f:
                                        f.write(order_user) 

                        if pay.lower() == 'да':
                                print('Спасибо за покупку заказ будет скоро у вас ', user_name, '.')  
                                with_write_file()
                                break
                                а = input('Вы хотите изменить или отменить свой заказ -> ')
                                print(order_user)
                                if а.lower() not in ('отменить', 'изменить'):
                                        print('Такой ответ не возможен!')
                                else:

                                        if а.lower() == 'изменить':
                                                order_user = input('Введите свой заказ из меню -> ')
                                                if order_user not in menu:
                                                        print('Error')
                                                print(order_user)
                                                with_write_file()     
                                        else:
                                                print('Спасибо что посетили наш сайт')       
                                                with_write_file()