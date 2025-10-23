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

#### *** NumPy should be kept below version 2.0; otherwise, ROS 2 or Ultralytics may encounter conflicts with globally installed dependencies. ***

### --- Install PyTorch CPU-only for ARM (this is for Raspberry 4+ models only, check the code for CUDA and other GPUs before installing)

      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

### ---- Install Ultralytics with all dependencies

      pip install ultralytics


### ---- Verify installation

      python3 -c 'import ultralytics; from ultralytics import YOLO; print("✅ YOLO ready")'
      python3 -c "import numpy; print('🔢 NumPy version:', numpy.__version__)"
      
Alternatively, you can run

        python3 check_yolo.py

Now, everytime a YOLO library is used within ROS2 node, that terminal needs to be separately sources and can not be sources globally with ROS 2 workpace, as ROS 2 and Ultralytics don't share the same version of many odules like OpenCV, Python, etc.

### Training a YOLO model within the VM Ubuntu without AVX

<b> Note:</b> Without AVX might be a slower training process; make sure enough resources is allocated for the VM. Porceed with caution!

#### If you have already installed YOLO similar to the process discussed earlier in this .readme file, you first need to uninstall the pytorch and other dependancies that might depend on GPU and AVX instructions within the virtual environment that was already created.

##### Make a folder for your YOLO projects
        mkdir -p ~/ros2_ws/venv_yolo
        cd ~/ros2_ws/venv_yolo
        
##### Create Python 3.10 virtual environment
        python3.10 -m venv venv_yolo
        
##### Activate the venv
        source venv_yolo/bin/activate


##### Upgrade pip
        pip install --upgrade pip

##### Uninstall any conflicting versions first
        pip uninstall torch torchvision torchaudio -y

##### Install CPU-only PyTorch 1.12 + torchvision 0.13 + torchaudio 0.12
        pip install torch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 --index-url https://download.pytorch.org/whl/cpu

##### CPU-only PyTorch 1.12 + torchvision 0.13
        pip install torch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 --index-url https://download.pytorch.org/whl/cpu

##### Now, finally, install ultralytics
        pip install ultralytics 

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
