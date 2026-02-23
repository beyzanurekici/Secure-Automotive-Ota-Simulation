import requests
import shutil
from verify_update import verify_signature

SERVER_URL = "http://127.0.0.1:8000"

VERSION_FILE = "firmware_storage/current_version.txt"
ACTIVE_FW = "firmware_storage/active_firmware.bin"
DOWNLOADED_FW = "firmware_storage/downloaded_firmware.bin"

PUBLIC_KEY = "server/public_key.pem"
SIGNATURE = "server/firmware_v2.sig"


class OTAUpdateManager:

    def get_current_version(self):
        with open(VERSION_FILE, "r") as f:
            return f.read().strip()

    def check_latest_version(self):
        response = requests.get(f"{SERVER_URL}/version")
        return response.json()["version"]

    def is_downgrade(self, current, new):
        current_tuple = tuple(map(int, current.split(".")))
        new_tuple = tuple(map(int, new.split(".")))
        return new_tuple < current_tuple

    def download_firmware(self):
        print("Downloading firmware...")
        response = requests.get(f"{SERVER_URL}/firmware")

        with open(DOWNLOADED_FW, "wb") as f:
            f.write(response.content)

    def verify_firmware(self):
        return verify_signature(PUBLIC_KEY, DOWNLOADED_FW, SIGNATURE)

    def install_firmware(self, new_version):
        print("Installing firmware...")
        shutil.copy(DOWNLOADED_FW, ACTIVE_FW)

        with open(VERSION_FILE, "w") as f:
            f.write(new_version)

    def rollback(self):
        print("Rollback triggered!")

    def run_update(self):
        print("STATE: CHECK_VERSION")

        current_version = self.get_current_version()
        latest_version = self.check_latest_version()

        print(f"Current: {current_version} | Latest: {latest_version}")

        if latest_version == current_version:
            print("System up to date.")
            return

        if self.is_downgrade(current_version, latest_version):
            print("❌ Downgrade detected! Update rejected.")
            return

        print("STATE: DOWNLOAD")
        self.download_firmware()

        print("STATE: VERIFY")
        if not self.verify_firmware():
            self.rollback()
            return

        print("STATE: INSTALL")
        self.install_firmware(latest_version)

        print("STATE: SUCCESS")


if __name__ == "__main__":
    ota = OTAUpdateManager()
    ota.run_update()