from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def verify_signature(public_key_path, firmware_path, signature_path):
    # Public key yükle
    with open(public_key_path, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )

    # Firmware yükle
    with open(firmware_path, "rb") as f:
        firmware_data = f.read()

    # Signature yükle
    with open(signature_path, "rb") as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            firmware_data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("✅ Signature VALID. Firmware trusted.")
        return True

    except Exception:
        print("❌ Signature INVALID. Update rejected.")
        return False


if __name__ == "__main__":
    verify_signature(
        "server/public_key.pem",
        "server/firmware_v2.bin",
        "server/firmware_v2.sig"
    )