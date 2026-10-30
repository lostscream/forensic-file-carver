# Forensic Signature-Based File Carver

A lightweight raw byte analysis tool designed for Digital Forensics investigations. It extracts deleted or hidden file artifacts from damaged file systems or unallocated memory blocks (raw binary dumps) using file signature (Magic Byte) matching.

## Supported Signatures
- **JPEG:** `FF D8 FF` ... `FF D9`
- **PNG:** `89 50 4E 47` ... `49 45 4E 44 AE 42 60 82`

## Usage
```bash
python carver.py disk_dump.raw
