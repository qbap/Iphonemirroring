import os
import subprocess
import shutil
from pathlib import Path

system_file = "/private/var/db/os_eligibility/eligibility.plist"
replacement_file = Path(__file__).parent / "eligibility.plist"

def replace_files():
    try:
        backup_file = f"{system_file}.backup"
        if not os.path.exists(backup_file):
            shutil.copy(system_file, backup_file)
            print(f"Backup created at: {backup_file}")

        print("Root permission required to replace system file.")
        subprocess.run(['sudo', 'cp', str(replacement_file), system_file], check=True)
        print("File replaced successfully.")

    except Exception as e:
        print(f"Error: {e}")

def launch_mirroring_app():
    try:
        # Run with sudo
        print("Starting iPhone Mirroring app...")
        subprocess.run(['open', '/System/Applications/iPhone Mirroring.app'], check=True)
        print("App launched successfully.")
	
    except Exception as e:
        print(f"Error starting app. Consider updating to macOS Sequoia. The error: {e}")

if __name__ == "__main__":
    # Replace system file
    replace_files()

    # Launch mirroring app
    launch_mirroring_app()
