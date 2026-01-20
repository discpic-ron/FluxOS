from emulator import Emulator

def load_OS(vm, instruction_list, start_at=0):
  for i, instruction in enumerate(instruction_list):
    vm.ram[i + start_at] = instruction
  print(f"KERNEL: Loaded {len(instruction_list)} instructions starting at Locker {start_at}")
  
instruction_list = [
   "SET A FluXOS_v1.0_2026",
   "PRINT",
]
load_OS(vm, instruction_list)
