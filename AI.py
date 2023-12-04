import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import openai

# Set up your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Function to listen to the question
def listen_question():
    recognizer = sr.Recognizer()
    question = ""

    with sr.Microphone() as source:
        print("Ask your question:")
        audio = recognizer.listen(source)

    try:
        question = recognizer.recognize_google(audio, language="en-US")
        print("Thanks for your question: ", question)
    except sr.UnknownValueError:
        print("Could not understand your question. Please repeat.")
    except sr.RequestError as e:
        print("There was a connection error. Please try again later: ", e)

    return question

# Function to generate an AI-based answer related to STC Saudi Arabia
def generate_ai_answer(question):
    # Modify the prompt to include STC Saudi Arabia
    prompt = f"Answer the following question about STC Saudi Arabia: {question}"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50  # Adjust the response length as needed
    )

    answer = response.choices[0].text.strip()
    return answer

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    tts.save("answer.mp3")

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

# Main loop
if __name__ == "__main__":
    while True:
        question = listen_question()
        answer = generate_ai_answer(question)
        print("AI Answer: ", answer)
        text_to_speech(answer)