#!/bin/bash

cc -c /home/sip/protection/cf-integrity/whitelist/snippet.c -o CFI-build/snippet.o
clang-3.9 -g -emit-llvm  /home/sip/dataset/src/tetris/tetris.c -c -o CFI-build/tetris.bc
opt-3.9 -load CFI-build/whitelist/libWhiteListPass.so -whitelist -sf fits_in  -sf place -sf freeze -sf update -sf show_high_score < CFI-build/tetris.bc > CFI-build/tetris_result.bc
llc-3.9 -filetype=obj CFI-build/tetris_result.bc
cc -g -rdynamic CFI-build/tetris_result.o CFI-build/snippet.o -L/usr/lib/gcc/x86_64-linux-gnu/5 -lbacktrace -o CFI-build/tetris_protected
