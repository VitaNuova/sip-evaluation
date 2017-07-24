import common

result_file = open("results.json", "a")

# SC
# micro-snake
protection_time = common.measure_protection_time(["SC-build/src/self-checksumming", "input_programs/snake", "1", "snake"])
print('SC snake protection time ' + str(protection_time))

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
print('SC csnake protection time ' + str(protection_time))

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
print('SC tetris protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris_modified"])
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/tetris", "input_programs/tetris_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('tetris', 'SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

result_file.close()
                   
