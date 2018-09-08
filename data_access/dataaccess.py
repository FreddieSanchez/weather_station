import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
        user='root',
        password='',
        db='pi_wather_temperature',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

# CREATE TABLE `temperature` ( `temperature_id` int(11) NOT NULL AUTO_INCREMENT, `temperature_c` float NOT NULL, `pressure` float NOT NULL, `dew_point` float NOT NULL, `altitude_m` float NOT NULL, `humidity` float NOT NULL, `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (`temperature_id`)) 

def add_temperature(temp_data):
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO temperature(NULL, %s, %s, %s, %s, %s, NULL)"

            cursor.execute(sql, (temp_data.temperature_c, 
                                 temp_data.pressure_hpa,
                                 temp_data.dew_point, 
                                 temp_data.altitude,
                                 temp_data.humidity))
        connection.commit()
    finally:
        connection.close()
