def main():
    class Taxi:
        def __init__(self, name, fuel, price_per_km):
            self.name = name
            self.fuel = fuel
            self.odometer = 0
            self.price_per_km = price_per_km

        def __str__(self):
            return "{} - fuel={}, odometer={}, {}km on current fare, ${:.2f}/km".format(
                self.name, self.fuel, self.odometer, self.odometer, self.price_per_km
            )

        def get_fare(self, distance):
            fare = distance * self.price_per_km
            self.odometer += distance
            self.fuel -= distance
            return fare

    class SilverServiceTaxi(Taxi):
        flagfall = 4.50

        def __init__(self, name, fuel, price_per_km, fanciness):
            super().__init__(name, fuel, price_per_km)
            self.fanciness = fanciness

        def get_fare(self, distance):
            fare = super().get_fare(distance)
            total_fare = fare + self.flagfall * self.fanciness
            return total_fare

    def display_available_taxis(taxis):
        print("Taxis available:")
        for i, taxi in enumerate(taxis):
            print("{} - {}".format(i, taxi))

    taxis = [
        Taxi("Prius", 100, 1.23),
        SilverServiceTaxi("Limo", 100, 2.46, 2),
        SilverServiceTaxi("Hummer", 200, 4.92, 4)
    ]
    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    while True:
        print("Bill to date: ${:.2f}".format(bill))
        action = input("(q)uit, (c)hoose taxi, (d)rive\n>>> ").strip().lower()

        if action == 'q':
            print("Total trip cost: ${:.2f}".format(bill))
            print("Taxis are now:")
            for taxi in taxis:
                print(taxi)
            break
        elif action == 'c':
            display_available_taxis(taxis)
            choice = input("Choose taxi: ")
            if choice.isdigit():
                choice = int(choice)
                if 0 <= choice < len(taxis):
                    current_taxi = taxis[choice]
                    print("Bill to date: ${:.2f}".format(bill))
                else:
                    print("Invalid taxi choice")
        elif action == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance_input = input("Drive how far? ")
                if distance_input.isdigit():
                    distance = float(distance_input)
                    fare = current_taxi.get_fare(distance)
                    print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                    bill += fare
                else:
                    print("Invalid distance")


if __name__ == "__main__":
    main()
