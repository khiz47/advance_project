import json
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'Body')
from Speak import Speak
from sumy.parsers.plaintext import PlaintextParser


# Function to read the intro_paragraph from the file
def read_intro_paragraph_from_file():
    try:
        with open(r"Features\wikistore.md", "r", encoding="utf-8") as file:
            intro_paragraph = file.read().strip()
        return intro_paragraph
    except FileNotFoundError:
        return ""

# Function to clear the content of the file
def clear_file_content(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("")

def InputExecution1(tag, query):
    data = open("Brain\intents.json").read()
    intents = json.loads(data)
    intent = intents["intents"]
    
    # Find the correct intent based on the given tag
    intent_data = next(item for item in intent if item["tag"] == tag)
    patterns = intent_data["patterns"]
    
    name = ' '.join(query).lower()  # Convert the list of words into a single string
    
    for pattern in patterns:
        if pattern in name:
            name = name.replace(pattern, "").strip()  # Remove pattern and leading/trailing spaces
            break  # Exit loop after removing the pattern
    
    # Inside the "summary" tag block
    if tag == "summary":
        from sumy.parsers.plaintext import PlaintextParser  # Add this import
        from sumy.nlp.tokenizers import Tokenizer
        from sumy.summarizers.lsa import LsaSummarizer

        try:
            # Read the intro_paragraph from the file
            intro_paragraph = read_intro_paragraph_from_file()

            print("Intro Paragraph Before Summarization:")
            print(intro_paragraph)  # Debugging line

            if intro_paragraph:
                # Perform summarization on the intro_paragraph
                parser = PlaintextParser.from_string(intro_paragraph, Tokenizer("english"))
                summarizer = LsaSummarizer()
                intro_summary = summarizer(parser.document, sentences_count=2)  # Summarize the paragraph to 2 sentences

                print("Summary:")
                print(intro_summary)  # Debugging line

                # Check if there are sentences in the summary
                if len(intro_summary) > 0:
                    intro = ""
                    for sentence in intro_summary:
                        intro += str(sentence)
                    Speak(intro)
                else:
                    Speak("I couldn't generate a summary from the stored content.")
                # Clear the saved intro_paragraph from the file
                clear_file_content("Features\wikistore.md")
            else:
                Speak("I couldn't find the information you requested.")
        except Exception as e:
            print(f"An error occurred while summarizing: {str(e)}")
            Speak("An error occurred while summarizing.")



