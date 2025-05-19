# Data Masking Extension for Secure Password Manager

This extension **demonstrates function overriding** to add **data masking** to the existing **Secure Password Manager (SPM)**.

This demonstrates how extending functionality through **function overriding** can add features like **privacy-preserving data masking** without changing the core application.

## How It Works
- This script **imports the original SPM** and **overrides** the `view_entries` function.
- The overridden function **masks email addresses** by partially hiding the username part (e.g., `j***e@example.com`).
- All other features of the password manager remain the same.

## How to Use
1. Make sure the original **SPM** project is located in `../SPM`.
2. Run this script instead of the original SPM:
   ```
   python data_masking_extension.py
   ```
3. When viewing entries, **emails will be masked**, while other data (such as decrypted passwords) will still display fully.
