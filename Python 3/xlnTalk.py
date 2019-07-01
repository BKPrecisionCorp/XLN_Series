#   8500MostlyJustTrigger.py
#
#   Copyright {2017} {B&K Precision Corporation}

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
import serial
import time

ser = serial.Serial()
ser.baudrate = 57600
ser.port = 'COM3'
ser.timeout = 2
print(ser)
ser.open()
print(ser.is_open)
ser.write("*idn\n".encode())
print("Wrote")
resp = ser.read(1)
print("read")
ser.close()
