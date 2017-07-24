import common
import subprocess
import os

result_file = open("results.json", "a")

# CFI + OH
# micro-snake
protection_time = common.measure_protection_time(["./cfi_oh.sh", "inputs/snake.bc", "snake_sens_list.txt", "inputs/micro-snake.in"])
print('CFI + OH snake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/snake", "OH-build/protected")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('micro-snake', 'CFI+OH', protection_time, runtime_overhead, memory_overhead, size_overhead)

result_file.write(snippet)

# RC
# zopfli
p = subprocess.Popen(["cp", "config_zopfli.json", "/home/sip/protection/stins4llvm"], stdout = subprocess.PIPE)
out, err = p.communicate()

os.chdir("/home/sip/protection/stins4llvm")
#p = subprocess.Popen(["cd", "/home/sip/protection/stins4llvm"], stdout = subprocess.PIPE)
#out, err = p.communicate()

protection_time = common.measure_protection_time(["./run.sh", "-f", "config_zopfli.json"])
print('RC zopfli protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["/home/sip/protection/sip-evaluation/input_programs/zopfli","/home/sip/dataset/inputs/zopfli.in"], ["build/zopfli-rewritten", "/home/sip/dataset/inputs/zopfli.in"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("/home/sip/protection/sip-evaluation/input_programs/zopfli", "build/zopfli-rewritten")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["/home/sip/protection/sip-evaluation/input_programs/zopfli","/home/sip/dataset/inputs/zopfli.in"], ["build/zopfli-rewritten", "/home/sip/dataset/inputs/zopfli.in"])
print('memory overhead ' + str(memory_overhead) + '%')

os.chdir("/home/sip/protection/sip-evaluation")

snippet = common.create_snippet('micro-snake', 'RC', protection_time, runtime_overhead, memory_overhead, size_overhead)

result_file.write(snippet)

result_file.close()
