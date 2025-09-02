from batt import INA219
import json

ina219 = INA219(addr=0x42)
bus_voltage = ina219.getBusVoltage_V()
shunt_voltage = ina219.getShuntVoltage_mV() / 1000
current = ina219.getCurrent_mA()
power = ina219.getPower_W()
p = (bus_voltage - 6)/2.4*100
if p > 100: p = 100
if p < 0: p = 0

stats = {
    'load_voltage': round(bus_voltage, 3),
    'shunt_voltage': round(shunt_voltage, 6),
    'current': round(current/1000, 6),
    'power': round(power, 3),
    'percent': round(p, 1)
}

print(json.dumps(stats))
