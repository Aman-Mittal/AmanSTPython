#program to to check number of minutes in a given year


year =int(input('Enter a Year:  '))

if (year%4 ==0 and year %100 != 0 or year %400 == 0):
    print('leap year')
    mins=366*24*60
    print(str(mins)+' minutes')
else:
    print('non leap year')
    mins=365*24*60
    print(str(mins)+' minutes')
