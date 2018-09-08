import MySQLdb 


# CREATE TABLE `temperature` ( `temperature_id` int(11) NOT NULL AUTO_INCREMENT, `temperature_c` float NOT NULL, `pressure` float NOT NULL, `dew_point` float NOT NULL, `altitude_m` float NOT NULL, `humidity` float NOT NULL, `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`temperature_id`)) 

def add_temperature(temp_data):
    try:
        db=MySQLdb.connect(user='root', db='pi_weather_temperature')
        with db.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO temperature VALUES (NULL, %s, %s, %s, %s, %s, NULL);"
            cursor.execute(sql % (float(temp_data['temperature_c']), 
                                 float(temp_data['pressure_hpa']),
                                 float(temp_data['dew_point_c']), 
                                 float(temp_data['altitude_m']),
                                 float(temp_data['humidity'])))
        db.commit()
    finally:
        db.close()
