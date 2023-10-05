from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
# from langchain.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

load_dotenv(find_dotenv())
def image2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]['generated_text']
    print(text)
    return text

image2text("4.jpg")

## llm 
def generate_story(scenario):
    template = """
    You are a storyteller;
    You can generate a short story based on a simple narrative, the story should be no more than 20 words.

    CONTEXT: {scenario}
    STORY:
    """
    prompt = PromptTemplate.from_template(template = template)

    story_llm = LLMChain(llm = OpenAI(
                         model_name="gpt-3.5-turbo",temperature=1),prompt=prompt, verbose=True)
    story = story_llm.predict(scenario=scenario)

    print(story)
    return story

scenario = image2text("4.jpg")
story = generate_story(scenario)

    




