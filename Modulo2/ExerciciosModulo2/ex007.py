"""
Desafio: Sistema de Monitoramento de Temperatura 
Você está desenvolvendo uma classe chamada TemperatureMonitor para monitorar sensores 
de temperatura em uma rede de dispositivos inteligentes. 
A temperatura é sempre armazenada internamente em Celsius, mas usuários podem acessar e 
definir a temperatura também em Fahrenheit.

"""
class TemperatureMonitor:
    def __init__(self, celsius):
        self.celsius = celsius  # usa o setter para validar

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return round((self._celsius * 9 / 5) + 32, 2)

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius = (value - 32) * 5 / 9
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = celsius

temp = TemperatureMonitor(25)
print(temp.celsius)      
print(temp.fahrenheit)   

temp.fahrenheit = 98.6
print(temp.celsius)      

temp.celsius = -300      


        
