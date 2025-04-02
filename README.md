## Android Mobile Automation for CaptionCall App using Appium
### Installation
1. Install brew

   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" `

2. Install python3 via brew

   `brew install python3 `

3. Install node via brew

   `brew install node`

4. Install Appium

   `npm i --location=global appium`

5. Install Appium UIAutomator2 driver

   `appium driver install uiautomator2`

6. Install JDK

   `brew install openjdk`

7. Add JDK to path (export JAVA_HOME=/usr/local/opt/openjdk@<version>/libexec/openjdk.jdk for MacOS)
8. Install Android SDK via Android Studio
9. Open the repository via VS Code
10. Install virtualenv using python3

   `pip3 install virtualenv`

11. Create virtual environment in the repository

   `python3 -m venv .venv`

12. Activate virtual environment

   `source .venv/bin/activate`

13. Install packages

   `pip install -r requirements.txt`

### Running Tests
1. In VS Code, press view > testing
2. Verify that there the tests are populated
3. Plug in your device
4. Verify that your device is visible using `adb devices`
5. Press the play button to run all tests
 
