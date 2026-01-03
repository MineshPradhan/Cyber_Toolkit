# Random Readme

# 🔐 Cryptography Toolkit v1.0

## 📌 Overview

**Cryptography Toolkit v1.0** is a command-line based security utility designed to demonstrate **core cryptographic concepts** used in modern cybersecurity systems.

It enables users to **hash files, verify file integrity, encrypt/decrypt data using AES and RSA, and securely manage passwords**.

This toolkit is intended for:

- Cybersecurity students
- Cryptography learning projects
- Secure systems demonstrations
- Academic labs and mini-projects

---

## ✨ Features

- ✅ File hashing for tamper detection
- ✅ File integrity verification
- ✅ AES symmetric encryption & decryption
- ✅ RSA asymmetric encryption & decryption
- ✅ Password strength analysis
- ✅ Secure password hashing with salting

---

# Setup

1. Create a python environment variable - > python -m venv venv and activate it.
2. Add all the files inside the .venv file
3. Install the libraries in the virtual environment

<img width="855" height="487" alt="image" src="https://github.com/user-attachments/assets/3d2b94d2-2fbf-4525-b900-66c9228eaf3b" />

## 🧭 Menu Options

```
1. Hash File
2. Check File Integrity
3. AES Encrypt / Decrypt
4. RSA Encrypt / Decrypt
5. Password Manager
0. Exit
```

---

## 🔑 Cryptographic Algorithms Used

---

## 🔐 Advanced Encryption Standard (AES)

## 🔑 Rivest–Shamir–Adleman (RSA)

### 🔐 Use Case in This Toolkit

- Encrypt small messages securely
- Decrypt using private key
- Demonstrates public/private key cryptography

> ⚠️ RSA is not suitable for large data — it is commonly used to encrypt AES keys instead.
> 

---

## 🔎 Hashing & File Integrity

### 📖 Hashing

Hashing converts data into a **fixed-length digest** using one-way functions.

Common properties:

- Deterministic
- Irreversible
- Collision-resistant

### 🔐 Hash Algorithms (Examples)

- SHA-256
- SHA-512

### 🧪 File Integrity Verification

1. Hash file initially
2. Store hash securely
3. Re-hash file later
4. Compare both hashes

If hashes differ → **File tampered**

---

## 🔐 Password Management & Security

### 🔑 Password Strength Analysis

The toolkit evaluates:

- Length
- Use of symbols
- Upper/lowercase characters
- Common patterns

### 🔒 Secure Password Storage

- Passwords are **never stored in plaintext**
- Uses:
    - **Salt** (random value)
    - **Strong hashing algorithm (bcrypt)**

### 🔁 Verification Process

1. User enters password
2. Hash is recomputed with stored salt
3. Hashes are compared securely

---

## 🔹 Logical Architecture Diagram (Textual Representation)

```
+--------------------------------------------------+
|User (CLI)                      |
|  (Menu Selection &Input Commands)               |
+------------------------+-------------------------+
                         |
                         v
+--------------------------------------------------+
|            Application Controller                |
|  - MenuHandler                                  |
|  -Input Validation                              |
|  - Operation Routing                             |
+------------------------+-------------------------+
                         |
                         v
+--------------------------------------------------+
|           Cryptographic Engine Layer             |
|                                                  |
|  +----------------+  +------------------------+ |
|  | Hashing Module |  |Password Manager      | |
|  | (SHA-256)      |  |  (bcrypt + salt)       | |
|  +----------------+  +------------------------+ |
|                                                  |
|  +----------------+  +------------------------+ |
|  | AES Module     |  |  RSA Module             | |
|  | (Encrypt/Dec)  |  | (Public/Private Keys)  | |
|  +----------------+  +------------------------+ |
+------------------------+-------------------------+
                         |
                         v
+--------------------------------------------------+
|Storage & Verification Layer             |
|  -Encrypted Files                               |
|  - HashValues                                   |
|  -Password Hash Store                           |
+--------------------------------------------------+
```

## 🛡️ Security Best Practices Followed

- ✔ Salting passwords before hashing
- ✔ Strong cryptographic primitives
- ✔ Separation of encryption & hashing
- ✔ Secure key handling

---

## 🧑‍💻 Technologies Used

- Python 3
- Cryptography libraries
- bcrypt
- hashlib

---

## 📚 Learning Outcomes

- Understand symmetric vs asymmetric encryption
- Learn real-world cryptographic workflows
- Apply hashing for integrity verification
- Implement secure password storage
- Gain hands-on experience with AES & RSA

---

## 🚀 Future Enhancements

- Digital Signatures
- AES-GCM authentication
- Key storage using HSM concepts
- GUI-based interface
- Secure key exchange (Diffie-Hellman)

---

## 📜 License

This project is for **educational purposes only**.

Use responsibly and ethically.

---
