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

### --- Install PyTorch CPU-only for ARM (this is for Raspberry 4+ models only, check the code for CUDA and other GPUs before installing)

      pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

### ---- Install Ultralytics with all dependencies

      pip install ultralytics


### ---- Verify installation

      python3 -c 'import ultralytics; from ultralytics import YOLO; print("✅ YOLO ready")'
      python3 -c "import numpy; print('🔢 NumPy version:', numpy.__version__)"
      
Alternatively, you can run

        python3 check_yolo.py

### ---- Installing  OpenNI for getting stream from depth sensor 

# 1. Install dependencies
        sudo apt update
        sudo apt install git build-essential python3-pip \
            libusb-1.0-0-dev libudev-dev openjdk-8-jdk freeglut3-dev \
            doxygen graphviz

# 2. Clone the OpenNI2 repository
        git clone https://github.com/structureio/OpenNI2.git
        cd OpenNI2

# 3. Checkout the master branch
        git checkout master

# 4. Build OpenNI2
        make
