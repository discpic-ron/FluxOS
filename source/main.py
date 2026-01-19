from emulator import Emulator

vm = Emulator(32)

def boot():
  global vm
  while vm.running:
    vm.step()
