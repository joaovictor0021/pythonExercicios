def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

temperatura = float(input("Digite a temperatura: "))
scale_thermometric = input("Digite a unidade de temperatura (C, F, K): ").upper()

if scale_thermometric == 'C':
    temperatura_fahrenheit = celsius_para_fahrenheit(temperatura)
    temperatura_kelvin = celsius_para_kelvin(temperatura)
    print(f"\n{temperatura:.0f} Celsius é equivalente a:")
    print(f"{temperatura_fahrenheit:.2f} Fahrenheit")
    print(f"{temperatura_kelvin:.2f} Kelvin")
elif scale_thermometric == 'F':
    temperatura_celsius = fahrenheit_para_celsius(temperatura)
    temperatura_kelvin = fahrenheit_para_kelvin(temperatura)
    print(f"\n{temperatura:.2f} Fahrenheit é equivalente a:")
    print(f"{temperatura_celsius:.2f} Celsius")
    print(f"{temperatura_kelvin:.2f} Kelvin")
elif scale_thermometric == 'K':
    temperatura_celsius = kelvin_para_celsius(temperatura)
    temperatura_fahrenheit = kelvin_para_fahrenheit(temperatura)
    print(f"\n{temperatura:.2f} Kelvin é equivalente a:")
    print(f"{temperatura_celsius:.2f} Celsius")
    print(f"{temperatura_fahrenheit:.2f} Fahrenheit")
else:
    print("Unidade de temperatura inválida. Use C, F ou K.")