from src.core.task import Task 

import python_weather
import asyncio

class WeatherTask(Task):
    
    def __init__(self):
        super().__init__([
            "what is weather in",
            "what is meteo in"
            ])
        
    def action(self, text):
        city = text.split()[-1]
        loop = asyncio.get_event_loop()
        
        return loop.run_until_complete(self.getWeather(city))
        

    async def getWeather(self, city):

        # declare the client. format defaults to metric system (celcius, km/h, etc.)
        client = python_weather.Client(format=python_weather.METRIC)
        # fetch a weather forecast from a city
        weather = await client.find(city)
        # close the wrapper once done
        await client.close()
        # returns the current day's forecast temperature (int)
        return f"Actually, the weather in {city} is {weather.current.temperature} degrees and the sky is {weather.current.sky_text}"