import common

result_file = open("results.json", "a")

# OH
# micro-snake
protection_time = common.measure_protection_time(["../introspection-oblivious-hashing/run-oh.sh", "inputs/snake.bc", "inputs/micro-snake.in"])
print('OH snake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "./out"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/snake", "./out")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "input_programs/snake"], ["python", "inputs/ptypipe.py", "inputs/micro-snake.in", "./out"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('micro-snake', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)


# c-snake
protection_time = common.measure_protection_time(["../introspection-oblivious-hashing/run-oh.sh", "inputs/csnake.bc", "inputs/c-snake.in"])
print('OH csnake protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "./out"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/csnake", "./out")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/c-snake.in", "input_programs/csnake"], ["python", "inputs/ptypipe.py", "inputs/c-snake.in", "./out"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('c-snake', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

'''
# tetris
protection_time = common.measure_protection_time(["../introspection-oblivious-hashing/run-oh.sh", "inputs/tetris.bc", "inputs/tetris.in"])
print('OH tetris protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "./out"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/tetris", "./out")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["python", "inputs/ptypipe.py", "inputs/tetris.in", "input_programs/tetris"], ["python", "inputs/ptypipe.py", "inputs/tetris.in", "./out"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('tetris', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)
'''
# zopfli
protection_time = common.measure_protection_time(["./run-oh-zopfli.sh", "./zopfli_whole.bc", "inputs/zopfli.in"])
print('OH zopfli protection time ' + str(protection_time))

runtime_overhead = common.measure_runtime_overhead(["input_programs/zopfli", "inputs/zopfli.in"], ["OH-build/protected", "inputs/zopfli.in"]) 
print('runtime overhead ' + str(runtime_overhead) + '%')

size_overhead = common.measure_binary_overhead("input_programs/zopfli", "OH-build/protected")
print('size overhead ' + str(size_overhead) + '%')

memory_overhead = common.measure_memory_overhead(["input_programs/zopfli", "inputs/zopfli.in"], ["OH-build/protected", "inputs/zopfli.in"])
print('memory overhead ' + str(memory_overhead) + '%')

snippet = common.create_snippet('zopfli', 'OH', protection_time, runtime_overhead, memory_overhead, size_overhead)
result_file.write(snippet)

result_file.close()
