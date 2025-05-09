# YouTube-video-Q-A-Chatbot
A YouTube Q&amp;A chatbot built with Flask, LangChain, and OpenAI. This app fetches YouTube video transcripts and allows users to ask questions. Using FAISS for similarity search and LangChain's RAG approach, it provides accurate answers based on video content, all via a simple web interface.

# Features
Fetches YouTube Video Transcript: Uses the YouTube Transcript API to fetch captions (if available) for a given YouTube video.

Question Answering: Allows you to ask questions about the video, and the model answers based on the transcript context.

Contextual Answering: Uses LangChain with OpenAI embeddings to process the transcript and generate context-aware answers.

Web Application: A simple Flask-based web app with a user-friendly UI where users can input the YouTube video ID and their questions.

# Install Dependencies

Make sure you're using Python 3.9 or higher. Then, install the required dependencies:
pip install -r requirements.txt

# Set Up Environment Variables
Create a .env file in the root directory of the project and add your OpenAI API key:

# Author
Made with ❤️ by [Sunny Wazeer]. Feel free to connect with me.
