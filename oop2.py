import random

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Company:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products
    
    def add_product(self, product):
        self.products.append(product)
        
    def set_price(self, product_name, new_price):
        for product in self.products:
            if product.name == product_name:
                product.price = new_price
                
    def get_products(self):
        return self.products

class Person:
    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.inventory = []
    
    def buy_product(self, company, product_name):
        for product in company.get_products():
            if product.name == product_name:
                if self.money >= product.price:
                    print(f"{self.name} купил {product.name} за {product.price}")
                    self.money -= product.price
                    self.inventory.append(product)
                    return True
                else:
                    print(f"У {self.name} недостаточно денег для покупки {product.name}")
                    return False
        print(f"Товар {product_name} отсутствует в ассортименте компании {company.name}")
        return False

class Market:
    def __init__(self, companies=[], people=[]):
        self.companies = companies
        self.people = people
    
    def add_company(self, company):
        self.companies.append(company)
    
    def add_person(self, person):
        self.people.append(person)
    
    def update_prices(self):
        # Простейшая модель изменения цен в зависимости от случайного спроса
        for company in self.companies:
            for product in company.get_products():
                demand_factor = random.uniform(0.8, 1.2)
                product.price *= demand_factor
                print(f"Цена на {product.name} изменилась до {product.price:.2f}")
    
    def simulate_day(self):
        # Имитация одного дня на рынке
        self.update_prices()
        for person in self.people:
            chosen_company = random.choice(self.companies)
            chosen_product = random.choice(chosen_company.get_products())
            person.buy_product(chosen_company, chosen_product.name)

# 1:
# Создаем компанию
apple_inc = Company("Apple Inc.")

# Добавляем новый продукт
iphone = Product("iPhone 13", 50000)
apple_inc.add_product(iphone)

print(apple_inc.get_products())  # Выводит список продуктов компании

# 2:
# Создаем человека
john = Person("John", 45000)

john.buy_product(apple_inc, "iPhone 13")
john.buy_product(apple_inc, "Samsung Galaxy s24+")

# 3:
# Создаем рынок
market = Market([apple_inc], [john])

# Симулируем один день на рынке
market.simulate_day()  # Обновляет цены и имитирует покупку товаров людьми