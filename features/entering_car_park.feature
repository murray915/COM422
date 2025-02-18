Feature: Vehicles entering the carpark

    Scenario: A car enters a car park with spaces
        Given an empty car park
        When a car with a reg number of "abc" enters the car park
        Then a car with a reg number of "abc" should occupy a space in the car park

    Scenario: A duplicate car tries to enter the car park
        Given a carpark that holds a car with the reg number "abc"
        When a second car with the reg number "abc" tries to enter the carpark
        Then only one car with the reg number "abc" should occupy a space in the car park