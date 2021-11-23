class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.passengers = []
        self.balance = 0

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def remaining_capacity(self):
        capacity = self.capacity - len(self.passengers)
        return capacity

    def pick_up(self, person):
        self.passengers.append(person)
    
    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def take_cash(self, amount):
        self.balance += amount

    def pick_up_from_stop(self, bus_stop):
        passengers = bus_stop.queue
        for passenger in passengers:
            if self.capacity >= bus_stop.queue_lenth():
                if passenger.destination == bus_stop.name:
                    self.pick_up(passenger)
