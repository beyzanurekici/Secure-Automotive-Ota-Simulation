# Secure Automotive OTA & Boot Validation Simulation

## Overview
This project simulates a secure Over-The-Air (OTA) firmware update system for an automotive ECU.

The system demonstrates how modern vehicles securely download, verify, and install firmware updates while preventing cybersecurity attacks.

## Features

- OTA firmware update simulation
- RSA digital signature verification
- Anti-downgrade protection
- Secure Boot simulation (SHA-256 hash validation)
- Firmware tamper detection

## Architecture

Server:
- Hosts firmware
- Provides version endpoint
- Signs firmware

ECU Client:
- Checks latest version
- Downloads firmware
- Verifies digital signature
- Prevents downgrade attacks
- Validates firmware integrity during boot

## Technologies Used

- Python
- FastAPI
- RSA Cryptography
- SHA-256 Hashing
- REST API

## Security Mechanisms Implemented

1. Digital Signature Verification  
2. Firmware Integrity Check  
3. Anti-Downgrade Logic  
4. Secure Boot Validation  

## Purpose

This project demonstrates understanding of automotive cybersecurity principles including OTA update security, firmware validation, and secure boot mechanisms.
