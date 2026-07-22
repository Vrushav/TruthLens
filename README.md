# 🔍 TruthLens

> **An AI-powered toolkit for secure code analysis and AI response validation.**

TruthLens is an open-source Python toolkit that helps developers **analyze Python code** for security, runtime, syntax, and AI-related issues while also **validating AI-generated responses** using retrieval-augmented verification, semantic similarity, and explainable trust scoring.

Whether you're reviewing source code or verifying factual claims produced by AI systems, TruthLens provides detailed reports, confidence scores, and actionable insights.

---

## ✨ Features

### 🛡 Code Analysis

- 🔎 Syntax analysis
- ⚙ Runtime issue detection
- 🔒 Security vulnerability detection
- 🤖 AI hallucination detection in generated code
- 📚 Rule-based Python API validation
- 📄 HTML report generation
- 📊 JSON report generation
- 💻 Command Line Interface (CLI)

### 🤖 AI Response Validation

- 📝 Claim extraction
- 🏷 Named Entity Recognition (spaCy)
- 🌐 Live web evidence collection
- 🧹 Evidence cleaning
- 📊 Evidence ranking
- 🧠 Semantic similarity verification
- ✅ Explainable trust scores
- 📑 Supporting evidence visualization

---

# 🏗 Architecture

## Code Analysis Pipeline

```text
Python Source
      │
      ▼
Response Parser
      │
      ▼
Analysis Pipeline
      │
      ├── Syntax Analyzer
      ├── Runtime Analyzer
      ├── Security Analyzer
      └── Hallucination Analyzer
      │
      ▼
Trust Engine
      │
      ▼
HTML Report
JSON Report
```

---

## AI Response Validation Pipeline

```text
AI Response
      │
      ▼
Response Parser
      │
      ▼
Entity Extraction
      │
      ▼
Technology Detection
      │
      ▼
Query Builder
      │
      ▼
Search Service
      │
      ▼
Evidence Cleaner
      │
      ▼
Evidence Ranker
      │
      ▼
Semantic Verifier
      │
      ▼
Trust Engine
      │
      ▼
Validation Report
```

---

# 🚀 Tech Stack

| Category | Technologies |
|------------|-----------------------------|
| Language | Python |
| NLP | spaCy |
| Embeddings | Sentence Transformers |
| Search | Tavily API |
| Reports | HTML, JSON |
| CLI | argparse |
| UI | Streamlit (Validation Demo) |

---

# 📂 Project Structure

```text
TruthLens/
│
├── assets/
├── data/
├── docs/
├── examples/
├── reports/
├── src/
│   ├── analysis/
│   ├── parser/
│   ├── pipeline/
│   ├── report/
│   ├── rules/
│   ├── services/
│   ├── verification/
│   └── knowledge/
│
├── templates/
├── tests/
├── truthlens/
│   ├── __init__.py
│   └── __main__.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙ Installation

```bash
git clone https://github.com/yourusername/TruthLens.git

cd TruthLens

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

---

# 🚀 Quick Start

## Code Analysis

```bash
python -m truthlens analyze examples/bad_code.py
```

Generates

- Console Report
- HTML Dashboard
- JSON Report

---

## AI Response Validation

```bash
streamlit run streamlit_app.py
```

Paste an AI-generated response and receive

- Trust Score
- Supporting Evidence
- Similarity Scores
- Explainable Verdict

---

# 📊 Sample Output

## Code Analysis

```
Trust Score

68%

Production Ready

No

Security Issues

2

Runtime Issues

1
```

---

## AI Validation

```
Claim

Python was created by Guido van Rossum.

Verdict

SUPPORTED

Trust Score

94%

Supporting Evidence

Python Official Documentation
Wikipedia
Britannica
```

---

# 📸 Screenshots

Coming soon

- CLI
- HTML Dashboard
- Validation Dashboard

---

# 🛣 Roadmap

## Version 1.0

- ✅ CLI
- ✅ HTML Reports
- ✅ JSON Reports
- ✅ Runtime Analyzer
- ✅ Security Analyzer
- ✅ Hallucination Analyzer
- ✅ AI Response Validation

## Version 1.1

- ⏳ Dark Mode Dashboard
- ⏳ Batch Analysis
- ⏳ PDF Reports

## Version 2.0

- ⏳ VS Code Extension
- ⏳ GitHub Action
- ⏳ REST API
- ⏳ React Dashboard

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, open issues, or submit pull requests.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Vrushav Piyushkumar Patel**

Computer Engineering Student

Building developer tools focused on AI trust, software quality, and secure code analysis.