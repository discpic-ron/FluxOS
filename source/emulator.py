import time
from vasm import set_reg, store, halt, jump, out

class Emulator:
  def __init__(self,lockers):
    self.ram = [0] * lockers
    self.disk = []
    self.registers = {"A": 0}
    self.arrow = 0
    self.running = True
    self.instructions = {
      "SET":set_rg,
      "STORE":store,
      "PRINT":out,
      "JUMP":jump,
      "HALT":halt
    }
    
  def step():
    instruction_line = self.ram[self.finger]
    parts = instruction_line.split()
    cmd_name = parts[0]
        
    if cmd_name in self.commands:
      args = parts[1:]
      self.commands[cmd_name](self, *args)
    else:
        self.finger += 1 # Skip empty lockers
