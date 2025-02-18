from behave import *
from car import car_park
from car import car

@given(u'an empty car park')
def step_impl(context):
    eliotts_front_garden = car_park(15)
    context.car_park = eliotts_front_garden

@when(u'a car with a reg number of "abc" enters the car park')
def step_impl(context):
    bob_car = car()


@then(u'a car with a reg number of "abc" should occupy a space in the car park')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a car with a reg number of "abc" should occupy a space in the car park')


@given(u'a carpark that holds a car with the reg number "abc"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a carpark that holds a car with the reg number "abc"')


@when(u'a second car with the reg number "abc" tries to enter the carpark')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a second car with the reg number "abc" tries to enter the carpark')


@then(u'only one car with the reg number "abc" should occupy a space in the car park')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then only one car with the reg number "abc" should occupy a space in the car park')