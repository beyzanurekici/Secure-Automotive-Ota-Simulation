import hashlib

ACTIVE_FW = "firmware_storage/active_firmware.bin"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def secure_boot(expected_hash):
    print("SECURE BOOT: Verifying firmware integrity...")

    current_hash = calculate_hash(ACTIVE_FW)

    if current_hash != expected_hash:
        print("🚨 Secure Boot Failed. System halted.")
        return False

    print("✅ Secure Boot Passed. System starting...")
    return True