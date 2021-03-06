#import time
#import subprocess
#import os

import common

result_file = open("results.json", "a")
'''
def measure_protection_time(args):
   start = time.time()
   FNULL = open(os.devnull, 'w')
   p = subprocess.Popen(args, stdout = FNULL, stderr = FNULL)
   out, err = p.communicate()
   end = time.time()
   return end - start
'''
'''
def measure_runtime_overhead(arg_before, arg_after):
   start = time.time()
   FNULL = open(os.devnull, 'w')
   p = subprocess.Popen(arg_before, stdout = FNULL, stderr = FNULL)
   out, err = p.communicate()
   end = time.time()
   runtime_before = end - start
   print('arg_before ' + str(arg_before))
   print('run_before ' + str(runtime_before)) 
   start = time.time()
   print('arg_after ' + str(arg_after))
   p = subprocess.Popen(arg_after, stdout = FNULL, stderr = FNULL)
   out, err = p.communicate()
   end = time.time()
   runtime_after = end - start
   print('run_after ' + str(runtime_after))
   runtime_overhead = (runtime_after - runtime_before) /  runtime_before * 100
   return runtime_overhead

def measure_binary_overhead(path_before, path_after):
   size_before = os.path.getsize(path_before)
   size_after = os.path.getsize(path_after)
   size_overhead = (size_after - size_before) / float(size_before) * 100
   return size_overhead

def measure_memory_overhead(cmd_before, cmd_after):
   cmd_before = ["/usr/bin/time", "-f", "%M"] + cmd_before
   FNULL = open(os.devnull, 'w')
   p = subprocess.Popen(cmd_before, stdout = FNULL, stderr = subprocess.PIPE)
   out, mem_before = p.communicate()
   print 'mem_before ' + mem_before
   cmd_after = ["/usr/bin/time", "-f", "%M"] + cmd_after
   p = subprocess.Popen(cmd_after, stdout = FNULL, stderr = subprocess.PIPE)
   out, mem_after = p.communicate()
   print 'mem_after ' + mem_after
   mem_overhead = (float(mem_after) - float(mem_before)) / float(mem_before) * 100 
   return mem_overhead
'''
'''
def create_snippet(program, composition, protection_time, runtime_overhead, memory_overhead, size_overhead):
   return '{\n"program": "' + program + '",\n"Results": [\n\t\t{\n\t\t"Composition": "' + composition + '",\n\t\t"ProtectionTime": ' + str(protection_time) + ',\n\t\t"RuntimeOverhead": ' + str(runtime_overhead) + ',\n\t\t"MemoryOverhead": ' + str(memory_overhead) + ',\n\t\t"BinarySizeOverhead": ' + str(size_overhead) + '\n\t\t}\n\t]\n}\n' 
'''
# SC
# micro-snake
protection_time = common.measure_protection_time(["SC-build/src/self-checksumming", "input_programs/snake", "1", "snake"])
print('snake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/snake", "input_programs/snake_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('micro-snake', 'SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# csnake
protection_time = common.measure_protection_time(["SC-build/src/self-checksumming", "input_programs/csnake", "1", "csnake"])
print('csnake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/csnake", "input_programs/csnake_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('csnake', 'SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# tetris
protection_time = common.measure_protection_time(["SC-build/src/self-checksumming", "input_programs/tetris", "1", "tetris"])
print('tetris protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/tetris", "input_programs/tetris_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('tetris', 'SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)
'''
# OH
# micro-snake
protection_time = measure_protection_time(["./run-oh-eval.sh", "/home/sip/dataset/src/micro-snake/snake.c", "inputs/micro-snake.in"])
print('OH snake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/snake", "OH-build/protected")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('micro-snake', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)


# c-snake
protection_time = measure_protection_time(["./run-oh-eval.sh", "/home/sip/dataset/src/c-snake/snake.c", "inputs/c-snake.in"])
print('OH csnake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "OH-build/protected"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/csnake", "OH-build/protected")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "OH-build/protected"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('c-snake', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# tetris
protection_time = measure_protection_time(["./run-oh-eval.sh", "/home/sip/dataset/src/tetris/tetris.c", "inputs/tetris.in"])
print('tetris protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "OH-build/protected"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/tetris", "OH-build/protected")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "OH-build/protected"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('tetris', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# zopfli
protection_time = measure_protection_time(["./run-oh-zopfli.sh", "./zopfli-whole.bc"])
print('zopfli protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["input_programs/zopfli", "inputs/zopfli.in"], ["OH-build/protected", "inputs/zopfli.in"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/zopfli", "OH-build/protected")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["input_programs/zopfli", "inputs/zopfli.in"], ["OH-build/protected", "inputs/zopfli.in"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('zopfli', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# CFI
# micro-snake
protection_time = measure_protection_time(["./compile.sh", "inputs/snake.bc", "CFI-build/snake", "snake_sens_list.txt"])
print('CFI snake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "CFI-build/snake"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/snake", "CFI-build/snake")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "CFI-build/snake"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('micro-snake', 'CFI', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

# csnake
protection_time = measure_protection_time(["./compile.sh", "inputs/csnake.bc", "CFI-build/csnake", "c_snake_sens_list.txt"])
print('csnake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "CFI-build/csnake"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/csnake", "CFI-build/csnake")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "CFI-build/csnake"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('csnake', 'CFI', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

# tetris
protection_time = measure_protection_time(["./compile.sh", "inputs/tetris.bc", "CFI-build/tetris","tetris_sens_list.txt"])
print('tetris protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "CFI-build/tetris"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/tetris", "CFI-build/tetris")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "CFI-build/tetris"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('tetris', 'CFI', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

# OH + SC
# micro-snake
oh_protection_time = measure_protection_time(["./run-oh-eval.sh", "/home/sip/dataset/src/micro-snake/snake.c", "inputs/micro-snake.in"])
sc_protection_time = measure_protection_time(["SC-build/src/self-checksumming", "OH-build/protected", "1", "protected"])
protection_time = oh_protection_time + sc_protection_time
print('OH + SC snake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/snake", "OH-build/protected_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('micro-snake', 'OH+SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# c-snake
oh_protection_time = measure_protection_time(["./run-oh-eval.sh", "/home/sip/dataset/src/c-snake/snake.c", "inputs/c-snake.in"])
sc_protection_time = measure_protection_time(["SC-build/src/self-checksumming", "OH-build/protected", "1", "protected"])
protection_time = oh_protection_time + sc_protection_time
print('OH + SC csnake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "OH-build/protected_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/csnake", "OH-build/protected_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "OH-build/protected_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('c-snake', 'OH+SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# tetris
oh_protection_time = measure_protection_time(["./run-oh-eval.sh", "/home/sip/dataset/src/tetris/tetris.c", "inputs/tetris.in"])
sc_protection_time = measure_protection_time(["SC-build/src/self-checksumming", "OH-build/protected", "1", "protected"])
protection_time = oh_protection_time + sc_protection_time
print('OH + SC tetris protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "OH-build/protected_modified"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/tetris", "OH-build/protected_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "OH-build/protected_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('tetris', 'OH+SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

# CFI + OH
# micro-snake
protection_time = measure_protection_time(["./cfi_oh.sh", "inputs/snake.bc", "snake_sens_list.txt", "inputs/micro-snake.in"])
print('CFI + OH snake protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/cfi_oh_protected"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("input_programs/snake", "OH-build/cfi_oh_protected")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/cfi_oh_protected"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = create_snippet('micro-snake', 'CFI+OH', protection_time, runtime_overhead, memory_overhead, size_overhead)

result_file.write(snippet)


# RC
# zopfli
p = subprocess.Popen(["cp", "config_zopfli.json", "/home/sip/protection/stins4llvm"], stdout = subprocess.PIPE)
out, err = p.communicate()

os.chdir("/home/sip/protection/stins4llvm")
#p = subprocess.Popen(["cd", "/home/sip/protection/stins4llvm"], stdout = subprocess.PIPE)
#out, err = p.communicate()

protection_time = measure_protection_time(["./run.sh", "-f", "config_zopfli.json"])
print('RC zopfli protection time ' + str(protection_time))

runtime_overhead = measure_runtime_overhead(["/home/sip/protection/sip-evaluation/input_programs/zopfli","/home/sip/dataset/inputs/zopfli.in"], ["build/zopfli-rewritten", "/home/sip/dataset/inputs/zopfli.in"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = measure_binary_overhead("/home/sip/protection/sip-evaluation/input_programs/zopfli", "build/zopfli-rewritten")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = measure_memory_overhead(["/home/sip/protection/sip-evaluation/input_programs/zopfli","/home/sip/dataset/inputs/zopfli.in"], ["build/zopfli-rewritten", "/home/sip/dataset/inputs/zopfli.in"])
print('memory overhead ' + str(memory_overhead) + '%')

os.chdir("/home/sip/protection/sip-evaluation")

snippet = create_snippet('micro-snake', 'RC', protection_time, runtime_overhead, memory_overhead, size_overhead)

result_file.write(snippet)
'''
result_file.close()
