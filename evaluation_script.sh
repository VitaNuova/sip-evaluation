#!/bin/bash

# build SC
# rm -rf SC-build
# mkdir SC-build
# cd SC-build
# cmake /home/sip/protection/self-checksumming
# make 
# cd ..

rm -rf OH-build
mkdir OH-build
cd OH-build
cmake /home/sip/protection/introspection-oblivious-hashing
make 
cd ..

# rm -rf CFI-build
# mkdir CFI-build
# cd CFI-build
# cmake /home/sip/protection/cf-integrity
# make
# cd ..



# protection time for SC
#python SC_standalone.py


