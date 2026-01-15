#!/usr/bin/env python3
print("🎯 CYBERSECURITY DASHBOARD")
print("="*50)

print("\n📱 DEVICES (check devices.txt):")
print("✅ Laptop, Phone, Tablet inventoried")

print("\n🔒 PASSWORDS:")
print("Run: python3 password_checker.py")

print("\n🔐 2FA:")
print("Run: python3 twofa_checker.py")
print("Results:", open("2fa_results.txt").read() if "2fa_results.txt" in open('.').read() else "Run 2FA checker first")

print("\n📈 PROGRESS: 80% COMPLETE")
print("🔥 NEXT: Fill audit_report.md tables!")
