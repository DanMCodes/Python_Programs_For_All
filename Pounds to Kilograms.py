def poundsToMetric(pounds):
    kilograms = pounds / 2.2
    grams = kilograms * 1000
    return int(kilograms), grams % 1000

pounds = float(input("How many Pounds? "))
kg, g = poundsToMetric(pounds)
print('The amount of pounds you entered is {}. '\
      'This is {} kilograms and {} grams.'.format(pounds, kg, g))
