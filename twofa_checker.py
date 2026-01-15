#!/usr/bin/env python3
accounts = ["Gmail", "Instagram", "PhonePe", "Bank"]

print("🔐 2FA AUDIT")
enabled = 0
results = []

for acc in accounts:
    status = input(f"{acc} 2FA? (y/n): ").lower()
    result = "🟢 YES" if status in 'yn' else "🔴 NO"
    results.append(f"{acc}: {result}")
    if status == 'y': enabled += 1

print(f"\n✅ 2FA ENABLED: {enabled}/4")
with open("2fa_results.txt", "w") as f:
    f.write("\n".join(results))
print("💾 Saved to 2fa_results.txt")
