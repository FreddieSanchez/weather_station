import os
import requests
import util

def update(temp_data):
    WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
    WU_station_id = os.getenv("WEATHER_UNDERGROUND_STATION_ID", "None")
    WU_station_pwd = os.getenv("WEATHER_UNDERGROUND_STATION_KEY", "None")
    WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
    date_str = "&dateutc=now"
    action_str = "&action=updateraw"

    r = requests.get(
            WUurl +
            WUcreds +
            date_str +
            "&baromin" + "{0:.2f}".format(util.hpa_to_in(temp_data['pressure_hpa'])) + 
            "&tempf=" + "{0:.2f}".format(util.c_to_f(temp_data['temperature_c'])) + 
            "&dewptf=" + "{0:.2f}".format(util.c_to_f(temp_data['dew_point_c']))+ 
            "&humidity=" + "{0:.2f}".format(temp_data['humidity'])+
            action_str)

    return r.status_code
