def check_drivers_powershell():
    import os
    import subprocess

    # Dictionary of web browser drivers and their download URLs
    drivers = {
        "Chrome": "https://chromedriver.storage.googleapis.com/latest/chromedriver_win32.zip",
        "Firefox": "https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-win64.zip",
        "Edge": "https://msedgedriver.azureedge.net/LATEST_RELEASE_EDGE",
    }

    # Check if each driver is installed
    for browser, url in drivers.items():
        # Check if the driver executable exists
        if not os.path.exists(f"C:\\Program Files\\{browser}\\driver.exe"):
            # Driver not found, download it
            print(f"{browser} driver not found, downloading...")

            # Use powershell to download the driver
            subprocess.run(["powershell", "-Command",
                            f"Invoke-WebRequest -Uri {url} -OutFile 'C:\\Program Files\\{browser}\\driver.zip'"])

            # Extract the downloaded zip file
            subprocess.run(["powershell", "-Command",
                            f"Add-Type -Assembly 'System.IO.Compression.FileSystem'; "
                            f"[IO.Compression.ZipFile]::ExtractToDirectory('C:\\Program Files\\{browser}\\driver.zip', "
                            f"'C:\\Program Files\\{browser}')"])

            # Delete the zip file
            subprocess.run(["powershell", "-Command",
                            f"Remove-Item 'C:\\Program Files\\{browser}\\driver.zip'"])

    print("All web browser drivers are installed.")


# Check if each driver is installed using sh
def check_drivers_shell():
    # Dictionary of web browser drivers and their download URLs
    drivers = {
        "Chrome": "https://chromedriver.storage.googleapis.com/latest/chromedriver_linux64.zip",
        "Edge": "https://msedgedriver.azureedge.net/LATEST_RELEASE_EDGE",
        "Safari": "https://webkit.org/blog/6900/webdriver-support-in-safari-10/",
        "Firefox": "https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz"
    }
    current_os = platform.system()
    for browser, url in drivers.items():
        # Skip Safari on non-macOS systems
        if browser == "Safari" and current_os != "Darwin":
            continue

        # Check if the driver executable exists
        if not os.path.exists(f"/usr/local/bin/{browser.lower()}driver"):
            # Driver not found, download it
            print(f"{browser} driver not found, downloading...")

            # Use wget to download the driver on Linux systems
            if current_os == "Linux":
                subprocess.run(["wget", "-O", f"/usr/local/bin/{browser.lower()}driver.zip", url])

                # Extract the downloaded zip file
                subprocess.run(["unzip", f"/usr/local/bin/{browser.lower()}driver.zip", "-d", "/usr/local/bin/"])

            # Use curl to download the driver on macOS systems
            elif current_os == "Darwin":
                subprocess.run(["curl", "-L", url, "-o", f"/usr/local/bin/{browser.lower()}driver.zip"])

                # Extract the downloaded zip file
                subprocess.run(["unzip", f"/usr/local/bin/{browser.lower()}driver.zip", "-d", "/usr/local/bin/"])

            # Set the executable bit on the driver executable
            subprocess.run(["chmod", "+x", f"/usr/local/bin/{browser.lower()}driver"])

    print("All web browser drivers are installed.")