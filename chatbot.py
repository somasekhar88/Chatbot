
import streamlit as st
import json
import random
from datetime import datetime
import spacy
import en_core_web_sm
from spacy.matcher import PhraseMatcher

# Load spaCy model and matcher
nlp = en_core_web_sm.load()
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Load intents
with open("intents.json") as f:
    intents = json.load(f)

intent_responses = {}
for intent in intents:
    patterns = [nlp(text) for text in intent["patterns"]]
    matcher.add(intent["intent"], patterns)
    intent_responses[intent["intent"]] = intent["response"]

# Ticket log file
TICKET_LOG = "ticket_log.json"

def classify_intent(user_input):
    doc = nlp(user_input)
    matches = matcher(doc)
    if matches:
        match_id, start, end = matches[0]
        intent = nlp.vocab.strings[match_id]
        return intent, intent_responses[intent]
    return None, None

def log_ticket(user_query, intent=None):
    ticket = {
        "ticket_id": f"SR-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
        "query": user_query,
        "intent": intent if intent else "Unrecognized",
        "status": "Escalated" if not intent else "Resolved",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(TICKET_LOG, "r") as f:
            tickets = json.load(f)
    except FileNotFoundError:
        tickets = []

    tickets.append(ticket)

    with open(TICKET_LOG, "w") as f:
        json.dump(tickets, f, indent=2)

    return ticket

# Streamlit UI
st.title("Internal Application Support Chatbot 🤖")
st.markdown("Ask me about HR, IT, Application, or Security issues!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if user_input:
    intent, response = classify_intent(user_input)
    if response:
        bot_reply = response
    else:
        bot_reply = "I'm not sure how to help with that. I've logged your query for support to review."

    ticket = log_ticket(user_input, intent)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", f"{bot_reply} (Ticket ID: {ticket['ticket_id']})"))

for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
