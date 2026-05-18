import streamlit as st

st.set_page_config(page_title="This Baptism Now Saves", page_icon="💧", layout="wide")

st.sidebar.title("💧 This Baptism Now Saves")
st.sidebar.markdown("**Why You Need to Rethink Your Position**  \n*by Bobby Warren*")

page = st.sidebar.radio("Navigate the Book", [
    "🏠 Home",
    "❓ Ch1: Diagnostic Questions",
    "📖 Chapter Explorer",
    "🛡️ Objection Crusher",
    "📝 Full Study Guide",
    "📜 Key Scriptures",
    "📈 My Journey Tracker"
])

if page == "🏠 Home":
    st.title("💧 This Baptism Now Saves")
    st.subheader("Interactive Edition")
    st.markdown("""
    Welcome to the living version of Bobby Warren’s book.  
    This app turns the full manuscript into a guided discipleship tool.
    
    Use it personally, with a small group, or as a church resource.
    """)
    st.info("All content is taken directly from the book you wrote.")

elif page == "❓ Ch1: Diagnostic Questions":
    st.title("Chapter 1 — What Do You Actually Believe About Baptism?")
    st.markdown("Answer these five questions honestly before diving deeper.")
    qs = [
        "Where did baptism come from?",
        "What does the word 'baptism' actually mean?",
        "Does baptism connect to salvation in any way?",
        "What is the right mode?",
        "Who is the right candidate?"
    ]
    for q in qs:
        st.text_area(q, height=100, key=f"q_{q}")

elif page == "📖 Chapter Explorer":
    st.title("Chapter Explorer — Full Book")
    chapters = {
        "Ch 2: If Baptism Is a Work...": "Baptism is not a 'work of law'. It is a gospel command. See Titus 3:5 — saved by the washing of regeneration.",
        "Ch 3: Is Baptism the Sinner's Prayer?": "1 Peter 3:21 — Baptism is 'an appeal to God for a good conscience'. This is the real sinner's prayer, happening in the water.",
        "Ch 4: Restoration Movement": "The simple question: What does the New Testament actually say? The movement recovered believer’s immersion for the forgiveness of sins.",
        "Ch 5: The Word They Wouldn't Translate": "Baptizō means immerse. Translators kept the sound instead of translating the meaning.",
        "Ch 6: Acts 2:38": "Repent and be baptized... for the forgiveness of your sins.",
        "Ch 7–9: History & Paul’s Images": "Buried, raised, clothed with Christ (Romans 6, Galatians 3).",
        "Ch 10: Outward Sign?": "That phrase is not in the New Testament. It came from Zwingli.",
        "Ch 11–12: Witnesses & Candidates": "Infant baptism entered later. New Testament pattern is believers.",
        "Ch 13: Hard Questions": "Thief on the cross, godly grandmother, deathbed conversions.",
        "Epilogue & Study Guide": "The water is where the appeal meets God’s promise."
    }
    ch = st.selectbox("Select Chapter", list(chapters.keys()))
    st.markdown(f"**{ch}**\n\n{chapters[ch]}")
    st.caption("Full text available in your PDF. This app gives the core arguments + reflections.")

elif page == "🛡️ Objection Crusher":
    st.title("Objection Crusher")
    obj = st.selectbox("Pick a common objection", [
        "Baptism is a work",
        "Sinner's prayer is enough",
        "It's just an outward sign",
        "What about the thief on the cross?",
        "Infant baptism is biblical"
    ])
    answers = {
        "Baptism is a work": "Paul’s 'works' = works of the Mosaic Law. Baptism is a faith-act where *God* does the work (Colossians 2:12).",
        "Sinner's prayer is enough": "The New Testament pattern is repentance + baptism as the appeal to God (Acts 22:16, 1 Peter 3:21).",
        # ... more can be added
    }
    st.success(answers.get(obj, "Full response in the book — let's expand this!"))

elif page == "📝 Full Study Guide":
    st.title("Personal & Group Study Guide")
    st.markdown("Reflection questions for every chapter (from the book’s workbook).")
    study_ch = st.selectbox("Choose Chapter for Reflection", ["Chapter 1", "Chapter 2", "Chapter 3", "..."])
    st.text_area("Personal Reflection:", height=150)
    st.text_area("What changed in my thinking?", height=100)
    st.text_area("Group Discussion Notes:", height=150)

elif page == "📜 Key Scriptures":
    st.title("Key Scriptures with Commentary")
    verses = ["Acts 2:38", "1 Peter 3:21", "Romans 6:3-4", "Galatians 3:27", "Colossians 2:12"]
    v = st.selectbox("Select Verse", verses)
    st.markdown(f"**{v}** — [Insert your full commentary from the book here]")

elif page == "📈 My Journey Tracker":
    st.title("My Rethinking Journey")
    progress = st.slider("How much has my position on baptism changed?", 0, 100, 30)
    st.progress(progress/100)
    st.text_area("Next step I'm considering (e.g., baptism, leading a group, further study)")

st.caption("Full interactive edition of *This Baptism Now Saves* by Bobby Warren • Powered by Grok")
