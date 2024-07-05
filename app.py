import subprocess
import winreg

def get_chrome_version():
    try:
        # Access the registry to find the version of Google Chrome
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon")
        version, regtype = winreg.QueryValueEx(key, "version")
        return version
    except FileNotFoundError:
        return "Chrome is not installed."

if __name__ == "__main__":
    chrome_version = get_chrome_version()
    print(f"Chrome version: {chrome_version}")
