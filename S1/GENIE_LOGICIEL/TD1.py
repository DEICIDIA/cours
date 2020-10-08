import abc

class TemperatureObserver:
	@abc.abstractmethod
	def update(event):
		pass

class WeatherStation(TemperatureObserver):
	__stationCounter=0
	def __init__(self):
		WeatherStation.__stationCounter+=1
		self.__number=WeatherStation.__stationCounter
	
	def displayTemperature(self, sensorName, temperature):
		print("Station", self.__number,"-",sensorName," > ",temperature, "degres")

		
class TemperatureAlarm(TemperatureObserver):
	def __init__(self, name):
		self.__name = name
	def update(event):
		print("aled")	

class Thermometer:
	def __init__(self, initalTemperature : float):
		self.temperature = initalTemperature
	def increaseTemperature(value : float):
		self.temperature += value 
		self.temperature += 0,1
	def decreaseTemperature(value : float):
		self.temperature -= value 
		self.temperature -= 0,1
	def getTemperature():
		return self.temperature 

class TemperatureChangeEvent:
	def __init__(self, temperature : float, name : str):
		self.temperature = temperature
		self.sensorName = name
	def getTemperature() -> float:
		return self.temperature
	def getSensorName() -> str:
		return self.name

class TemperatureSensor:
	def __init__(self, name):
		self.__name = name
		self.__temperature=0
		self.__weatherStations =[]	
	def getTemperature(self):
		return __temperature
	
	def setTemperature(self, temperature):
		self.__temperature = temperature
		t = TemperatureChangeEvent(temperature, self.__name)

	def addWeatherStation(self, ws):
		self.__weatherStations.append(ws)

ws1 = WeatherStation()
ws2 = WeatherStation()

ts1 = TemperatureSensor("Salon")
ts2 = TemperatureSensor("Cave")
ts3 = TemperatureSensor("Jardin")

ts1.addWeatherStation(ws1)
ts1.addWeatherStation(ws2)
ts2.addWeatherStation(ws2)
ts3.addWeatherStation(ws2)

print("Salon 20 degres - Cave 14 degres - Jardin 19 degres")
ts1.setTemperature(20)
ts2.setTemperature(14)
ts3.setTemperature(19)
print("Jardin 13 degres")
ts3.setTemperature(13)
print("Salon 19 degres")
ts1.setTemperature(19)
