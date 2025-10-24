# <b>venv_yolo</b>
<i>Ultralytics YOLO Virtual Environment to run in parallel with ROS 2</i>

<p>This README provides a complete guide to creating a dedicated Python virtual environment (<code>venv_yolo</code>) for training and using <b>Ultralytics YOLO</b> alongside your ROS 2 workspace. Covers host computers/microcontrollers and virtual machines without AVX.</p>

---

<h2>Preliminary Setup</h2>

<h3>1. Install Python Virtual Environment</h3>
<pre><code class="bash">
sudo apt update && sudo apt install python3.10-venv
</code></pre>

<h3>2. Create Virtual Environment</h3>
<pre><code class="bash">
python3 -m venv ~/venv_yolo
</code></pre>

<h3>3. Activate the Virtual Environment</h3>
<pre><code class="bash">
source ~/venv_yolo/bin/activate
# Windows:
# Command Prompt: venv_yolo\Scripts\activate
# PowerShell: .\venv_yolo\Scripts\Activate.ps1
# May require: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
</code></pre>

<h3>4. Upgrade pip and Install Compatible NumPy</h3>
<pre><code class="bash">
pip install --upgrade pip
pip install "numpy<2"
</code></pre>

---

<h2>Host Computer / Microcontroller Installation</h2>

<h3>1. Install PyTorch CPU-only</h3>
<pre><code class="bash">
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
</code></pre>

<h3>2. Install Ultralytics YOLO</h3>
<pre><code class="bash">
pip install ultralytics
</code></pre>

---

<h2>Virtual Machine Installation Without AVX</h2>
<p><b>Note:</b> AVX instructions may be missing. Build PyTorch from source to avoid illegal instruction crashes. Training may be slower.</p>

<h3>1. Install Build Dependencies</h3>
<pre><code class="bash">
sudo apt update
sudo apt install -y git python3-dev python3-pip cmake ninja-build libopenblas-dev
</code></pre>

<h3>2. Clone PyTorch Repository</h3>
<pre><code class="bash">
git clone --branch v2.2.2 https://github.com/pytorch/pytorch.git
cd pytorch
git submodule sync
git submodule update --init --recursive
pip install -r requirements.txt
</code></pre>

<h3>3. Build PyTorch Without AVX</h3>
<pre><code class="bash">
USE_CUDA=0 USE_MKLDNN=0 USE_FBGEMM=0 USE_AVX=0 USE_AVX2=0 USE_AVX512=0 \
USE_VSX=0 USE_MPS=0 BUILD_TEST=0 python setup.py install
</code></pre>

---

<h2>Verify Installation</h2>

<pre><code class="bash">
python3 -c 'import ultralytics; from ultralytics import YOLO; print("✅ YOLO ready")'
python3 -c "import numpy; print('🔢 NumPy version:', numpy.__version__)"
</code></pre>

<p>Optional: create <code>check_yolo.py</code>:</p>
<pre><code class="python">
from ultralytics import YOLO
import numpy as np

print("✅ YOLO ready")
print("🔢 NumPy version:", np.__version__)
</code></pre>

<pre><code class="bash">
python3 check_yolo.py
</code></pre>

---

<h2>Using YOLO with ROS 2</h2>
<p>Always activate <code>venv_yolo</code> in a separate terminal. Do not source ROS 2 globally in the same terminal.</p>

<pre><code class="bash">
# Terminal 1 – ROS 2 workspace
source /opt/ros/humble/setup.bash
colcon build

# Terminal 2 – YOLO environment
source ~/venv_yolo/bin/activate
python3 train_yolo_model.py
</code></pre>

---

<h2>Optional: Installing OpenNI for Depth Sensor Streaming</h2>
<pre><code class="bash">
sudo apt update && \
sudo apt install git build-essential python3-pip \
libusb-1.0-0-dev libudev-dev openjdk-8-jdk freeglut3-dev \
doxygen graphviz

git clone https://github.com/structureio/OpenNI2.git
cd OpenNI2
git checkout master
make
</code></pre>

---

<h2>Summary</h2>

<table>
<tr><th>Environment</th><th>PyTorch Install</th><th>AVX Support</th><th>Recommended For</th></tr>
<tr><td>Host / Microcontroller</td><td>pip install torch torchvision torchaudio</td><td>✅ Yes</td><td>Linux, Windows, Raspberry Pi</td></tr>
<tr><td>Virtual Machine</td><td>Build from source</td><td>❌ No</td><td>VirtualBox or CPUs without AVX</td></tr>
</table>

<p>End of venv_yolo setup.</p>
