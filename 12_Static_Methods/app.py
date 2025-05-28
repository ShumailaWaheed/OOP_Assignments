# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

temp_f = TemperatureConverter.celsius_to_fahrenheit(30)
print("Fahrenheit:", temp_f)
