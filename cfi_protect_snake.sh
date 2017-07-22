#!/bin/bash

cc -c /home/sip/protection/cf-integrity/whitelist/snippet.c -o CFI-build/snippet.o
clang-3.9 -g -emit-llvm /home/sip/dataset/src/micro-snake/snake.c -c -o CFI-build/snake.bc -Xclang -DVERSION=\"1.0.1\"
opt-3.9 -load CFI-build/whitelist/libWhiteListPass.so -whitelist -sf collision -sf eat_gold -sf setup_level -sf move -sf collide_self -sf collide_object -sf show_score -sf collide_walls -sf main < CFI-build/snake.bc > CFI-build/snake_result.bc
llc-3.9 -filetype=obj CFI-build/snake_result.bc
cc -g -rdynamic CFI-build/snake_result.o CFI-build/snippet.o -L/usr/lib/gcc/x86_64-linux-gnu/5 -lbacktrace -o CFI-build/snake_protected
