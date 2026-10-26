# Technical Design Document

## Purpose
CyberShield AI is an educational web prototype intended to help users notice common scam and phishing warning signs.

## Architecture

```text
User
 |
 v
Browser form (HTML/CSS)
 | message or URL
 v
Flask route (app.py)
 |
 v
Detector functions (detector.py)
 |-- message keyword/rule checks
 |-- URL structure/rule checks
 v
Result categories + warning explanations
 |
 v
Browser results and safety guidance
```

## Components
- **Presentation:** HTML form and responsive CSS.
- **Web server:** Flask receives the submitted text and URL.
- **Detection baseline:** transparent rule-based indicators. This version does not use a trained ML model.
- **Output:** a risk-indicator category, matching signals, and safety advice.

## Evaluation plan
Create a labelled dataset with documented provenance and permission to use it. Separate training and test data before model development. Measure precision, recall, F1-score, confusion matrix, and latency. Include benign messages and difficult examples to test false positives and false negatives. Do not report results until tests have actually been run.

## Limitations
- Rules cannot detect all scam styles and can flag harmless messages.
- URL indicators are heuristic and do not query reputation databases.
- A clean result is not a guarantee of safety.
- No automated external URL fetching is performed.
- Do not use this prototype as the sole basis for financial or security decisions.
