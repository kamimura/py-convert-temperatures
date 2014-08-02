#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# added a new temperature scale, two if statements need to add

def convert_to_celsius(t, source):
    if source == "Kelvin":
        return t - 273.15
    elif source == "Celsius":
        return t
    elif source == "Fahrenheit":
        return (t - 32) * 5 / 9
    elif source == "Rankine":
        return (t - 491.67) * 5 / 9
    elif source == "Delisle":
        return 100 - t * 2 / 3
    elif source == "Newton":
        return t * 100 / 33
    elif source == "Reaumur":
        return t * 5 / 4
    elif source == "Romer":
        return (t - 7.5) * 40 / 21
    else:
        raise Exception("convert_to_celsius: {0}".format(source))

def convert_from_celsius(t, target):
    if target == "Kelvin":
        return t + 273.15
    elif target == "Celsius":
        return t
    elif target == "Fahrenheit":
        return t * 9 / 5 + 32
    elif target == "Rankine":
        return (t + 273.15) * 9 / 5
    elif target == "Delisle":
        return (100 - t) * 3 / 2
    elif target == "Newton":
        return t * 33 / 100
    elif target == "Reaumur":
        return t * 4 / 5
    elif target == "Romer":
        return t * 21 / 40 + 7.5
    else:
        raise Exception("convert_from_celsius: {0}".format(target))

def convert_temperatures(t, source, target):
    return convert_from_celsius(convert_to_celsius(t, source), target)

if __name__ == '__main__':
    units = ["Kelvin", "Celsius", "Fahrenheit", "Rankine", "Delisle","Newton",
             "Reaumur", "Romer"]

    # http://en.wikipedia.org/wiki/Comparison_of_temperature_scales#Comparison_of_temperature_scales
    print("Absolute zero")
    for target in units:
        print("{0}: {1:.2f}".format(
            target, convert_temperatures(0, "Kelvin", target)))
    print("Ice melts")
    for target in units:
        print("{0}: {1:.2f}".format(
            target, convert_temperatures(32, "Fahrenheit", target)))
