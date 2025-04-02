Installation
Install brew

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 

Install python3 via brew

brew install python3 

Install node via brew

brew install node

Install Appium

npm i --location=global appium

Install Appium UIAutomator2 driver

appium driver install uiautomator2

Install JDK

brew install openjdk

Add JDK to path (export JAVA_HOME=/usr/local/opt/openjdk@/libexec/openjdk.jdk for MacOS)

Install Android SDK via Android Studio

Open the repository via VS Code

Install virtualenv using python3

pip3 install virtualenv

Create virtual environment in the repository
python3 -m venv .venv

Activate virtual environment
source .venv/bin/activate

Install packages
pip install -r requirements.txt

Running Tests
In VS Code, press view > testing
Verify that there the tests are populated
Plug in your device
Verify that your device is visible using adb devices
Press the play button to run all tests
