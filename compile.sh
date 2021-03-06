#!/bin/bash

usage () {
	printf "Usage: $0 <llvm bitcode file> <desired path to new binary> <sensitive function list>\n"
	printf "Example: '$0 ../something.bc ./something sensitiveList.txt'\n"
	exit 1
}

if [ $# -ne 3 ]
then
	printf "Wrong number of parameters\n"
	usage
fi

opt-3.9 -load /home/sip/protection/cfi/build/code/libFunctionPass.so -i $3 -functionpass < $1 > something_pass.bc
opt-3.9 -O3 < something_pass.bc > something_opt.bc
clang-3.9 -g -c -emit-llvm /home/sip/protection/cfi/code/NewStackAnalysis.c -o NewStackAnalysis.bc -lssl -lcrypto
llvm-link-3.9 NewStackAnalysis.bc something_opt.bc -o something_tmp.bc
clang-3.9 -g something_tmp.bc -lm -lncurses -o $2 -lssl -lcrypto
