#!/bin/bash

source_input=$1
input=$2

# compile source to bitcode
# clang-3.9 -c -emit-llvm $source_input -o OH-build/input.bc -Xclang -DVERSION=\"1.0.1\"

# compiling external libraries to bitcodes
clang++-3.9 /home/sip/protection/introspection-oblivious-hashing/assertions/asserts.cpp -std=c++0x -c -emit-llvm -o OH-build/asserts.bc
clang-3.9 /home/sip/protection/introspection-oblivious-hashing/hashes/hash.c -c -emit-llvm -o OH-build/hash.bc

# Running hash insertion pass
opt-3.9 -load /usr/local/lib/libInputDependency.so -load  OH-build/lib/liboblivious-hashing.so $source_input -oh-insert -num-hash 5 -o OH-build/out.bc
# Linking with external libraries
llvm-link-3.9 OH-build/out.bc OH-build/hash.bc -o OH-build/out.bc
llvm-link-3.9 OH-build/out.bc OH-build/asserts.bc -o OH-build/out.bc

# precompute hashes
clang++-3.9 -lncurses -rdynamic -std=c++0x OH-build/out.bc -o OH-build/out
python inputs/ptypipe.py $input OH-build/out 
###rm out
#

# Running assertion insertion pass
opt-3.9 -load /usr/local/lib/libInputDependency.so -load OH-build/lib/liboblivious-hashing.so OH-build/out.bc -insert-asserts -o OH-build/protected.bc
# Compiling to final protected binary
llc-3.9 -filetype=obj OH-build/protected.bc
g++ -lncurses -rdynamic -std=c++0x OH-build/protected.o -o OH-build/protected
#clang++-3.9 -g -lncurses -rdynamic -std=c++0x OH-build/protected.bc -o OH-build/protected

