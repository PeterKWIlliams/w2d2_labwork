class Train:
    def __init__(self, capacity, destination, origin, price):
        self.capacity = capacity
        self.destination = destination
        self.origin = origin
        self.price = price
        self.passengers = []
        self.season_ticket_price = 20

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def passenger_count(self):
        return len(self.passengers)

    def remaining_capacity(self):
        capacity = self.capacity - len(self.passengers)
        return capacity
    
    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def take_cash(self, amount, person):
        if person.number_of_trips < 5:
            self.balance += amount
            person.cash -= amount
        

