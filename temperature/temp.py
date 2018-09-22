import board
import busio
import time
import adafruit_bme280
import adafruit_mcp9808

SLEEP_TIME=30

def read_temp(bme280, mcp9808):

    # change this to match the location's pressure (hPa) at sea level
    bme280.sea_level_pressure = 1014.25

    reading = {  
            'temperature_c':  bme280.temperature,
            'temperature2_c':  mcp9808.temperature,
            'humidity': bme280.humidity,
            'altitude_m': bme280.altitude, 
            'pressure_hpa': bme280.pressure,
            'dew_point_c': bme280.dew_point, 
            'timestamp': time.localtime()
            }

    return reading

if __name__ == '__main__':
    # Create library object using our Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    mcp9808 = adafruit_mcp9808.MCP9808(i2c)

    while True:
        read_temp(bme280, mcp9808)
        time.sleep(SLEEP_TIME)
	

