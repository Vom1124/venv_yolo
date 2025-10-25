
# <b>venv_yolo</b>
<i>Ultralytics YOLO Virtual Environment to run in parallel with ROS 2</i>

<p>
This README provides a complete guide to creating a dedicated Python virtual environment (<code>venv_yolo</code>) for training and using <b>Ultralytics YOLO</b> alongside your ROS 2 workspace. 
</p>

<p>
<b>Important:</b> There are two installation options depending on your system:
<ul>
<li><b>Host Computer / Microcontroller:</b> Recommended for Linux, Windows, or ARM devices (e.g., Raspberry Pi 4+).</li>
<li><b>Virtual Machine without AVX instructions:</b> Recommended for VMs such as VirtualBox or CPUs without AVX support. PyTorch must be built from source.</li>
</ul>
Choose only one path below after completing the common prerequisites.
</p>

---

<h2>Common Prerequisites</h2>

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
# Linux/macOS
source ~/venv_yolo/bin/activate
</code></pre>

<pre><code class="cmd">
REM Windows CMD
venv_yolo\Scripts\activate
</code></pre>

<pre><code class="powershell">
# Windows PowerShell
.\venv_yolo\Scripts\Activate.ps1
</code></pre>

<h3>4. Upgrade pip</h3>
<pre><code class="bash">
pip install --upgrade pip
</code></pre>


<h2>Installation Options</h2>
---
<h3>A. Host Computer / Microcontroller</h3>
<p>Use this if you are on Linux, Windows, or an ARM device like Raspberry Pi 4+. Follow these steps:</p>

<pre><code class="bash">
# Install PyTorch CPU-only
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
</code></pre>

<h3>B. Virtual Machine without AVX</h3>
<p>Use this if you are on a VM (e.g., VirtualBox) or CPU without AVX support. Note: Training may be slower.</p>
<p><u>Warning:</u> This installation might much longer than installing direclty with .whl file. Also, make sure to uninstall
  or remove pre-exisitng pytorch within the venv</p>
<pre><code class="bash">
pip uninstall torch torchvision && pip cache purge
</code></pre>

<pre><code class="bash">
# Install build dependencies
sudo apt update
sudo apt install -y git python3-dev python3-pip cmake ninja-build libopenblas-dev

# Clone PyTorch repository (v2.2.2)
git clone --branch v2.2.2 https://github.com/pytorch/pytorch.git
cd pytorch

# Initialize submodules
git submodule sync
git submodule update --init --recursive

# Install Python build dependencies
pip install -r requirements.txt

# Build PyTorch without AVX
USE_CUDA=0 USE_MKLDNN=0 USE_FBGEMM=0 USE_AVX=0 USE_AVX2=0 USE_AVX512=0 \
USE_VSX=0 USE_MPS=0 BUILD_TEST=0 python setup.py install

</code></pre>

##### Verify the pytorch version and check for CPU status for AVX free
<pre><code class="bash">
python -c "import torch; print(torch.__version__); print(torch.__config__.show())"
OR
grep -a AVX $(python -c "import torch; print(torch.__file__)") || echo "No AVX detected"

</code></pre>


  
<h2> Install Ultralytics YOLO without any dependencies to avoid ultralytics to automatically install the recent pytorch</h2>
<pre><code class="bash">
pip install ultralytics --no-deps
</code></pre>

<h3>Now, add necessary packages as needed. For example, OpenCV, Matplotlib, etc.</h3>
<pre><code class="bash">
pip install opencv-python tqdm matplotlib

</code></pre>
  
<h3> Ensure NumPy is < 2 to avoid conflicts  </h3>
<pre><code class="bash">
pip install "numpy<2"
</code></pre>


<h2>Verify Installation</h2>
---
<pre><code class="bash">
#Test YOLO
python3 -c 'import ultralytics; from ultralytics import YOLO; print("✅ YOLO ready")'
  
#Test NumPy  
python3 -c "import numpy; print('🔢 NumPy version:', numpy.__version__)"
</code></pre>

<p>Optional <code>check_yolo.py</code>:</p>
<pre><code class="bash">
python3 check_yolo.py
</code></pre>


<h2>Example using YOLO with ROS 2</h2>
---
<p>Always activate <code>venv_yolo</code> in a separate terminal. Do NOT source ROS 2 globally in the same terminal.</p>

<pre><code class="bash">
# Terminal 1 – ROS 2 workspace
source /opt/ros/humble/setup.bash
colcon build

# Terminal 2 – YOLO environment
source ~/venv_yolo/bin/activate
python3 train_yolo_model.py
</code></pre>


<!---
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
--->!
---

<h2>Summary</h2>

<table>
<tr><th>Environment</th><th>PyTorch Install</th><th>AVX Support</th><th>Recommended For</th></tr>
<tr><td>Host / Microcontroller</td><td>pip install torch torchvision torchaudio + ultralytics</td><td>✅ Yes</td><td>Linux, Windows, Raspberry Pi</td></tr>
<tr><td>Virtual Machine</td><td>Build from source + ultralytics</td><td>❌ No</td><td>VirtualBox or CPUs without AVX</td></tr>
</table>

<p>End of venv_yolo setup.</p>
