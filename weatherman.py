import forecastio
from geopy.geocoders import Nominatim
from twilio.rest import Client

def send_weather(address):
    api_key = "<API KEY>"   
    location = Nominatim().geocode(address)
    forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
    forecast2 = forecastio.load_forecast(api_key, location.latitude, location.longitude).hourly()
    if location: 
        return f"Good morning! It is currently {forecast.summary}, {forecast.temperature} degrees. Today it's going to be {forecast2.summary}"
    else:
        return "Location not found."
    
def send_text():
    account = "<TWILIO ACCOUNT NO.>"
    token = "<TWILIO ACCT TOKEN>"
    client = Client(account, token)
    message = client.messages.create(to="<RECEIVING NUMBER>", from_="<TWILIO SENDING NUMBER>", body=text)

searchlocation = input("Where are you right now? ")
text = send_weather(searchlocation)

send_text()

