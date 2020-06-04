class flight:
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

 class Flight:

      # assume same __init__ method

      def print_info(self):
          print(f"Flight origin: {self.origin}")
          print(f"Flight destination: {self.destination}")
          print(f"Flight duration: {self.duration}")

  def main():
      f1 = Flight(origin="New York", destination="Paris", duration=540)
      f1.print_info()
