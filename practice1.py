import random

weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Windy", "Snowy", "Foggy", "Humid"]
advice = {
    "Sunny": "Wear sunglasses and stay hydrated!",
    "Cloudy": "Might need a light jacket.",
    "Rainy": "Don't forget your umbrella!",
    "Stormy": "Better to stay indoors if possible.",
    "Windy": "Hold onto your hat!",
    "Snowy": "Wear warm clothes and boots.",
    "Foggy": "Drive carefully!",
    "Humid": "Stay cool and drink water."
}

def generate_temperature(condition):
    if condition == "Snowy":
        return random.randint(-10, 2)
    elif condition == "Sunny":
        return random.randint(25, 40)
    elif condition in ["Rainy", "Stormy"]:
        return random.randint(15, 25)
    elif condition in ["Windy", "Cloudy", "Foggy"]:
        return random.randint(10, 22)
    elif condition == "Humid":
        return random.randint(26, 35)
    else:
        return random.randint(0, 30)

def c_to_f(celsius):
    return celsius * 9 / 5 + 32

def generate_humidity():
    return random.randint(30, 90)  # percentage

def generate_wind_speed():
    return round(random.uniform(0, 20), 1)  # km/h

def is_valid_city(city):
    return city.replace(" ", "").isalpha()

def print_forecast(city, days):
    print(f"\n📍 Weather forecast for {city.capitalize()} ({days} day{'s' if days > 1 else ''}):")
    for day in range(1, days + 1):
        condition = random.choice(weather_conditions)
        temp_c = generate_temperature(condition)
        temp_f = c_to_f(temp_c)
        humidity = generate_humidity()
        wind = generate_wind_speed()
        print(f"\n Day {day}:")
        print(f"  Condition   : {condition}")
        print(f"  Temperature : {temp_c}°C / {temp_f:.1f}°F")
        print(f"  Humidity    : {humidity}%")
        print(f"  Wind Speed  : {wind} km/h")
        print(f"  Advice      : {advice[condition]}")

def main():
    print("=== Enhanced Simulated Weather Forecast App ===")
    while True:
        city = input("\nEnter a city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("👋 Thanks for using the Weather App!")
            break
        elif not city or not is_valid_city(city):
            print("⚠ Please enter a valid city name (letters and spaces only).")
            continue
        
        while True:
            try:
                days = int(input("How many days forecast? (1-7): "))
                if 1 <= days <= 7:
                    break
                else:
                    print("⚠ Please enter a number between 1 and 7.")
            except ValueError:
                print("⚠ That’s not a valid number.")
        
        print_forecast(city, days)

if __name__ == "__main__":
    main()
