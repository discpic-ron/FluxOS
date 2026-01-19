from emulator import Emulator

# instructions
def set_reg(vm,value):
  vm.registers["A"] = value
  vm.arrow += 1
  
def store(vm,index):
  idx = int(index)
  vm.ram[idx] = vm.registers["A"]
  vm.arrow += 1

def halt(vm):
  vm.running = False

def jump(vm,index):
  vm.arrow = int(index)

def out(vm):
  print(f"[DISPLAY]: {vm.registers['A']}"})
  vm.arrow += 1
