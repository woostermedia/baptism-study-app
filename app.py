import streamlit as st

st.set_page_config(page_title="This Baptism Now Saves", page_icon="💧", layout="wide")

st.sidebar.title("💧 This Baptism Now Saves")
st.sidebar.markdown("**Why You Need to Rethink Your Position**  \n*by Bobby Warren*")

page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "❓ Ch1: Diagnostic Questions",
    "📖 Full Chapter Explorer",
    "🛡️ Objection Crusher",
    "📝 Study Guide",
    "📜 Key Scriptures",
    "📈 My Journey"
])

if page == "🏠 Home":
    st.title("💧 This Baptism Now Saves")
    st.subheader("The Interactive Edition")
    st.markdown("""
    This is the living digital companion to Bobby Warren’s book.  
    Read key sections, answer the diagnostic questions, crush objections, and track your rethinking journey.
    """)
    st.success("All content drawn directly from the book.")

elif page == "❓ Ch1: Diagnostic Questions":
    st.title("Chapter 1 — What Do You Actually Believe About Baptism?")
    st.markdown("**Five questions worth sitting with** (from the book)")
    questions = [
        "Where did baptism come from?",
        "What does the word 'baptism' actually mean?",
        "Does baptism connect to salvation in any way?",
        "What is the right mode?",
        "Who is the right candidate?"
    ]
    for q in questions:
        st.text_area(q, height=120, key=q)

elif page == "📖 Full Chapter Explorer":
    st.title("Chapter Explorer")
    chapter = st.selectbox("Select a chapter/section", [
        "Introduction — Why I Wrote This",
        "Ch 2: If Baptism Is a Work...",
        "Ch 3: Is Baptism the Sinner's Prayer?",
        "Ch 4: Restoration Movement",
        "Key Passages"
    ])
    
    content = {
        "Introduction — Why I Wrote This": """I was baptized as an infant. I think... That experience sent me on a journey... This book is written for Christians who have dismissed the idea that baptism might actually be connected to salvation.""",
        
        "Ch 2: If Baptism Is a Work...": """The most common objection... Paul’s “works” means works of law (erga nomou), not gospel commands. Baptism is not a work of merit — it is a faith-act where God does the saving (Titus 3:5, Colossians 2:12).""",
        
        "Ch 3: Is Baptism the Sinner's Prayer?": """1 Peter 3:21 — Baptism now saves you... as an appeal (eperotema) to God for a good conscience. The real sinner's prayer happens in the water (Acts 22:16).""",
        
        "Ch 4: Restoration Movement": """The simple question: What does the New Testament actually say? Alexander Campbell and others recovered believer’s immersion for the forgiveness of sins.""",
        
        "Key Passages": """Acts 2:38 • Romans 6:3-4 • Galatians 3:27 • 1 Peter 3:21 • Colossians 2:12"""
    }
    
    st.markdown(f"**{chapter}**\n\n{content[chapter]}")
    st.caption("More full text can be added — let me know which chapter to expand next.")

elif page == "🛡️ Objection Crusher":
    st.title("🛡️ Objection Crusher")
    obj = st.selectbox("Choose an objection", [
        "Baptism is a work",
        "The sinner's prayer is how we’re saved",
        "Baptism is just an outward sign",
        "What about the thief on the cross?",
        "Infant baptism"
    ])
    answers = {
        "Baptism is a work": "Paul excludes 'works of law', not gospel responses. Baptism is where God works (Col 2:12).",
        "The sinner's prayer is how we’re saved": "The NT pattern is repentance + baptism as the appeal to God (1 Pet 3:21, Acts 22:16). The modern sinner's prayer is recent.",
        # Add more as needed
    }
    st.success(answers.get(obj, "See the book for the full response."))

elif page == "📝 Study Guide":
    st.title("📝 Full Study Guide Reflections")
    st.markdown("Interactive reflections from the book’s study guide.")
    ch = st.selectbox("Chapter", ["Ch1", "Ch2", "Ch3", "General"])
    st.text_area("My honest answers / What changed?", height=200)
    st.text_area("Action step (personal or group)", height=150)

elif page == "📜 Key Scriptures":
    st.title("Key Scriptures")
    verse = st.selectbox("Verse", ["Acts 2:38", "1 Peter 3:21", "Romans 6:3-4"])
    st.write("**Book commentary goes here** — I can paste the full exegesis from your manuscript.")

elif page == "📈 My Journey":
    st.title("My Rethinking Journey")
    progress = st.slider("How much has my view on baptism changed?", 0, 100, 40)
    st.progress(progress / 100)
    st.text_area("Key takeaway so far")
    st.text_area("Next step I'm prayerfully considering")

st.caption("Interactive companion to *This Baptism Now Saves* by Bobby Warren • Built live with Grok")
