from django.shortcuts import render
from .models import Altitude, AtmosphericVariables


def calculate_atmospheric_variables(request):
    atmospheric_variables = None
    if request.method == 'POST':
        altitude_value = request.POST.get('altitude')
        altitude = Altitude.objects.create(value=altitude_value)
        temperature = calculate_temperature(altitude_value)
        pressure = calculate_pressure(altitude_value)
        density = calculate_density(altitude_value, temperature, pressure)
        atmospheric_variables = AtmosphericVariables.objects.create(
            altitude=altitude,
            temperature=temperature,
            pressure=pressure,
            density=density,
        )
    context = {
        'atmospheric_variables': atmospheric_variables,
    }
    return render(request, 'calculator/calculate.html', context)


def calculate_temperature(altitude):
    # Implement the temperature calculation based on the input altitude.
    # Here's an example calculation using the ISA model:
    altitude = int(altitude)
    if altitude < 11000:
        temperature = 288.15 - 0.0065 * altitude
    else:
        temperature = 216.65
    return temperature


def calculate_pressure(altitude):
    # Implement the pressure calculation based on the input altitude.
    # Here's an example calculation using the ISA model:
    altitude = int(altitude)
    if altitude < 11000:
        pressure = 101325 * (288.15 / (288.15 - 0.0065 *
                             altitude)) ** (-9.81 / (0.0065 * 287))
    else:
        pressure = 22632 * 10 ** (-11.1 * (altitude / 1000 - 11))

    return pressure


def calculate_density(altitude, temperature, pressure):
    # Implement the density calculation based on the input altitude, temperature, and pressure.
    # Here's an example calculation using the ideal gas law:
    density = pressure / (287.058 * temperature)

    return density
