import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="This Baptism Now Saves", page_icon="💧", layout="wide")

# Sidebar navigation
st.sidebar.image("https://via.placeholder.com/150x150/0A2540/FFFFFF?text=💧", width=150)  # Replace with your book cover later
st.sidebar.title("This Baptism Now Saves")
st.sidebar.markdown("**Why You Need to Rethink Your Position** — Bobby Warren")
page = st.sidebar.radio("Navigate the Study", 
    ["Home", "Diagnostic Questions (Ch1)", "Chapter Explorer", "Objection Crusher", "Study Guide Reflections", "Scripture Explorer", "Your Journey Tracker"])

# Home
if page == "Home":
    st.title("💧 This Baptism Now Saves")
    st.subheader("An interactive discipleship tool based on the book")
    st.markdown("""
    **You’ve read the book. Now live it.**  
    This app turns Bobby Warren’s biblical case into a guided, repeatable journey.  
    Answer the 5 questions → explore chapters → crush objections → reflect weekly → track your rethinking.
    
    Perfect for personal study, small groups, or preparing for baptism.
    """)
    st.success("**Monthly subscribers get:** new devotionals, group modes, and exportable PDFs.")
    st.info("Prototype by Grok • Built from your full manuscript")

# Diagnostic Questions
elif page == "Diagnostic Questions (Ch1)":
    st.title("Chapter 1: What Do You Actually Believe About Baptism?")
    st.markdown("Five honest questions before the arguments begin.")
    
    questions = [
        "Where did baptism come from?",
        "What does the word 'baptism' actually mean?",
        "Does baptism connect to salvation in any way?",
        "What is the right mode?",
        "Who is the right candidate?"
    ]
    
    responses = {}
    for q in questions:
        responses[q] = st.text_area(q, height=100, key=q)
    
    if st.button("Save My Answers & Get Personalized Path"):
        st.session_state['answers'] = responses
        st.success("Answers saved! Your path: Start with Ch2 if you wrestle with the 'works' objection.")

# Chapter Explorer (key excerpts)
elif page == "Chapter Explorer":
    st.title("Chapter Explorer")
    chapter = st.selectbox("Select Chapter", [
        "Ch2: If Baptism Is a Work...", "Ch3: Is Baptism the Sinner's Prayer?",
        "Ch4: Restoration Movement", "Ch5-6: The Word & Acts 2:38", 
        "Ch7-9: History & Paul’s Images", "Ch10-12: Symbol, Witnesses, Candidates",
        "Ch13: Hard Questions", "Epilogue: The Water"
    ])
    
    # Hardcoded key excerpts from your book (expandable)
    excerpts = {
        "Ch2: If Baptism Is a Work...": "Baptism is not a work of law. It is a gospel command — a faith-act where God does the saving work.",
        "Ch3: Is Baptism the Sinner's Prayer?": "1 Peter 3:21 calls baptism 'an appeal to God for a good conscience' — the real sinner's prayer happens in the water.",
        # Add more from PDF snippets as needed
    }
    st.markdown(f"**Key Excerpt:** {excerpts.get(chapter, 'Full text available in the book.')}")

# Objection Crusher
elif page == "Objection Crusher":
    st.title("Objection Crusher")
    objection = st.selectbox("Common Objection", [
        "Baptism is a work — we're not saved by works",
        "The sinner's prayer is how people get saved",
        "Baptism is just an outward sign",
        "Infant baptism is biblical",
        "What about the thief on the cross?"
    ])
    st.markdown("**Book Response:**")
    responses = {
        "Baptism is a work...": "Paul's 'works' = works of law (Torah). Baptism is a gospel command. See Titus 3:5 — the washing *is* the means of salvation.",
        # etc. — full responses pulled from your chapters
    }
    st.write(responses.get(objection, "Full answer in the book — let's discuss it!"))

# Study Guide Reflections
elif page == "Study Guide Reflections":
    st.title("Personal & Group Study Guide")
    st.markdown("Reflection questions from the book’s workbook section.")
    # Example for Ch1
    st.subheader("Chapter 1 Reflections")
    st.text_area("Personal: How did you arrive at what you believe about baptism?")
    # More prompts from PDF

# Scripture Explorer & Tracker
elif page == "Scripture Explorer":
    st.title("Key Scriptures")
    verse = st.selectbox("Key Verse", ["Acts 2:38", "1 Peter 3:21", "Romans 6:3-4", "Galatians 3:27"])
    st.markdown("**Book Commentary:** [Insert your exegesis here — e.g., eis = 'for' purpose]")

elif page == "Your Journey Tracker":
    st.title("Your Rethinking Journey")
    if 'progress' not in st.session_state:
        st.session_state.progress = 0
    st.progress(st.session_state.progress)
    st.slider("How much have you rethought your position? (0-100)", 0, 100, st.session_state.progress, key="prog")
    st.session_state.progress = st.session_state.prog
    st.markdown("**Next action:** Schedule your baptism or lead a group study.")

st.caption("Built live by Grok from your manuscript • Deploy this free & add Stripe for monthly subs in minutes. Want group mode, PDF exports, or full AI Q&A chatbot? Say the word and I’ll expand the code.")