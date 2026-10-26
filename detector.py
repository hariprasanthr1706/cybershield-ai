"""Baseline rule-based scam/phishing indicators. This is an educational prototype,
not a guarantee that content is safe or malicious.
"""
import re
from urllib.parse import urlparse

URGENCY_TERMS = [
    "urgent", "immediately", "verify now", "account suspended",
    "limited time", "act now", "claim your prize", "password expires"
]
PAYMENT_TERMS = [
    "send money", "transfer money", "upi pin", "one time password",
    "otp", "bank details", "gift card", "payment failed"
]
IMPERSONATION_TERMS = [
    "customer support", "bank account", "government refund",
    "delivery failed", "kyc update", "lottery winner"
]

def analyze_text(text: str) -> dict:
    lowered = text.lower()
    signals = []
    for term in URGENCY_TERMS:
        if term in lowered:
            signals.append(f"Urgency or pressure wording: “{term}”")
    for term in PAYMENT_TERMS:
        if term in lowered:
            signals.append(f"Payment or sensitive-information wording: “{term}”")
    for term in IMPERSONATION_TERMS:
        if term in lowered:
            signals.append(f"Possible impersonation theme: “{term}”")
    if re.search(r"\b(click here|open this link|login here)\b", lowered):
        signals.append("Encourages the recipient to click or log in")
    level = "High risk indicators" if len(signals) >= 3 else (
        "Review carefully" if signals else "No common indicators detected"
    )
    return {"level": level, "signals": signals,
            "advice": "Do not share passwords, OTPs, UPI PINs, or payment details. Verify through an official channel."}

def analyze_url(url: str) -> dict:
    candidate = url.strip()
    if "://" not in candidate:
        candidate = "https://" + candidate
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower()
    signals = []
    if parsed.scheme != "https":
        signals.append("URL does not use HTTPS")
    if not host:
        signals.append("Could not identify a valid hostname")
    if host and (host.startswith("xn--") or ".xn--" in host):
        signals.append("Hostname contains an internationalized/punycode label")
    if host and re.search(r"\d+\.\d+\.\d+\.\d+", host):
        signals.append("Uses an IP address instead of a typical domain name")
    if "@" in parsed.netloc:
        signals.append("Contains @ in the network location, which can be misleading")
    if host.count("-") >= 3:
        signals.append("Hostname contains several hyphens")
    if len(url) > 100:
        signals.append("Unusually long URL")
    if signals:
        level = "Review carefully"
    else:
        level = "No common indicators detected"
    return {"level": level, "signals": signals,
            "advice": "A URL can still be malicious even if no warning is detected. Open important services using their official app or a saved bookmark."}
