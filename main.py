from constants import dict
delivery_cost = 50

menu = [product['product_name'] for product in dict]

user_name = input("Запишіть своє ім'я -> ")
def menu():
    print('Наше меню:')
    for product in dict:
        print(f"{product['product_name']} - {product['price']}")

menu()

def main():                          
    while True:
        order_user = input('запишіть замовлення з меню -> ')
        if order_user.lower() not in menu:
                print('Виправіть своє  замовлення, буд ласка. Можете записати по-новому своє замовлення')                
        else:
            add_oder = input('Якщо потрібно доповнити замовлення продовжуйте свій список далі, якщо це все напишіть замовлення готово -> ')
            if add_oder.lower() == 'замовлення готово':
                delivery_cost += [product2['price'] for product2 in dict if product2['product_name'] == order_user.lower()][0]
                print('Вартість замовлення -> ',delivery_cost)
                print('Дякую за покупку замовлення буде скоро у вас.')  
                def with_write_file():
                    with open('Order/order_for_{user_name}.txt', 'w', encoding='utf-8') as f:
                            f.write(order_user)
                with_write_file()
                break
            elif order_user.lower() not in menu:
                print('Виправіть своє  замовлення, буд ласка. Можете записати по-новому своє замовлення')            
            else:
                print(order_user.lower())   
                delivery_cost += [product2['price'] for product2 in dict if product2['product_name'] == order_user.lower()][0]
                print('Вартість замовлення -> ',delivery_cost)
                print('Дкую що використовували наш сайт.')
                
main()                                                                