from secure_boot import secure_boot

TRUSTED_HASH = "ef154537fd4944989f0bd1a7217bb3cd36601c3ca9d7223c0b7943555f8d02ae"

if __name__ == "__main__":
    secure_boot(TRUSTED_HASH)