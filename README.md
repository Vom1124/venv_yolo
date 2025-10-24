# venv_yolo
Ultralytics_YOLO Virtual Environment to run in parallel with ROS~2

##  Preliminary Setup

### -- Install Python Virtual Environment (using the correct python 3 version installed in your system)

        sudo apt update && sudo apt install python3.10-venv
        
### ---- Create a virtual environment parent directory to install the Ultralytics (preferrably outisde the ros2_ws to avoid any package conflcits)

    python3 -m venv ~/venv_yolo

### --- Now, source the venv using

    source ~/venv_yolo/bin/activate

### --- Update the pip

      pip install --upgrade pip

#### *** NumPy should be kept below version 2.0; otherwise, ROS 2 or Ultralytics may encounter conflicts with globally installed dependencies. 
This can simply be done by reinstalling older version of numpy as

                pip install "numpy<2"
***

### ons are define: [1] Host computer; and [2] Virtual Machine Ubuntu

## [1] Installing in the host computer/microcontroller
[.] ### --- Install PyTorch CPU-only for ARM (this is for Raspberry 4+ models only, check the code for CUDA and other GPUs before installing)

      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

[.] ### ---- Install Ultralytics with all dependencies

      pip install ultralytics

## [2] Installing on a VM without AVX instructions
[.] ### Installing PyTorch from source instead of .whl file.
<b> Note:</b> Without AVX might be a slower training process; make sure enough resources is allocated for the VM. Porceed with caution!

        sudo apt update
        sudo apt install -y git python3-dev python3-pip cmake ninja-build libopenblas-dev
        
        git clone --branch v2.2.2 https://github.com/pytorch/pytorch.git
        cd pytorch
        git submodule sync
        git submodule update --init --recursive
        
        pip install -r requirements.txt
        
        USE_CUDA=0 USE_MKLDNN=0 USE_FBGEMM=0 USE_AVX=0 USE_AVX2=0 USE_AVX512=0 \
        USE_VSX=0 USE_MPS=0 BUILD_TEST=0 python setup.py install


### ---- Verify installation

      python3 -c 'import ultralytics; from ultralytics import YOLO; print("✅ YOLO ready")'
      python3 -c "import numpy; print('🔢 NumPy version:', numpy.__version__)"
      
Alternatively, you can run

        python3 check_yolo.py

Now, everytime a YOLO library is used within ROS2 node, that terminal needs to be separately sources and can not be sources globally with ROS 2 workpace, as ROS 2 and Ultralytics don't share the same version of many odules like OpenCV, Python, etc.

### Training a YOLO model within the VM Ubuntu without AVX




<!---
### ---- Installing  OpenNI for getting stream from depth sensor 

#### 1. Install dependencies
        sudo apt update && \
        sudo apt install git build-essential python3-pip \
            libusb-1.0-0-dev libudev-dev openjdk-8-jdk freeglut3-dev \
            doxygen graphviz

#### 2. Clone the OpenNI2 repository
        git clone https://github.com/structureio/OpenNI2.git
        cd OpenNI2

#### 3. Checkout the master branch
        git checkout master

#### 4. Build OpenNI2
        make
-->
