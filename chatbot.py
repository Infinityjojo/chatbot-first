import streamlit as st
import nltk
import string

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# NLTK downloads
# --------------------------------------------------
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")

# --------------------------------------------------
# Load Bible text
# --------------------------------------------------
with open("bible.txt", "r", encoding="utf-8") as f:
    data = f.read().replace("\n", " ")

sentences = sent_tokenize(data)

# --------------------------------------------------
# Preprocessing
# --------------------------------------------------
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]
    return " ".join(tokens)

processed_sentences = [preprocess(sentence) for sentence in sentences]

# --------------------------------------------------
# TF-IDF
# --------------------------------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_sentences)

# --------------------------------------------------
# Greetings
# --------------------------------------------------
GREETINGS = {
    "hello": "Hello! How can I help you from the Bible today?",
    "hi": "Hi! Ask me any Bible-related question.",
    "hey": "Hey! What would you like to know from Scripture?",
    "good morning": "Good morning! May God's Word guide you today.",
    "good evening": "Good evening! How can I help you from the Bible?"
}

def greeting_response(text):
    text = text.lower()
    for greeting in GREETINGS:
        if greeting in text:
            return GREETINGS[greeting]
    return None
def normalize_query(query):
    query = query.strip().lower()
    if len(query.split()) == 1:
        return f"what is {query} according to the bible"
    return query


# --------------------------------------------------
# Topic-based explanations (SAFE & SHORT)
# --------------------------------------------------
EXPLANATIONS = {
    "faith": "The Bible teaches that faith is trusting in God and believing in His promises.",
    "love": "According to the Bible, love is central to God's nature and how believers should live.",
    "sin": "The Bible describes sin as anything that goes against God's will and separates people from Him.",
    "forgiveness": "Scripture teaches that God forgives those who sincerely repent and forgive others.",
    "salvation": "The Bible teaches that salvation comes through faith in Jesus Christ.",
    "prayer": "Prayer is presented in the Bible as communication between people and God.",
    "jesus": "The Bible reveals Jesus Christ as the Son of God and Savior of the world."
}

def get_explanation(question):
    question = question.lower()
    for keyword in EXPLANATIONS:
        if keyword in question:
            return EXPLANATIONS[keyword]
    return "Here is a relevant passage from the Bible related to your question."

# --------------------------------------------------
# Intelligent verse retrieval
# --------------------------------------------------
def get_best_verse(question):
    question = normalize_query(question)
    processed_question = preprocess(question)
    question_vector = vectorizer.transform([processed_question])

    similarities = cosine_similarity(question_vector, tfidf_matrix)[0]

    # Get top 5 candidate verses
    top_indices = similarities.argsort()[-5:][::-1]

    best_sentence = None
    best_score = 0

    for idx in top_indices:
        sentence = sentences[idx]

        # Prefer explanatory verses (longer & not questions)
        length_score = len(sentence.split())
        is_question = sentence.strip().endswith("?")

        score = similarities[idx] + (length_score * 0.002)

        if not is_question and score > best_score:
            best_score = score
            best_sentence = sentence

    if best_sentence is None:
        return None

    return best_sentence

# --------------------------------------------------
# Chatbot logic
# --------------------------------------------------
def chatbot(question):
    greet = greeting_response(question)
    if greet:
        return greet

    explanation = get_explanation(question)
    verse = get_best_verse(question)

    if verse is None:
        return (
            explanation
            + "\n\n📖 Verse:\n"
            + "I could not find a clear verse. Please rephrase your question."
        )

    return (
        "🧠 Explanation:\n"
        + explanation
        + "\n\n📖 Bible Verse:\n"
        + verse
    )

# --------------------------------------------------
# Streamlit app
# --------------------------------------------------
def main():
    st.title("📖 Intelligent Bible Chatbot")
    st.write(
        "This chatbot answers questions using **short explanations** "
        "and **relevant Bible verses**, powered by NLP."
    )

    user_input = st.text_input("You:")

    if st.button("Submit"):
        response = chatbot(user_input)
        st.write("🤖 Chatbot:")
        st.write(response)

# --------------------------------------------------
# Run
# --------------------------------------------------
if __name__ == "__main__":
    main()
