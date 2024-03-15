class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Roommate:
    def __init__(self, name, days_in_room):
        self.name = name
        self.days_in_room = days_in_room

    def pays(self, bill, roommate2):
        weight = self.days_in_room / (self.days_in_room + roommate2.days_in_room)
        return bill.amount * weight