import common

result_file = open("results.json", "a")

# OH + SC
# micro-snake
oh_protection_time = common.measure_protection_time(["./run-oh-eval.sh", "inputs/snake.bc", "inputs/micro-snake.in"])
sc_protection_time = common.measure_protection_time(["SC-build/src/self-checksumming", "OH-build/protected", "1", "protected"])
protection_time = oh_protection_time + sc_protection_time
print('OH + SC snake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected_modified"])
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/snake", "OH-build/protected_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "OH-build/protected_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('micro-snake', 'OH+SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

'''
# c-snake
oh_protection_time = common.measure_protection_time(["./run-oh-eval.sh", "inputs/csnake.bc", "inputs/c-snake.in"])
sc_protection_time = common.measure_protection_time(["SC-build/src/self-checksumming", "OH-build/protected", "1", "protected"])
protection_time = oh_protection_time + sc_protection_time
print('OH + SC csnake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "OH-build/protected_modified"])
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/csnake", "OH-build/protected_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "OH-build/protected_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('c-snake', 'OH+SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)
'''
# tetris
oh_protection_time = common.measure_protection_time(["./run-oh-eval.sh", "inputs/tetris.bc", "inputs/tetris.in"])
sc_protection_time = common.measure_protection_time(["SC-build/src/self-checksumming", "OH-build/protected", "1", "protected"])
protection_time = oh_protection_time + sc_protection_time
print('OH + SC tetris protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "OH-build/protected_modified"])
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/tetris", "OH-build/protected_modified")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "OH-build/protected_modified"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('tetris', 'OH+SC', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

result_file.close()
