# ----------------------------------------------------------------------------------------------------------------
# Implementa una pantalla LCD de caracteres HD44780 conectada a través de PCF8574 en I2C
# Visita https://jorgechac.blogspot.com Venta de accesorios Arduino/Raspberry Pi Pico
# ----------------------------------------------------------------------------------------------------------------

from time import sleep_ms
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd

# El PCF8574 tiene una dirección seleccionable por jumper: 0x20 a 0x27
# dependiendo del fabricante del LCD, la direccion 0x27 puede cambiar, utilice el I2C_Scan.py primero por favor!

DEFAULT_I2C_ADDR = 0x27

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(0,scl=Pin(1), sda=Pin(0), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.putstr("PROTOCOLO I2C\nLCD 2x16")
    sleep_ms(3000)
    lcd.clear()
    count = 0
    while True:
        lcd.move_to(0, 0)
        lcd.putstr("  SUBSCRIBETE!  ")
        sleep_ms(1000)
        lcd.clear()
        sleep_ms(1000)

test_main()