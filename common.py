import time
import subprocess
import os

# protection overhead
def measure_protection_time(args):
   start = time.time()
   FNULL = open(os.devnull, 'w')
   p = subprocess.Popen(args, stdout = FNULL, stderr = FNULL)
   out, err = p.communicate()
   end = time.time()
   return end - start

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

def create_snippet(program, composition, protection_time, runtime_overhead, memory_overhead, size_overhead):
   return '{\n"program": "' + program + '",\n"Results": [\n\t\t{\n\t\t"Composition": "' + composition + '",\n\t\t"ProtectionTime": ' + str(protection_time) + ',\n\t\t"RuntimeOverhead": ' + str(runtime_overhead) + ',\n\t\t"MemoryOverhead": ' + str(memory_overhead) + ',\n\t\t"BinarySizeOverhead": ' + str(size_overhead) + '\n\t\t}\n\t]\n}\n'


