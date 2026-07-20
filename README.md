# 🔍 TruthLens

> **AI-powered Hallucination & Trust Validator using Retrieval-Augmented Validation**

TruthLens is an AI fact-verification system that analyzes AI-generated responses, retrieves supporting evidence from trusted web sources, measures semantic similarity, and assigns a trust score with an explainable verdict.

---

## ✨ Features

- 🔎 Detects factual claims from AI responses
- 🏷️ Extracts named entities using spaCy
- 🌐 Searches the web for supporting evidence using Tavily
- 🧹 Cleans and filters noisy search results
- 📊 Ranks evidence using multiple scoring signals
- 🧠 Measures semantic similarity using Sentence Transformers
- ✅ Generates explainable trust scores and verdicts
- 💻 Interactive Streamlit dashboard

---

## 🏗️ Architecture

```text
User Input
     │
     ▼
Response Parser
     │
     ▼
Entity Extractor
     │
     ▼
Technology Detector
     │
     ▼
Query Builder
     │
     ▼
Search Service (Tavily)
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
Trust Report
```

---

## 🚀 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| UI | Streamlit |
| NLP | spaCy |
| Embeddings | Sentence Transformers |
| Search | Tavily API |
| Similarity | Cosine Similarity |
| Environment | python-dotenv |

---

## 📂 Project Structure

```text
TruthLens/
│
├── app.py
├── streamlit_app.py
├── src/
│   ├── models/
│   ├── modules/
│   ├── pipeline/
│   ├── services/
│   └── utils/
├── tests/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd TruthLens

pip install -r requirements.txt
```

Create a `.env` file:

```env
TAVILY_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python -m streamlit run streamlit_app.py
```

---

## 📸 Screenshots

### Home Page

(Add Screenshot)

---

### Validation Result

(Add Screenshot)

---

## 📈 Example

### Input

```
Python was created by Guido van Rossum.
React is maintained by Meta.
The Earth has two moons.
```

### Output

```
Claim 1
✔ SUPPORTED
Trust Score: 91%

Claim 2
✔ LIKELY SUPPORTED
Trust Score: 87%

Claim 3
✖ UNSUPPORTED
Trust Score: 28%
```

---

## 🔮 Future Work

- LLM-powered claim verification
- Multi-source agreement analysis
- Contradiction detection
- Browser extension
- REST API
- PDF report generation
- Batch processing

---

## 👨‍💻 Author

Vrushav Piyushkumar Patel

Computer Engineering Student
