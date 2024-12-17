import random

# паттерн "Наблюдатель"
class Observer:
    def update(self, product):
        raise NotImplementedError()

class Person(Observer):
    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.inventory = []
    
    def update(self, product):
        print(f"Уведомление для {self.name}: Цена на {product.name} изменилась до {product.price:.2f}")

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

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
    
    def set_price(self, new_price):
        self.price = new_price
        self.notify_observers()

# паттерн "Стратегия"
class DemandStrategy:
    def calculate_demand(self, product):
        raise NotImplementedError()

class RandomDemandStrategy(DemandStrategy):
    def calculate_demand(self, product):
        return random.uniform(0.8, 1.2)


class Company:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products
    
    def add_product(self, product):
        self.products.append(product)
    
    def get_products(self):
        return self.products

class Market:
    def __init__(self, companies=[], people=[], demand_strategy=None):
        self.companies = companies
        self.people = people
        self.demand_strategy = demand_strategy if demand_strategy else RandomDemandStrategy()
    
    def add_company(self, company):
        self.companies.append(company)
    
    def add_person(self, person):
        self.people.append(person)
    
    def update_prices(self):
        for company in self.companies:
            for product in company.get_products():
                demand_factor = self.demand_strategy.calculate_demand(product)
                new_price = product.price * demand_factor
                product.set_price(new_price)
    
    def simulate_day(self):
        self.update_prices()
        for person in self.people:
            chosen_company = random.choice(self.companies)
            chosen_product = random.choice(chosen_company.get_products())
            person.buy_product(chosen_company, chosen_product.name)

# пример использования:

apple_inc = Company("Apple Inc.")
iphone = Product("iPhone 13", 50000)
apple_inc.add_product(iphone)

john = Person("John", 45000)
iphone.add_observer(john)

# создаем рынок с конкретной стратегией спроса
market = Market([apple_inc], [john], RandomDemandStrategy())

market.simulate_day()