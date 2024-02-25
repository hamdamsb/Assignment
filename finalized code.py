class Passenger:
    def __init__(self, traveler_name):
        self.name = traveler_name
        self.ticket_info = None
        self.boarding_info = None
        self.checked_bag = False
        self.assigned_seat = False

    def book_ticket(self, ticket):
        self.ticket_info = ticket

    def get_traveler_name(self):
        return self.name

    def get_ticket_info(self):
        return self.ticket_info

    def board_flight(self, boarding_pass):
        self.boarding_info = boarding_pass

    def get_boarding_info(self):
        return self.boarding_info

    def check_bag(self, status):
        self.checked_bag = status

    def has_bag_checked(self):
        return self.checked_bag

    def assign_seat(self, status):
        self.assigned_seat = status

    def has_assigned_seat(self):
        return self.assigned_seat

    def __str__(self):
        return f"Traveler: {self.name}"


class Flight:
    def __init__(self, flight_number, departure_location, arrival_location, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure = departure_location
        self.arrival = arrival_location
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.passengers = []

    def add_traveler(self, traveler):
        self.passengers.append(traveler)

    def get_flight_number(self):
        return self.flight_number

    def get_departure_location(self):
        return self.departure

    def get_arrival_location(self):
        return self.arrival

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def __str__(self):
        return f"Flight {self.flight_number} from {self.departure} to {self.arrival}, Departure: {self.departure_time}, Arrival: {self.arrival_time}"


class Ticket:
    def __init__(self, pass_number, pass_type, electronic_number, traveler, journey):
        self.pass_number = pass_number
        self.pass_type = pass_type
        self.electronic_number = electronic_number
        self.traveler = traveler
        self.journey = journey

    def get_pass_number(self):
        return self.pass_number

    def get_pass_type(self):
        return self.pass_type

    def get_electronic_number(self):
        return self.electronic_number

    def get_traveler(self):
        return self.traveler

    def get_journey(self):
        return self.journey

    def __str__(self):
        return f"Pass: {self.pass_number} Type: {self.pass_type}, Electronic Number: {self.electronic_number}"


class BoardingPass:
    def __init__(self, journey, traveler, gate, seat_num):
        self.journey = journey
        self.traveler = traveler
        self.gate = gate
        self.seat_num = seat_num

    def get_journey(self):
        return self.journey

    def get_traveler(self):
        return self.traveler

    def get_gate(self):
        return self.gate

    def get_seat_number(self):
        return self.seat_num

    def __str__(self):
        return f"Boarding Pass for {self.traveler} - Flight {self.journey.get_flight_number()}, Gate: {self.gate}, Seat: {self.seat_num}"
()


# Create a passenger
Hamda = Passenger("Hamda mohamed")

# Create a flight
flight1 = Flight("AA123", "New York", "London", "08:00 AM", "08:00 PM")

# Book a ticket for the passenger
ticket1 = Ticket("P12345", "Economy", "E12345", Hamda, flight1)
Hamda.book_ticket(ticket1)

# Issue a boarding pass to the passenger
boarding_pass1 = BoardingPass(flight1, Hamda, "G5", "12A")
Hamda.board_flight(boarding_pass1)

# Print the passenger's information
print(Hamda)

# Print the flight information
print(flight1)

# Print the ticket information
print(ticket1)

# Print the boarding pass information
print(boarding_pass1)

