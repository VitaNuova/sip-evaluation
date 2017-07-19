#!/bin/bash

# build SC
rm -rf SC-build
mkdir SC-build
cd SC-build
cmake /home/sip/protection/self-checksumming
make 

# protection time for SC
#python SC_standalone.py


