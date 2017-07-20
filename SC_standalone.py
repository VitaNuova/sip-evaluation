import time
import subprocess
import os

result_file = open("results.json", "a")

# protection overhead
def measure_protection_time(args):
   start = time.time()
   p = subprocess.Popen(args, stdout = subprocess.PIPE)
   out, err = p.communicate()
   end = time.time()
   return end - start

def measure_runtime_overhead(arg_before, arg_after):
   start = time.time()
   p = subprocess.Popen(arg_before, stdout = subprocess.PIPE)
   out, err = p.communicate()
   end = time.time()
   runtime_before = end - start

   start = time.time()
   p = subprocess.Popen(arg_after, stdout = subprocess.PIPE)
   out, err = p.communicate()
   end = time.time()
   runtime_after = end - start
   runtime_overhead = (runtime_after - runtime_before) /  runtime_before * 100
   return runtime_overhead

def measure_binary_overhead(path_before, path_after):
   size_before = os.path.getsize(path_before)
   size_after = os.path.getsize(path_after)
   size_overhead = (size_after - size_before) / size_before * 100
   return size_overhead

def create_snippet(program, composition, protection_time, runtime_overhead, memory_overhead, size_overhead):
   return '{\n"program": "' + program + '",\n"Results": [\n\t\t{\n\t\t"Composition": "' + composition + '",\n\t\t"ProtectionTime": ' + str(protection_time) + ',\n\t\t"RuntimeOverhead": ' + str(runtime_overhead) + ',\n\t\t"MemoryOverhead": ' + str(memory_overhead) + ',\n\t\t"BinarySizeOverhead": ' + str(size_overhead) + '\n\t\t}\n\t]\n}\n' 

# SC
# micro-snake
protection_time = measure_protection_time(["src/self-checksumming", "input_programs/snake", "1", "snake"])
print('snake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/snake", "input_programs/snake_modified")
print('size overhead ' + str(size_overhead) + '%')

snippet = create_snippet('micro-snake', 'SC', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

# csnake
protection_time = measure_protection_time(["src/self-checksumming", "input_programs/csnake", "1", "csnake"])
print('csnake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/csnake", "input_programs/csnake_modified")
print('size overhead ' + str(size_overhead) + '%')

snippet = create_snippet('csnake', 'SC', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

# tetris
protection_time = measure_protection_time(["src/self-checksumming", "input_programs/tetris", "1", "tetris"])
print('tetris protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/tetris", "input_programs/tetris_modified")
print('size overhead ' + str(size_overhead) + '%')

snippet = create_snippet('tetris', 'SC', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

'''
# zopfli
protection_time = measure_protection_time(["src/self-checksumming", "input_programs/zopfli", "1", "zopfli"])
print('zopfli protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/zopfli.in", "input_programs/zopfli"], ["python", "inputs/ptypipe.py", "inputs/zopfli.in", "input_programs/zopfli_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/zopfli", "input_programs/zopfli_modified")
print('size overhead ' + str(size_overhead) + '%')

snippet = create_snippet('zopfli', 'SC', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)
'''


result_file.close()
