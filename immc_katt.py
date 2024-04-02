import math 

# Tid ( hjemme, vekter lite)
# Bolig ( ute/inne, vekter mye fordi katten mjauer)
# Barn (vekter middels foodi ansvar og)
# Lager score paa disse tre for katte modellen mjau.

c_responsibility_weight = 50
c_time_weight = 30
c_adaptability_weight = 20
assert c_responsibility_weight + c_time_weight + c_adaptability_weight == 100

class Household():
    def __init__(self, country, allocated_money, age, time_at_home):
        self.country = country
        self.allocated_money = allocated_money
        self.age = age
        self.time_at_home = time_at_home
    
    def calculate(self):
        responsibility = self.calculate_responsibility(0.7, 3)
        adaptability = self.calculate_adaptability()
        time = self.calculate_time()
        return (time * c_time_weight) + (responsibility * c_responsibility_weight) + (adaptability * c_adaptability_weight)
        
    def calculate_responsibility(self, personality, amount_of_kids):
        return 1

    def calculate_adaptability(self, amount_of_kids, house_type):
        score = 0
        if amount_of_kids == 0:
            score += 0.5
        
    def calculate_time(self): # avg time per day in hours
        # Cats need min 30 min
        # https://www.catster.com/guides/how-much-attention-does-a-cat-need/
        assert self.time_at_home <= 24
        score = float(100.2584 / (1 + 9.2034*(math.exp(-5.2851*self.time_at_home))))
        if score > 100:
            score = 100
        elif score < 0:
            score = 0
        return score/100

def allocated_money_function(money):
    return math.log(money)

def main():
    country = "Norway"
    allocated_money = 1000 # usd
    age = 30 # years
    time_at_home = 3.5 # hours
    household = Household(country, allocated_money, age, time_at_home)
    print(str(household.calculate()) + "%")

if __name__ == "__main__":
    main()