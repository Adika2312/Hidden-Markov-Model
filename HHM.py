import random
def write_weather_to_file(currentWeather, WEATHER_OUT):
    """"write to the file the letter that corresponds to the current weather"""

    if currentWeather == PLEASANT:
        WEATHER_OUT.write("P")
    elif currentWeather == HOT:
        WEATHER_OUT.write("H")
    else:
        WEATHER_OUT.write("C")


def determine_game_based_of_weather_and_write_to_file(currentWeather, GAME_OUT):
    """predict the game based on the current weather, and write the correct game letter to the file"""

    numberLottery = random.uniform(0, 1)

    if currentWeather == PLEASANT:
        if numberLottery < 0.6:
            GAME_OUT.write("B")
        elif numberLottery < 0.9:
            GAME_OUT.write("S")
        else:
            GAME_OUT.write("C")

    elif currentWeather == HOT:
        if numberLottery < 0.1:
            GAME_OUT.write("B")
        elif numberLottery < 0.2:
            GAME_OUT.write("S")
        else:
            GAME_OUT.write("C")

    else:
        if numberLottery < 0.7:
            GAME_OUT.write("B")
        elif numberLottery < 0.9:
            GAME_OUT.write("S")
        else:
            GAME_OUT.write("C")


def determine_weather_based_of_last_weather_and_write_to_file(currentWeather, WEATHER_OUT):
    """determine the current weather_based of the last weather and write the currect letter to the file"""

    numberLottery = random.uniform(0, 1)

    if currentWeather == PLEASANT:
        if numberLottery < 0.2:
            WEATHER_OUT.write("C")
            return CLOUDY
        elif numberLottery < 0.7:
            WEATHER_OUT.write("P")
            return PLEASANT
        else:
            WEATHER_OUT.write("H")
            return HOT


    elif currentWeather == HOT:
        if numberLottery < 0.4:
            WEATHER_OUT.write("C")
            return CLOUDY
        elif numberLottery < 0.6:
            WEATHER_OUT.write("P")
            return PLEASANT
        else:
            WEATHER_OUT.write("H")
            return HOT

    else:
        if numberLottery < 0.5:
            WEATHER_OUT.write("C")
            return CLOUDY
        elif numberLottery < 0.8:
            WEATHER_OUT.write("P")
            return PLEASANT
        else:
            WEATHER_OUT.write("H")
            return HOT


PLEASANT = 1
HOT = 2
CLOUDY = 3

GAME_OUT = open("GAME_OUT.txt", "w")
WEATHER_OUT = open("WEATHER_OUT.txt", "w")

currentWeather = random.randint(1, 3)
write_weather_to_file(currentWeather, WEATHER_OUT)
determine_game_based_of_weather_and_write_to_file(currentWeather, GAME_OUT)

numOfDays = 200

for i in range(numOfDays - 1):
    currentWeather = determine_weather_based_of_last_weather_and_write_to_file(currentWeather, WEATHER_OUT)
    determine_game_based_of_weather_and_write_to_file(currentWeather, GAME_OUT)

WEATHER_OUT.close()
GAME_OUT.close()