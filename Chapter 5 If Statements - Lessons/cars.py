# Chapter 5 If Statements, p.76

cars = ['toyota', 'bmw', 'nissan', 'mistubishi', 'mercedes']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# ln.6: if statement is used to check that if any car is 'bmw', then it needs
# to be printed all uppercase, or else (ln.8-9), the car name needs to be
# printed in title.
