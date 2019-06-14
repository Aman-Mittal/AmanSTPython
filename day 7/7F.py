def KelvinToFahrenheit(Temperature):
    assert(Temperature>=0)
    res=((Temperature-273)*1.8)+32
    return res


try:
    print(KelvinToFahrenheit(273))
    print(KelvinToFahrenheit(505.78))
    print(KelvinToFahrenheit(-5))
except AssertionError as ob:
    print(ob)
print("thankyou")
          
