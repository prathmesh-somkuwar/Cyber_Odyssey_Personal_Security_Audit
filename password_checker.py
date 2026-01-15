#!/usr/bin/env python3
import re

def check_password(password):
    score = 0
    issues = []
    
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: issues.append("Length < 8")
    
    if re.search(r'[A-Z]', password): score += 1
    else: issues.append("No UPPERCASE")
    
    if re.search(r'[a-z]', password): score += 1
    else: issues.append("No lowercase")
    
    if re.search(r'\d', password): score += 1
    else: issues.append("No numbers")
    
    if re.search(r'[!@#$%^&*]', password): score += 1
    else: issues.append("No special chars")
    
    strength = "🟢 EXCELLENT" if score >= 6 else "🟡 GOOD" if score >= 4 else "🔴 WEAK"
    return f"{strength} ({score}/6): {', '.join(issues)}"

while True:
    pwd = input("\nPassword test (quit to exit): ")
    if pwd.lower() == 'quit': break
    print(check_password(pwd))
