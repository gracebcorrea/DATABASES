class flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight Origin: {self.origin} ")
        print(f"Flight Destination: {self.Destination} ")
        print(f"Flight Duration: {self.Duration} minutes ")

    def delay(self, amount):
        self.duration += amount

def main():
    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.delay()
    f1.print_info()

if __name__ = "__main__":
    main()
