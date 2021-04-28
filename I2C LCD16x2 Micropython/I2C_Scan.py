# ----------------------------------------------------------------------------------------------------------------
# I2C_Scan.py sketch para escanear buscando dispositivos I2C conectados en I2C cero, localizandolos e imprimiendo
# las direcciones que encuentra en hexadecimal.
# Visita  https://jorgechac.blogspot.com venta de accesorios Arduino y Raspberry Pi Pico.
# ----------------------------------------------------------------------------------------------------------------

from machine import Pin                     # importamos la funcion pin del modulo machine
from machine import I2C                     # importamos la funcion I2C del modulo machine
import utime                                # 

sda = Pin(0)                                # objeto tipo pin que especifica el pin que se utilizará para SDA,
                                            # en este caso utilizaremos GP0 como sda

scl = Pin(1)                                # objeto tipo pin que especifica el pin que se utilizará para SCL,
                                            # en este caso utilizaremos GP1 como scl
                                            
i2c = I2C(0,sda=sda,scl=scl,freq=400000)    # le decimos que vamos a usar I2C cero y frecuencia max de 400k para scl
direccion = hex(i2c.scan()[0])              # primera posicion que entrega i2c.scan
print('La dirección I2C es ', direccion)