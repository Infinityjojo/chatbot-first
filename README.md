

📖 Intelligent Bible Chatbot
📌 Project Overview

The Intelligent Bible Chatbot is a web-based chatbot application that answers user questions using the Bible text as its knowledge source.
It uses Natural Language Processing (NLP) techniques to retrieve relevant Bible verses and provide short explanatory responses.

The chatbot also supports basic greetings such as hello, hi, and good morning.

🎯 Project Objectives

Build a chatbot based on a custom text corpus (Bible)

Apply text preprocessing techniques

Use TF-IDF and cosine similarity for intelligent information retrieval

Create an interactive Streamlit web interface

Deploy the application using GitHub and Streamlit Cloud

🧠 How the Chatbot Works

The chatbot follows a hybrid approach:

1️⃣ Rule-Based Logic

Detects and responds to greetings (e.g., “hi”, “good morning”)

2️⃣ NLP-Based Retrieval

Splits the Bible text into sentences

Cleans and preprocesses text (tokenization, stopword removal, lemmatization)

Converts sentences into TF-IDF vectors

Computes cosine similarity between user input and Bible verses

Retrieves the most relevant verse

Adds a short, topic-based explanation

⚠️ The chatbot does not generate new theology; it retrieves Scripture passages intelligently.

🛠 Technologies Used

Python 3

NLTK – text preprocessing

Scikit-learn – TF-IDF & cosine similarity

Streamlit – web application interface

Git & GitHub – version control and deployment

📂 Project Structure
chatbot-first/
│
├── chatbot.py          # Main application code
├── bible.txt           # Bible text file (KJV – public domain)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

📦 Installation & Setup (Local)
1️⃣ Clone the Repository
git clone https://github.com/your-username/chatbot-first.git
cd chatbot-first

2️⃣ Create a Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
streamlit run chatbot.py


Then open:

http://localhost:8501

☁️ Deployment (Streamlit Cloud)

Push your code to GitHub

Go to https://streamlit.io/cloud

Create a new app

Select:

Repository

Branch

chatbot.py as the entry file

Deploy 🚀

💬 Example Questions
Greetings

“Hi”

“Good morning”

“Hello”

Bible-Based Questions

“What is faith?”

“What does the Bible say about love?”

“Who is Jesus Christ?”

“What does Scripture say about forgiveness?”

“What is salvation?”

⚠️ Limitations

The chatbot does not perform deep theological reasoning

It retrieves verses rather than generating original interpretations

Best performance is achieved with clear, Bible-related questions

📚 Data Source

Bible Text: King James Version (KJV)

Source: Public domain (Project Gutenberg)

🧑‍🏫 Academic Explanation (For Assessment)

This project implements a retrieval-based chatbot using TF-IDF vectorization and cosine similarity to match user questions with relevant Bible verses. The system combines rule-based greetings with NLP techniques to deliver meaningful responses through a Streamlit interface.

✨ Future Improvements

Display book, chapter, and verse

Return top 3 relevant verses

Add topic buttons (Faith, Love, Salvation)

Improve semantic understanding using transformer models
