#!/bin/bash

cc -c /home/sip/protection/cf-integrity/whitelist/snippet.c -o CFI-build/snippet.o
clang-3.9 -g -emit-llvm  /home/sip/dataset/src/c-snake/snake.c -c -o CFI-build/csnake.bc
opt-3.9 -load CFI-build/whitelist/libWhiteListPass.so -whitelist -sf snake_game_over -sf snake_in_bounds -sf snake_draw_fruit -sf snake_index_to_coordinate -sf snake_cooridinate_to_index -sf snake_move_player -sf main < CFI-build/csnake.bc > CFI-build/csnake_result.bc
llc-3.9 -filetype=obj CFI-build/csnake_result.bc
cc -g -rdynamic CFI-build/csnake_result.o CFI-build/snippet.o -L/usr/lib/gcc/x86_64-linux-gnu/5 -lbacktrace -lncurses -o CFI-build/csnake_protected
