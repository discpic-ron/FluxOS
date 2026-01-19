import time

class Emulator:
  def __init__(self):
    self.ram = [0] * 50
    self.disk = []
    self.registers = {"A": 0}
    self.arrow = 0
    
  def boot(self):
    while True:
      ir = ram[self.arrow] # 'ir' stands for Instruction Register
      time.sleep(0.6)
      #if ir ==
