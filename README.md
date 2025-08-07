
# Enterprise IT & HR Support Chatbot

A real-time internal support chatbot designed to simulate L1 support for IT, HR, and application-related queries in an enterprise environment. Built using **spaCy** for NLP and **Streamlit** for interactive UI.

---

##  Features

•	35+ real-world support intents (VPN, SAP, payroll, MFA, onboarding, etc.)

•	NLP intent classification with `spaCy` PhraseMatcher

•	Automatic ticket logging with unique ID, timestamp, and intent classification

•	Ticket escalation for unrecognized queries

•	Chat history UI with Streamlit

•	Designed to reflect enterprise support environments


---

##  Project Structure

```
├── chatbot.py              # Main application file
├── intents.json            # Intent dataset with patterns & responses
├── ticket_log.json         # Auto-logged tickets
├── requirements.txt        # Dependencies for pip install
└── README.md              
```

---

## How to Run Locally

1. **Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

2. **Start the app**
```bash
streamlit run chatbot.py
```

3. **Start chatting!**

---

##  Deployment (Streamlit Cloud)

- Upload your repo to GitHub
- Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Connect your repo, select `chatbot.py` as the main file
- Done

---