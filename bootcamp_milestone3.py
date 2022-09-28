from urllib.request import urlopen
import json


def get_ip():
    url = "http://checkip.dyndns.org"
    data = urlopen(url).read()
    ip_address = data[-30:-16]
    return ip_address


def get_weather(ip_address):
    end_point = "http://api.worldweatheronline.com/premium/v1/weather.ashx?"
    query = "key=f2568645186a4838a9a45708222809&q=" + str(ip_address.decode()) + "&num_of_days=0&format=json"
    url = end_point + query
    json_data = urlopen(url).read()
    data = json.loads(json_data)
    current_weather = data['data']['current_condition'][0]
    return current_weather


def print_weather(data):
    print(f"""
    Weather : {data['weatherDesc'][0]['value']}
    Temperatue : {data['temp_C']}
    Wind : {data['windspeedKmph']} Kmph {data['winddir16Point']}
    Humidity : {data['humidity']}
    Precipitation : {data['precipMM']} MM
    """)


def main():
    print("\nGetting weather information for your location...")
    ip_address = get_ip()
    data = get_weather(ip_address)
    print_weather(data)


if __name__ == "__main__":
    main()