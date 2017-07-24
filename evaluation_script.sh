#!/bin/bash

rm -rf SC-build
mkdir SC-build
cd SC-build
cmake /home/sip/protection/self-checksumming
make 
cd ..

rm -rf OH-build
mkdir OH-build
cd OH-build
cmake /home/sip/protection/introspection-oblivious-hashing
make 
cd ..

rm -rf CFI-build
mkdir CFI-build
cd CFI-build
cmake /home/sip/protection/cfi
make
cd ..

cp config_zopfli.json /home/sip/protection/stins4llvm
cp run-oh.sh /home/sip/protection/introspection-oblivious-hashing

python SC.py
python OH.py
python CFI.py
python OH-SC.py
python CFI-OH-RC.py



