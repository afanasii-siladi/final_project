from constants import dict
delivery_cost = 0
delivery = 50
delivery_cost += delivery

menu = [product['product_name'] for product in dict]


user_name = input("Запишіть своє ім'я -> ")
print('Наше меню:')
for product in dict:
    print(f"{product['product_name']} - {product['price']}")
from constants import dict
delivery_cost = 0
delivery = 50
delivery_cost += delivery

menu = [product['product_name'] for product in dict]


user_name = input("Запишіть своє ім'я -> ")
print('Наше меню:')
for product in dict:
    print(f"{product['product_name']} - {product['price']}")
def check_menu():
    if order_user.lower() not in menu:
        print('Виправіть своє  замовлення, буд ласка. Можете записати по-новому своє замовлення')                
    else:
        delivery_cost += [product2['price'] for product2 in dict if product2['product_name'] == order_user.lower()][0]
        print('Вартість за доставку -> ',delivery)
        print('Вартість замовлення -> ',delivery_cost)

def write_in_file():
    with open('order_user.txt', 'w', encoding='utf-8') as f:
                    f.write(order_user)
                    f.write(';')
                    
def write_in_file_final():
    with open('order_for_{user_name}.txt', 'w', encoding='utf-8') as f:
                    f.write(order_user)
                    f.write(';')
                    f.write(add_oder)
                    f.write(';')
                                        
while True:
    order_user = input('запишіть замовлення з меню -> ')
    check_menu()
    
    not_add_oder = input('Якщо це весь сипос напишіть /замовлення готово, якщо потрібно продовжити замволення на друкуйте /далі -> ')
    if not_add_oder.lower() == 'замовлення готово':
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
                        delivery_cost1 = delivery_cost + [product2['price'] for product2 in dict if product2['product_name'] == add_oder.lower()][0] + [product2['price'] for product2 in dict if product2['product_name'] == order_user.lower()][0]
                        print('Вартість за доставку -> ',delivery)
                        print('Вартість замовлення -> ',delivery_cost1)
                        print('Дкую що використовували наш сайт.')
                        write_in_file_final()            
                        break
