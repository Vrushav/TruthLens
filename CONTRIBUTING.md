# Contributing to TruthLens

First off, thank you for your interest in contributing to TruthLens!

TruthLens aims to improve trust in AI-generated and developer-written Python code through static analysis, security checks, and trust scoring. Contributions of all sizes are welcome.

---

## Ways to Contribute

You can contribute by:

- Reporting bugs
- Suggesting new features
- Improving documentation
- Optimizing performance
- Adding new security rules
- Improving AI trust analysis
- Writing tests
- Fixing issues

---

## Getting Started

### 1. Fork the repository

Click **Fork** on GitHub and clone your fork.

```bash
git clone https://github.com/<your-username>/TruthLens.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it.

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Development Workflow

Create a new branch:

```bash
git checkout -b feature/your-feature
```

Make your changes.

Run the application:

```bash
truthlens analyze examples/mixed_risks.py
```

Commit using meaningful commit messages, for example:

```text
feat: add SQL injection detector
fix: improve trust score calculation
docs: update README
```

Push your branch and open a Pull Request.

---

## Coding Guidelines

- Follow PEP 8.
- Write clear and maintainable code.
- Keep functions focused on a single responsibility.
- Add comments where the logic is non-obvious.
- Maintain the existing project structure.

---

## Reporting Bugs

When reporting a bug, please include:

- Operating System
- Python version
- TruthLens version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages (if any)

---

## Feature Requests

Feature requests should include:

- Problem statement
- Proposed solution
- Example use case
- Expected benefit

---

## Code of Conduct

By participating in this project, you agree to follow the project's Code of Conduct.

Thank you for helping improve TruthLens!