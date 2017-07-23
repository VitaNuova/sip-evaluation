#!/bin/bash

INPUT_DEP_PATH=/usr/local/lib/
OH_PATH=/home/sip/protection/introspection-oblivious-hashing
OH_LIB=$OH_PATH/build/lib
bitcode=$1
input=$2

# compiling external libraries to bitcodes
clang++-3.9 $OH_PATH/assertions/asserts.cpp -std=c++0x -c -emit-llvm -o $OH_PATH/assertions/asserts.bc
clang-3.9 $OH_PATH/hashes/hash.c -c -emit-llvm -o $OH_PATH/hashes/hash.bc

# Running hash insertion pass
opt-3.9 -load $INPUT_DEP_PATH/libInputDependency.so -load  $OH_LIB/liboblivious-hashing.so $1 -oh-insert -num-hash 1 -o OH-build/out.bc
# Linking with external libraries
llvm-link-3.9 OH-build/out.bc $OH_PATH/hashes/hash.bc -o OH-build/out.bc
llvm-link-3.9 OH-build/out.bc $OH_PATH/assertions/asserts.bc -o OH-build/out.bc

# precompute hashes
clang++-3.9 -lncurses -rdynamic -std=c++0x OH-build/out.bc -o OH-build/out
OH-build/out $input
###rm out
#

# Running assertion insertion pass
opt-3.9 -load $INPUT_DEP_PATH/libInputDependency.so -load $OH_LIB/liboblivious-hashing.so OH-build/out.bc -insert-asserts -o OH-build/protected.bc
# Compiling to final protected binary
clang++-3.9 -lncurses -rdynamic -std=c++0x OH-build/protected.bc -o OH-build/protected

