<h1 align="center">📸 Automatic Screenshot Capture & Email Sender</h1>

<p align="center">
A Python-based automation tool that captures screenshots at specific intervals and sends them via email in real-time.
</p>

<hr>

<h2>👨‍💻 Authors</h2>

<ul>
<li><strong>Rahat Sahriar Rafi</strong> – Main Author, Project Lead, System Design & Core Development</li>
<li><strong>Md. Munkasir Haque</strong> – Co-Author, Automation, Email Integration & Deployment</li>
</ul>

<hr>

<h2>🚀 Features</h2>

<ul>
<li>📸 Automatic screenshot capture</li>
<li>⏱️ Custom time interval support</li>
<li>📧 Email sending with attachment</li>
<li>🖥️ Real-time execution</li>
<li>📂 Local screenshot storage</li>
<li>🔐 Secure credential input (no hardcoded secrets)</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
Automatic-Screenshot-Capture-and-Email-Sender/
│
├── main.py
├── screenshot.py
├── mailer.py
├── config.py
│
├── screenshots/
└── README.md
</pre>

<hr>

<h2>⚙️ Installation</h2>

<pre>
# Install system dependencies
sudo apt install python3-venv scrot gnome-screenshot

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate

# Install Python packages
pip install pyautogui pillow
</pre>

<hr>

<h2>▶️ Usage</h2>

<pre>
python main.py
</pre>

<ul>
<li>Enable email sending (optional)</li>
<li>Enter sender email and app password</li>
<li>Tool will start capturing and sending screenshots automatically</li>
</ul>

<hr>

<h2>⚠️ Important Notes</h2>

<ul>
<li>Use Gmail App Password (not your real password)</li>
<li>Works only in GUI environment (not SSH/headless)</li>
<li>X11 session recommended (Wayland may cause screenshot issues)</li>
</ul>

<hr>

<h2>🔮 Future Improvements</h2>

<ul>
<li>📦 Batch screenshot sending (ZIP)</li>
<li>📡 Telegram integration</li>
<li>🕵️ Background/stealth execution</li>
<li>🧠 Smart capture (on screen changes only)</li>
</ul>

<hr>

<h2>📜 License</h2>

<p>This project is for educational purposes only.</p>

<hr>

<p align="center">🔥 Built with Python by Rahat & Munkasir</p>
