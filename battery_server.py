from flask import Flask, jsonify
from batt import INA219

app = Flask(__name__)
ina219 = INA219(addr=0x42)

@app.route('/api/voltage')
def get_voltage():
    bus_voltage = ina219.getBusVoltage_V()
    return jsonify({'voltage': round(bus_voltage, 3)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
