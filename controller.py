import serial
import time

def col_to_bytearray(h):
    # Take int color (0xRRGGBB) and return bytearray([RR, GG, BB])
    return bytearray([h>>16, (h>>8)&0xFF, h&0xFF])

def dim_color(color, part):
    # Dim color bytearray
    return bytearray([round(i*part) for i in color])

def cols_to_col(r, g, b):
    if max(r, g, b) > 255 or min(r, g, b) < 0:
        raise ValueError("r, g, and b must be above 0 and below 256.")
    return round(r) << 16 | round(g) << 8 | round(b)

class Controller:
    def __init__(self, port='COM3'):
        print("Initializing serial port")
        ser = serial.Serial()
        ser.port = port
        ser.baudrate = 9600
        ser.parity = serial.PARITY_NONE
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.writeTimeout = 0
        ser.open()

        start_time = time.time()
        width = 25
        wait_time = 2
        print(f"[{' '*width}]", end="")
        while (time.time() - start_time) < wait_time: 
            part = (time.time() - start_time) / wait_time
            print("\rWaiting for Arduino to reset", end="   ")
            print(f"[{'='*round(width*part)}{' '*(width-round(width*part))}]", end="")
        print(end="\n")
        print("Resetting Color")
        ser.write(col_to_bytearray(0))

        self.ser = ser
    
    def send(self, data, dim=1, delay=250, wait=0, log=True):
        """
            Send data to serial.

            data:       int: 24-byte hex int in the form 0xRRGGBB
            data:  iterable: List of hex ints. Waits DELAY ms between each
            data: bytearray: 3-element bytearray (bytearray([RR, GG, BB]))

            dim: Float between 0 and 1 which indicates what brightness level of output

            delay: int: Waits this many ms between sending each elem of data if iterable

            wait: int: Waits this many ms after sending all data

            log: bool: Determines if the command should print info
        """

        if dim < 0 or dim > 1:
            raise ValueError("Dim value must be between 0 and 1.")
        
        if log: 
            ds = str(data)
            if type(data) == int:
                ds = '#'+hex(data)[2:].zfill(6)
            print(f"Sending color {ds} at {round(dim*100, 2)}% brightness for {wait/1000}s")
        if type(data) == int:
            self.ser.write(dim_color(col_to_bytearray(data), dim))
        elif hasattr(data, '__iter__'):
            for color in data:
                self.ser.write(dim_color(col_to_bytearray(color), dim))
                time.sleep(delay/1000)
        elif type(data) == bytearray:
            self.ser.write(dim_color(data, dim))
        else:
            raise TypeError(f"Controller.send does not take {type(data)} as a data argument.")

        time.sleep(wait/1000)