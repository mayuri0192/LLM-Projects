## Youtube Video Summarizer

Pytube is used for downloading youtube video as mp3 file
[reference](https://www.geeksforgeeks.org/pytube-python-library-download-youtube-videos/)

Deepgram is used to transcribe the videos. 
DEEPGRAM_API_KEY should be set to the API key you created upon signing up for Deepgram here.

filename should be set to the path of the file you wish to transcribe, written as a string.
[reference](https://deepgram.com/learn/how-to-transcribe-and-analyze-any-youtube-video)

Setup your OpenAPI key for video summarization. [reference](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/)

## Installation

To use this script, you will need to install the necessary requirements. You can do this by running the following command in your terminal:

`pip install -r requirements.txt`

## Usage

To use this script, you will need to add your YouTube URL to the video_summarize.py file. Then, you can run the script by running the following command in your terminal:

`python video_summarize.py`

The script will download the audio for your video source, convert the speech to text via Deepgram API, summarize the text via OpenAI's GPT3 API, and chunk everything to fit within the limits of Whisper and GPT3 APIs. The script will also display the costs for both Whisper and GPT3 API usage.

