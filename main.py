import board
import busio
import time
import adafruit_bme280
import adafruit_mcp9808
import temperature.temp as temp
import data_access.dataaccess as da
import pws.pws as pws

SLEEP_TIME=30

if __name__ == "__main__":
    # Create library object using our Bus I2C port
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    mcp9808 = adafruit_mcp9808.MCP9808(i2c)

    while True:
        # grab the temp data from the sensors
        temp_data = temp.read_temp(bme280, mcp9808)
        
        # add the data to the database
        da.add_temperature(temp_data)

        # Update the Private Weather Station site
        pws.update(temp_data)

        time.sleep(SLEEP_TIME)
	


