# Secure Coding Review

## Project Overview

This project focuses on identifying and mitigating security vulnerabilities in a Python-based login application. The objective is to perform a secure code review, analyze potential risks, and implement security best practices to improve the application's security posture.

---

## Objective

- Review a Python application for security vulnerabilities.
- Identify insecure coding practices.
- Recommend remediation techniques.
- Implement a more secure version of the application.

---

## Technology Used

- Python 3
- bcrypt Library
- VS Code

---

## Vulnerable Application

The initial login system contained several security weaknesses:

### Identified Vulnerabilities

1. **Hardcoded Credentials**
   - Username and password were stored directly in the source code.

2. **Plain Text Password Storage**
   - Passwords were compared as plain text without encryption.

3. **No Brute Force Protection**
   - Unlimited login attempts were allowed.

4. **Lack of Input Validation**
   - User inputs were not validated or sanitized.

5. **No Account Lockout Mechanism**
   - Attackers could repeatedly attempt to guess passwords.

---

## Security Improvements Implemented

### 1. Password Hashing

Passwords are securely hashed using the bcrypt library instead of storing them in plain text.

### 2. Login Attempt Limitation

The application restricts users to a maximum of three failed login attempts.

### 3. Improved Authentication Process

User credentials are verified using bcrypt's secure password verification mechanism.

### 4. Better Security Practices

- Reduced exposure of sensitive information.
- Enhanced protection against credential theft.
- Improved resistance to brute-force attacks.

## How to Run

### Install Dependencies

```bash
pip install bcrypt
```

### Run Vulnerable Version

```bash
python vulnerable_login.py
```

### Run Secure Version

```bash
python secure_login.py
```

---

## Results

The secure version successfully addresses major security issues found in the vulnerable application by implementing password hashing and login attempt restrictions.

---

## Learning Outcomes

- Understanding Secure Coding Principles
- Identifying Common Security Vulnerabilities
- Password Hashing with bcrypt
- Authentication Security
- Secure Software Development Practices

---

## Conclusion

This project demonstrates how a basic code review can identify critical security vulnerabilities and how secure coding techniques can significantly improve application security. Implementing password hashing, authentication controls, and brute-force protection helps create safer and more reliable software systems.
