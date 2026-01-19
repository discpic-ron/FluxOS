# instructions
def set_reg(vm,value):
  vm.registers["A"] = value
  vm.arrow += 1
  
def store(vm,index):
  idx = int(index)
  vm.ram[idx] = vm.registers["A"]
  vm.arrow += 1
  
def load(vm,index):
  idx = int(index)
  value = vm.ram[idx]
  vm.registers["A"] = value
  print(f"[Action] Loaded '{value}' from locker {idx} into Register A")
  vm.arrow += 1
  
def v_input(vm,user_input):
  vm.registers["A"] = user_input
  vm.arrow += 1
  
def halt(vm):
  vm.running = False

def jump(vm,index):
  vm.arrow = int(index)

def out(vm):
  print(f"[DISPLAY]: {vm.registers['A']}")
  vm.arrow += 1
  
def check(vm,target_value, jump_location):
  if str(vm.registers["A"]) == str(target_value):
    vm.arrow = int(jump_location)
    print(f"  [Logic] Match found! Jumping to {jump_location}")
  else:
    vm.arrow += 1
