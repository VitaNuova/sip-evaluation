FROM ubuntu:16.04

# Install some dependencies
RUN apt-get update && apt-get install -y build-essential cmake git sudo wget vim time
RUN echo "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main" >> /etc/apt/sources.list
RUN echo "deb-src http://apt.llvm.org/xenial/ llvm-toolchain-xenial-3.9 main"  >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 15CF4D18AF4F7421
RUN apt-get update && apt-get install -y clang-3.9 clang-3.9-doc libclang-common-3.9-dev libclang-3.9-dev libclang1-3.9 libclang1-3.9-dbg libllvm-3.9-ocaml-dev libllvm3.9 libllvm3.9-dbg lldb-3.9 llvm-3.9 llvm-3.9-dev llvm-3.9-doc llvm-3.9-examples llvm-3.9-runtime clang-format-3.9 python-clang-3.9 libfuzzer-3.9-dev zlibc zlib1g zlib1g-dev libboost-all-dev

# Install dyninst
RUN git clone --depth 1 --branch v9.3.2 https://github.com/dyninst/dyninst.git
WORKDIR /dyninst
RUN mkdir build
WORKDIR /dyninst/build
# Fix the problem with while
COPY files/dyninst/dyninstAPI/src/ast.C  /dyninst/dyninstAPI/src/ast.C
RUN cmake ..
RUN make && make install
# Set runtime libraries
RUN export DYNINSTAPI_RT_LIB=/usr/local/lib/libdyninstAPI_RT.so
RUN export LD_LIBRARY_PATH=/usr/local/lib/:$LD_LIBRARY_PATH

# Add a non-root user
RUN useradd --create-home --shell /bin/bash sip && adduser sip sudo
RUN echo 'sip:sip' | chpasswd
WORKDIR /home/sip

# Build KLEE
RUN apt-get -y install bc bison build-essential cmake curl flex git libboost-all-dev libcap-dev libncurses5-dev python-minimal python-pip subversion unzip zlib1g-dev
RUN git clone https://github.com/tum-i22/klee-install.git
RUN mkdir build
RUN sh ./klee-install/ubuntu.sh /home/sip/build/

# Build KLEE opt passes
RUN apt-get install -y python3
WORKDIR /home/sip/build
RUN git clone -b ktest-result --depth 1 https://github.com/tum-i22/macke-opt-llvm.git
WORKDIR /home/sip/build/macke-opt-llvm
RUN make LLVM_SRC_PATH=/home/sip/build/llvm KLEE_BUILDDIR=/home/sip/build/klee/Release+Asserts KLEE_INCLUDES=/home/sip/build/klee/include/


# Copy pass files
COPY files/home/klee /home/sip/klee
COPY files/home/ /home/sip/
COPY files/include/ /usr/local/include/
COPY files/lib/ /usr/local/lib/


############ Self-cehcksumming from Anahit & Daniel (team2)#############
RUN apt-get install -y libelf-dev

WORKDIR /home/sip/protection

#clone self-checksumming
WORKDIR /home/sip/protection
RUN git clone https://github.com/anahitH/self-checksumming.git
WORKDIR /home/sip/protection/self-checksumming
RUN mkdir build
WORKDIR /home/sip/protection/self-checksumming/build
RUN cmake ..
RUN make
RUN cp src/self-checksumming /usr/local/bin/
WORKDIR /home/sip/protection
#RUN rm -rf self-checksumming
############ End of Self-cehcksumming #############

############ Control flow integrity from Martin & Alex (team3) #############
RUN apt-get install -y gdb python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
RUN pip install --upgrade pip
RUN pip install --upgrade pwntools

# Copy files for control flow integrity program and build it
RUN apt-get install -y openssl libssl-dev
WORKDIR /home/sip/protection/cfi/build
RUN cmake ..
RUN make
############ End of control flow  #############

############ Result checking from Zhechko & Johannes (team6) #############
WORKDIR /home/sip

RUN apt-get update && apt-get install -y \
	jq \
	locales \
	python3.5-dev && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Specify locales
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install project dependencies
RUN git clone --depth 1 --branch 1.8.1 https://github.com/open-source-parsers/jsoncpp.git && \
    mkdir -p /home/sip/jsoncpp/build && \
    cmake -H/home/sip/jsoncpp -B/home/sip/jsoncpp/build && \
    make -C /home/sip/jsoncpp/build -j 2 install
WORKDIR /home/sip/protection/stins4llvm
RUN make
############ End of result checking #############

############ Oblivious hashing from Anahit & Daniel (team2)#############
# clone oblivious hashing
WORKDIR /home/sip/protection
RUN git clone https://github.com/djwessel/introspection-oblivious-hashing.git
WORKDIR introspection-oblivious-hashing
RUN mkdir build
WORKDIR /home/sip/protection/introspection-oblivious-hashing/build
RUN cmake ..
RUN make
RUN cp lib/liboblivious-hashing.so /usr/local/lib
WORKDIR /home/sip/protection
#RUN rm -rf introspection-oblivious-hashing
############ End of Oblivious hashing #############
RUN git clone https://github.com/VitaNuova/sip-evaluation.git

# Switch to user
RUN chown -R sip:sip /home/sip
USER sip
RUN export DYNINSTAPI_RT_LIB=/usr/local/lib/libdyninstAPI_RT.so

