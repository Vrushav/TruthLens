import streamlit as st

from src.pipeline.validation_pipeline import ValidationPipeline
from src.utils.text_cleaner import clean_snippet

# ---------------- Page Configuration ---------------- #

st.set_page_config(page_title="TruthLens", page_icon="🔍", layout="wide")

pipeline = ValidationPipeline()

# ---------------- Header ---------------- #

st.title("🔍 TruthLens")

st.markdown("""
### AI Hallucination & Trust Validator

Validate AI-generated responses using:

- 🌐 Live Web Search
- 🧠 Semantic Similarity
- 📊 Trust Scoring
- 📄 Explainable Evidence
""")

st.divider()

# ---------------- Input ---------------- #

response = st.text_area(
    "📝 Paste AI Response",
    placeholder="""Example:

Python was created by Guido van Rossum.
React is maintained by Meta.
The Earth has two moons.
""",
    height=220,
)

validate = st.button("🚀 Validate Response", use_container_width=True)

# ---------------- Validation ---------------- #

if validate:

    if not response.strip():
        st.warning("⚠ Please enter an AI response.")
        st.stop()

    with st.spinner("Analyzing response..."):

        claims = pipeline.validate(response)

    st.success(f"Analysis completed! Found {len(claims)} claim(s).")

    # ---------------- Results ---------------- #

    for index, claim in enumerate(claims, start=1):

        st.divider()

        st.subheader(f"📌 Claim {index}")

        st.write(claim.text)

        # -------------------------------------------------
        # Safely handle optional trust_result
        # -------------------------------------------------

        if claim.trust_result is None:
            st.error("No trust analysis available.")
            continue

        verdict = claim.trust_result.verdict

        if verdict == "SUPPORTED":
            st.success("🟢 SUPPORTED")

        elif verdict == "LIKELY SUPPORTED":
            st.info("🟡 LIKELY SUPPORTED")

        elif verdict == "UNCERTAIN":
            st.warning("🟠 UNCERTAIN")

        else:
            st.error("🔴 UNSUPPORTED")

        score = claim.trust_result.trust_score

        st.progress(score / 100)

        st.metric("Trust Score", f"{score:.2f}%")

        st.write("### 📄 Supporting Evidence")

        for evidence in claim.evidence:

            with st.expander(evidence.title):

                st.write(f"**Source:** {evidence.source}")

                st.write(f"**Semantic Match:** {evidence.similarity_score:.2%}")

                st.markdown(
                    f"<div style='font-size:15px'>{evidence.snippet}</div>",
                    unsafe_allow_html=True,
                )

                st.link_button("🔗 Open Source", evidence.url)
