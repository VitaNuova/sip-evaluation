import common

result_file = open("results.json", "a")

#CFI
# micro-snake
protection_time = common.measure_protection_time(["./compile.sh", "inputs/snake.bc", "CFI-build/snake", "snake_sens_list.txt"])
print('CFI snake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "CFI-build/snake"])
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/snake", "CFI-build/snake")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "CFI-build/snake"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('micro-snake', 'CFI', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

# csnake
protection_time = common.measure_protection_time(["./compile.sh", "inputs/csnake.bc", "CFI-build/csnake", "c_snake_sens_list.txt"])
print('CFI csnake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "CFI-build/csnake"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/csnake", "CFI-build/csnake")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "CFI-build/csnake"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('csnake', 'CFI', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

# tetris
protection_time = common.measure_protection_time(["./compile.sh", "inputs/tetris.bc", "CFI-build/tetris","tetris_sens_list.txt"])
print('CFI tetris protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "CFI-build/tetris"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/tetris", "CFI-build/tetris")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "CFI-build/tetris"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('tetris', 'CFI', protection_time, runtime_overhead, 0, size_overhead)
result_file.write(snippet)

result_file.close()
