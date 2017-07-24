#!/bin/bash

usage () {
	printf "Usage: $0 <source file> <sensitive function list> <input to pipe>\n"
	printf "Example: '$0 ../something.bc sensitiveList.txt input.in'\n"
	exit 1
}

if [ $# -ne 3 ]
then
	printf "Wrong number of parameters\n"
	usage
fi

opt-3.9 -load /home/sip/protection/cfi/build/code/libFunctionPass.so -i $2 -functionpass < $1 > CFI-build/something_pass.bc
opt-3.9 -O3 < CFI-build/something_pass.bc > CFI-build/something_opt.bc
clang-3.9 -g -c -emit-llvm /home/sip/protection/cfi/code/NewStackAnalysis.c -o CFI-build/NewStackAnalysis.bc 


# compiling external libraries to bitcodes
clang++-3.9 /home/sip/protection/introspection-oblivious-hashing/assertions/asserts.cpp -std=c++0x -c -emit-llvm -o OH-build/asserts.bc
clang-3.9 /home/sip/protection/introspection-oblivious-hashing/hashes/hash.c -c -emit-llvm -o OH-build/hash.bc
clang++-3.9 /home/sip/protection/introspection-oblivious-hashing/assertions/logs.cpp -std=c++0x -c -emit-llvm -o OH-build/logs.bc

# Running hash insertion pass
opt-3.9 -load /usr/local/lib/libInputDependency.so -load  OH-build/lib/liboblivious-hashing.so CFI-build/something_pass.bc -oh-insert -num-hash 5 -o OH-build/out.bc
# Linking with external libraries
llvm-link-3.9 CFI-build/NewStackAnalysis.bc OH-build/out.bc -o OH-build/out.bc
llvm-link-3.9 OH-build/out.bc OH-build/hash.bc -o OH-build/out.bc
llvm-link-3.9 OH-build/out.bc OH-build/asserts.bc -o OH-build/out.bc
llvm-link-3.9 OH-build/out.bc OH-build/logs.bc -o OH-build/out.bc


# precompute hashes
clang++-3.9 -g -lncurses -rdynamic -std=c++0x OH-build/out.bc -o OH-build/out -lssl -lcrypto
python /home/sip/dataset/inputs/ptypipe.py $3 OH-build/out

# Running assertion insertion pass
opt-3.9 -load /usr/local/lib/libInputDependency.so -load OH-build/lib/liboblivious-hashing.so OH-build/out.bc -insert-asserts -o OH-build/protected.bc
# Compiling to final protected binary
clang++-3.9 -g -lncurses -rdynamic -std=c++0x OH-build/protected.bc -o OH-build/protected -lssl -lcrypto


