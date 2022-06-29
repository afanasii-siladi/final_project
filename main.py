from constants import dict
delivery_cost = 0
delivery = 50
delivery_cost += delivery

menu = [product['product_name'] for product in dict]


user_name = input("Запишіть своє ім'я -> ")
print('Наше меню:')
for product in dict:
    print(f"{product['product_name']} - {product['price']}")
    
def write_in_file():
    with open('order_user.txt', 'w', encoding='utf-8') as fw:
                    fw.write(order_user)
                    fw.write(';')
                    

def write_in_file_finish():
    with open('order_for_{user_name}.txt', 'w', encoding='utf-8') as fw:
                    fw.write(order_user)
                    fw.write(';')
                    fw.write(add_oder)
                    fw.write(';')

def print_final():
    print('Вартість за доставку -> ',delivery)
    print('Вартість замовлення -> ',delivery_cost)


def cart():
    with open('order_user_cart.txt', 'r', encoding='utf-8') as fr:
        data = fr.read()


def cancel_order():
    a = input('Вам потрібно відмінити замовлення, так чи ні? ')
    if a == 'так':
        print('Замовлення скасовано.') 
        cart()          
    else:
        print('Дкую що використовували наш сайт.')
     

while True:
    order_user = input('запишіть замовлення з меню -> ')
    if order_user.lower() not in menu:
        print('Виправіть своє  замовлення, буд ласка. Можете записати по-новому своє замовлення')             
    else:
        delivery_cost += [product2['price'] for product2 in dict if product2['product_name'] == order_user.lower()][0]
        print_final()
        not_add_oder = input('Якщо це весь сипос напишіть /готово, якщо потрібно продовжити замволення на друкуйте /далі -> ')
        if not_add_oder.lower() == 'готово':
            print_final()
            print('Дякую за покупку, незабаром замовлення прибуде до вас.')  
            write_in_file()            
            break
        elif not_add_oder.lower() == 'далі':
                        add_oder = input('доповнити замовлення можливо на цьому кроці -> ')
                        if add_oder.lower() not in menu:
                            print('Виправіть своє  замовлення, буд ласка. Потрібно записати по-новому замовлення')            
                        else:
                            print(order_user.lower())   
                            print(add_oder.lower())
                            delivery_cost += [product2['price'] for product2 in dict if product2['product_name'] == add_oder.lower()][0] + [product2['price'] for product2 in dict if product2['product_name'] == order_user.lower()][0]
                            print_final()
                            cancel_order()
                            write_in_file_finish()            
                            break
