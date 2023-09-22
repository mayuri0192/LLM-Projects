import youtube_dl
from flask import Flask, request 
from pytube import YouTube
from deepgram import Deepgram
import asyncio, json
from gpt3summarizer import GPT3Summarizer
import os
# from dotenv import load_dotenv

video_url = "https://www.youtube.com/watch?v=QMaWfbosR_E"

OPENAI_API_KEY = 'ENTER YOUR OPEN API KEY'
DEEPGRAM_API_KEY = 'ENTER YOUR DEEPGRAM KEY' 

filename = "How to Make RAG Chatbots FAST.mp3"
file_id = 1
transcript = "How to Make RAG Chatbots FAST.json"
max_sentences = 50

summarizer = GPT3Summarizer(OPENAI_API_KEY, DEEPGRAM_API_KEY, model_engine="gpt-3.5-turbo")
summarizer.summarize(file_id, video_url, filename, transcript, max_sentences)


