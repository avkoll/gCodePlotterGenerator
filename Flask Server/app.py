from flask import Flask, render_template, request, redirect, url_for, flash
import os
import serial

app = Flask(__name__)
app.secret_key = 'raspberrypitableplotter'

GCODE_DIR = os.path.join(app.static_folder, 'gcode_files')
SERIAL_PORT = '/dev/ttyUSB0'  # Adjust this to your serial port
BAUD_RATE = 115200

@app.route('/')
def index():
    files = os.listdir(GCODE_DIR)
    return render_template('index.html', files=files)

@app.route('/send_gcode', methods=['POST'])
def send_gcode():
    selected_file = request.form['gcode_file']
    file_path = os.path.join(GCODE_DIR, selected_file)

    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            with open(file_path, 'r') as f:
                for line in f:
                    command = line.strip()
                    if command:
                        print(f"Sending: {command}")
                        ser.write((command + '\n').encode())
                        response = ser.readline().decode().strip()
                        print(f"Response: {response}")
                        if "error" in response.lower() or "alarm" in response.lower():
                            flash(f"Error in G-code execution: {response}", 'error')
                            break
        flash('G-code sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send G-code: {str(e)}', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)