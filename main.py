import requests
from datetime import datetime

def get_weather_data(date_time):
    CITY_NAME = "London"
    BASE_URL = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q={CITY_NAME},us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(BASE_URL)
    data = response.json()
    for i in data['list']:
        if i["dt_txt"] == date_time:
            return i
    return None

def get_temperature(data):
    return data["main"]["temp"]

def get_wind_speed(data):
    return data["wind"]["speed"]

def get_pressure(data):
    return data["main"]["pressure"]

def main():
    while True:
        print("="*100)
        print("Choose an option:\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        print("="*100)
        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting the program.")
            break

        elif choice in ["1", "2", "3"]:
            date_str = input("Enter the date (YYYY-MM-DD): ")
            try:
                date_time = datetime.strptime(date_str, "%Y-%m-%d") # To Validate date
                date_time = date_str+" 00:00:00"
                data = get_weather_data(date_time)

                if data is not None:
                    if choice == "1":
                        value = get_temperature(data)
                        unit = "°C"
                    elif choice == "2":
                        value = get_wind_speed(data)
                        unit = "m/s"
                    else:
                        value = get_pressure(data)
                        unit = "hPa"

                    print(f"{value} {unit}\n")
                else:
                    print("No Data Found")

            except ValueError:
                print("Invalid date format. Please try again.\n")
            except Exception as e:
                print(str(e))

if __name__ == "__main__":
    main()
