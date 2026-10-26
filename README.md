CyberShield AI: Intelligent Scam and Phishing Detection

1. Project Overview

CyberShield AI is a cybersecurity awareness web application designed to help users identify potential scam messages and phishing URLs. It analyses suspicious content, highlights common warning signs, and provides simple safety recommendations.

The project aims to promote digital safety among students, senior citizens, and the wider community.

2. Problem Statement

Online users frequently encounter phishing links, fraudulent messages, fake offers, and misleading requests for personal or financial information. Many people struggle to recognise these threats before clicking a link or sharing sensitive information.

CyberShield AI aims to make scam awareness easier through an accessible web-based detection tool.

3. Objectives

- Identify common warning signs in suspicious messages.
- Analyse URLs for potentially misleading characteristics.
- Explain why particular content may be suspicious.
- Provide practical cybersecurity awareness tips.
- Encourage safer online behaviour.

4. Features

- Message Analysis: Checks text for suspicious urgency, payment requests, and impersonation-related phrases.
- URL Analysis: Checks for selected URL warning signs, including insecure HTTP connections and IP-address-based URLs.
- Risk Indicators: Displays a category based on the warning patterns detected.
- Safety Recommendations: Provides advice to help users avoid common online scams.
- Simple Web Interface: Allows users to submit messages and URLs for analysis.

5. Technology Stack

- Programming Language: Python
- Web Framework: Flask
- Frontend: HTML, CSS, JavaScript
- Detection: Rule-based text and URL analysis
- Testing: Python unittest

Current implementation note: This starter version uses rule-based detection. A trained machine-learning classifier is planned for a future version.

6. Project Architecture

1. The user enters a suspicious message or URL.
2. The Flask application receives the submitted input.
3. The detector checks for configured warning patterns.
4. The application displays the detected indicators and safety advice.
5. The user reviews the results and makes an informed decision.

7. Project Structure

cybershield-ai/
├── app.py
├── detector.py
├── requirements.txt
├── README.md
├── LICENSE
├── data/
│   └── sample_cases.csv
├── docs/
│   └── architecture.md
├── tests/
│   └── test_detector.py
├── static/
│   └── style.css
└── templates/
    └── index.html

8. Installation and Setup

Prerequisites

- Python 3.10 or newer
- pip package manager
- A web browser

Step 1: Clone the Repository

git clone https://github.com/hariprasanthr1706/cybershield-ai.git
cd cybershield-ai

Step 2: Create a Virtual Environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

Activate it on macOS or Linux:

source .venv/bin/activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run the Application

python app.py

Open the following address in your browser:

"http://127.0.0.1:5000"

9. Sample Test Cases

Input| Expected behaviour
A message demanding an OTP urgently| Highlights urgency and sensitive-information indicators
A normal college announcement| Reports no configured message warning patterns
An HTTP URL containing an IP address| Highlights relevant URL warning indicators
"https://example.com"| Reports no configured URL warning patterns

These are example test cases, not measured model-performance results.

10. Testing

Run the included tests using:

python -m unittest discover -s tests -v

The tests cover selected message and URL detection rules.

11. Social Impact and UN SDGs

SDG 9 — Industry, Innovation and Infrastructure: Promotes accessible technological innovation for digital safety.

SDG 16 — Peace, Justice and Strong Institutions: Supports awareness and prevention efforts related to online fraud and deceptive communications.

The project aims to improve digital awareness and help people recognise potential online threats.

12. Limitations

- Rule-based detection may miss sophisticated scams.
- Legitimate messages may sometimes trigger warnings.
- The application does not verify URLs against live threat-intelligence databases.
- A result without warnings does not guarantee that content is safe.
- The current version is an educational prototype, not a replacement for professional cybersecurity tools.

13. Future Enhancements

- Integrate a trained machine-learning model.
- Evaluate performance using a documented, labelled dataset.
- Add multilingual scam-message analysis.
- Improve URL threat analysis.
- Develop a mobile-friendly interface.
- Conduct usability testing and security reviews.

14. Privacy and Security

Do not enter passwords, OTPs, UPI PINs, bank credentials, or confidential personal information. The current prototype processes submitted content locally within the application and does not call external analysis services.

Public deployment requires additional security configuration and testing.

15. Author

Hari Prasanth R.
Department: Computer Science and Engineering — Artificial Intelligence and Machine Learning
Institution: Sri Sairam Institute of Technology

GitHub: https://github.com/hariprasanthr1706

16. License

This project is released under the MIT License. Refer to the "LICENSE" file for details.
