from cryptography.hazmat.primitives import serialization
from crypto_utils import generate_keys, sign_firmware

# Firmware dosyasını oku
with open("server/firmware_v2.bin", "rb") as f:
    firmware_data = f.read()

private_key, public_key = generate_keys()

signature = sign_firmware(private_key, firmware_data)

# Signature kaydet
with open("server/firmware_v2.sig", "wb") as f:
    f.write(signature)

# Public key kaydet (ECU kullanacak)
with open("server/public_key.pem", "wb") as f:
    f.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("Firmware signed successfully.")