# import requests
# from bs4 import BeautifulSoup
# from googlesearch import search
# import re

# def get_google_search_results(query):
#     search_results = list(search(query, num=1, stop=1, pause=2))
#     return search_results

# def extract_answer_from_google(result_url):
#     response = requests.get(result_url)
#     response.raise_for_status()

#     soup = BeautifulSoup(response.text, "html.parser")

#     # Find the "People also ask" section (modify this based on actual HTML structure)
#     people_also_ask_section = soup.find("div", class_="g")

#     if people_also_ask_section:
#         # Extract the question
#         question = people_also_ask_section.get_text(strip=True)

#         # Extract the answer (modify this based on actual HTML structure)
#         answer_element = people_also_ask_section.find("span", class_="aCOpRe")
#         if answer_element:
#             answer = answer_element.get_text()
#             return question, answer

#     return None, None

# # Main function
# def get_google_answer(query):
#     search_results = get_google_search_results(query)

#     if search_results:
#         result_url = search_results[0]
#         question, answer = extract_answer_from_google(result_url)

#         if question and answer:
#             print("Question:", question)
#             print("Answer:", answer)
#         else:
#             print("No relevant answer found in 'People also ask' section.")

# # Example query
# query = "what is the capital of India"
# get_google_answer(query)


# notes-----------------------------------------------------------------
# wikipedia
    # if tag == "wikipedia":
    #     import bs4
    #     import requests
    #     import wikipediaapi
    #     response = requests.get("https://en.wikipedia.org/wiki/" + name)

    #     if response is not None:
    #         html = bs4.BeautifulSoup(response.text, 'html.parser')

    #         title = html.select("#firstHeading")[0].text
    #         paragraphs = html.select("p")
            
    #         intro_sentences = []
    #         sentence_count = 0
    #         for para in paragraphs:
    #             sentences = para.text.split('.')
    #             for sentence in sentences:
    #                 if sentence.strip() != '':
    #                     intro_sentences.append(sentence.strip())
    #                     sentence_count += 1
    #                     if sentence_count == 2:
    #                         break
    #             if sentence_count == 2:
    #                 break
            
    #         intro = '. '.join(intro_sentences)
    #         Speak(intro)


    # wikipedia in summarize way
        # if tag == "wikipedia":
        # import wikipediaapi
        # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        # wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
        # page = wiki_wiki.page(name)

        # if page.exists():
        #     intro_paragraph = page.text.split('\n')[2]  # Get the first paragraph
            
        #     from sumy.parsers.plaintext import PlaintextParser
        #     from sumy.nlp.tokenizers import Tokenizer
        #     from sumy.summarizers.lsa import LsaSummarizer
            
        #     parser = PlaintextParser.from_string(intro_paragraph, Tokenizer("english"))
        #     summarizer = LsaSummarizer()
        #     intro_summary = summarizer(parser.document, sentences_count=2)  # Summarize the paragraph to 1 sentence
            
        #     intro = ""
        #     for sentence in intro_summary:
        #         intro += str(sentence)
        #     Speak(intro)
        # else:
        #     Speak("I couldn't find the information you requested on Wikipedia.")

        # game
# import random 

# import pyautogui as pg

# import time

# animal = ('monkey','donkey','dog')
# stupid = ('stupid','dumb','idiot')
# hello = ('hello','listen','hey!!!')

# time.sleep(5)

# for i in range(50):
#     a = random.choice(animal)
#     pg.write("you are a " + a)
#     pg.press('enter')



# summary modle
# Function to save the name to a file
# def save_name_to_file(name):
#     with open("Features\\name_file.txt", "w") as file:
#         file.write(name)

# # Function to read the name from the file
# def read_name_from_file():
#     with open("Features\\name_file.txt", "r") as file:
#         name = file.read().strip()
#     return name

# def InputExecution(tag, query):
#     data = open("Brain/intents.json").read()
#     intents = json.loads(data)
#     intent = intents["intents"]
    
#     # Find the correct intent based on the given tag
#     intent_data = next(item for item in intent if item["tag"] == tag)
#     patterns = intent_data["patterns"]
    
#     name = ' '.join(query).lower()  # Convert the list of words into a single string
    
#     for pattern in patterns:
#         if pattern in name:
#             name = name.replace(pattern, "").strip()  # Remove pattern and leading/trailing spaces
#             break  # Exit loop after removing the pattern
    
#     # Save the name to the file regardless of the tag
#     save_name_to_file(name)

#     if tag == "wikipedia":
#         import bs4
#         import requests
#         import wikipediaapi
#         user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"  # Replace with a valid user agent
#         wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
#         page = wiki_wiki.page(name)

#         if page.exists():
#             intro = page.summary.split('.')[0]  # Get the first line of the summary
#             Speak(intro)
#         else:
#             Speak("I couldn't find the information you requested on Wikipedia.")
    
#     elif tag == "wikipedia2":
#         import wikipediaapi
#         user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
#         wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
#         page = wiki_wiki.page(name)

#         if page.exists():
#             intro_paragraph = page.text.split('\n')[0]
#             Speak(intro_paragraph)
#             save_name_to_file(name)  # Save the name to the file
#         else:
#             Speak("I couldn't find the information you requested on Wikipedia.")

#     # Check if the tag is "summary" or its patterns
#     elif tag == "summary":
#         from sumy.parsers.plaintext import PlaintextParser
#         from sumy.nlp.tokenizers import Tokenizer
#         from sumy.summarizers.lsa import LsaSummarizer
        
#         name = read_name_from_file()  # Read the name from the file
#         page = wiki_wiki.page(name)  # Retrieve the Wikipedia page using the saved name
        
#         if page.exists():
#             intro_paragraph = page.text.split('\n')[0]
#             parser = PlaintextParser.from_string(intro_paragraph, Tokenizer("english"))
#             summarizer = LsaSummarizer()
#             intro_summary = summarizer(parser.document, sentences_count=2)  # Summarize the paragraph to 1 sentence
            
#             intro = ""
#             for sentence in intro_summary: 
#                 intro += str(sentence)
#             Speak(intro)
#         else:
#             Speak("I couldn't find the information you requested on Wikipedia.")

#         # Clear the saved name from the file
#         with open("Features\\name_file.txt", "w") as file:
#             file.write("")

# summary function with wikipedia
# elif tag == "wikipedia2":
#         import wikipediaapi
#         user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
#         wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent=user_agent)
#         page = wiki_wiki.page(name)

#         if page.exists():
#             # Retrieve the first 3 paragraphs of the page
#             intro_paragraphs = page.text.split('\n')[:3]
#             intro_paragraph = '\n'.join(intro_paragraphs)
            
#             # Speak the intro_paragraph
#             Speak(intro_paragraph)
            
#             # Summarize the intro_paragraph
#             from sumy.parsers.plaintext import PlaintextParser
#             from sumy.nlp.tokenizers import Tokenizer
#             from sumy.summarizers.lsa import LsaSummarizer
            
#             parser = PlaintextParser.from_string(intro_paragraph, Tokenizer("english"))
#             summarizer = LsaSummarizer()
#             intro_summary = summarizer(parser.document, sentences_count=2)  # Summarize the paragraph to 2 sentences
            
#             intro = ""
#             for sentence in intro_summary: 
#                 intro += str(sentence)
            
#             # Speak the summary
#             Speak(intro)
            
#             # Save the intro_paragraph to a file for later use in the "summary" tag
#             save_intro_paragraph_to_file(intro_paragraph)
#         else:
#             Speak("I couldn't find the information you requested on Wikipedia.")



# if tag == "calculator":
#     # Load spaCy NLP model
#     nlp = spacy.load("en_core_web_sm")

#     # Process the user's question using spaCy
#     doc = nlp(name)

#     # Create a mapping of common arithmetic words to mathematical symbols
#     arithmetic_mapping = {
#         "plus": "+",
#         "add": "+",
#         "minus": "-",
#         "subtract": "-",
#         "divide": "/",
#         "division": "/",
#         "multiply": "*",
#         "multiplication": "*",
#         "times": "*",
#         "modulus": "%",
#         "remainder": "%",
#         "power": "^",
#         "to the power of": "^",
#     }

#     # Extract mathematical expressions (e.g., 1 + 1)
#     math_expression = None
#     for token in doc:
#         if token.pos_ == "NUM" or token.pos_ == "SYM":
#             if math_expression is None:
#                 math_expression = token.text
#             else:
#                 math_expression += " " + token.text

#     # Check if the question contains symbolic variables
#     if any(token.text in ['x', 'y', 'z'] for token in doc):
#         # Initialize symbolic variables for mathematical operations
#         x, y, z = sp.symbols('x y z')

#         # Initialize a list to store equations
#         equations = []

#         # Extract and process each equation from the user's input
#         for token in doc:
#             if token.text == "=":
#                 # Split the input into equations based on the equal sign (=)
#                 equation_parts = name.split("=")
#                 if len(equation_parts) == 2:
#                     left_side = equation_parts[0].strip()
#                     right_side = equation_parts[1].strip()

#                     # Define the equation using the left and right sides
#                     equation = sp.Eq(sp.sympify(left_side), sp.sympify(right_side))
#                     equations.append(equation)

#         # Attempt to solve the equations
#         try:
#             # Solve the system of equations
#             solution = sp.solve(equations, (x, y, z))  # Adjust the symbols as needed

#             # Convert the solution to a readable format
#             solution_text = ", ".join([f"{symbol} = {value}" for symbol, value in solution.items()])

#             response = f"The solution to the equations:\n\n{name}\n\nis:\n\n{solution_text}"
#         except Exception as e:
#             response = "Sorry, I couldn't solve those equations. Please check your input."
#     # Check if the question contains trigonometric functions
#     elif any(token.text in ['sin', 'cos', 'tan', 'cot', 'sec', 'cosec', 'theta'] for token in doc):
#         # This is a trigonometric question, you can handle it here
#         # Extract the user's name
#         name = doc.text.lower()

#         # Function to handle trigonometric questions
#         def handle_trigonometric_question(name):
#             # Check for specific trigonometric functions in the user's name
#             if "sin" in name:
#                 # Example: "What is the sine of 30 degrees?"
#                 degrees = extract_degrees(name)
#                 if degrees is not None:
#                     radians = math.radians(degrees)
#                     result = math.sin(radians)
#                     return f"The sine of {degrees} degrees is {result}"

#             elif "cos" in name:
#                 # Example: "What is the cosine of 45 degrees?"
#                 degrees = extract_degrees(name)
#                 if degrees is not None:
#                     radians = math.radians(degrees)
#                     result = math.cos(radians)
#                     return f"The cosine of {degrees} degrees is {result}"

#             elif "tan" in name:
#                 # Example: "What is the tangent of 60 degrees?"
#                 degrees = extract_degrees(name)
#                 if degrees is not None:
#                     radians = math.radians(degrees)
#                     result = math.tan(radians)
#                     return f"The tangent of {degrees} degrees is {result}"

#             elif "cot" in name:
#                 # Example: "What is the cot of 60 degrees?"
#                 degrees = extract_degrees(name)
#                 if degrees is not None:
#                     radians = math.radians(degrees)
#                     result = math.cot(radians)
#                     return f"The cot of {degrees} degrees is {result}"

#             elif "sec" in name:
#                 # Example: "What is the sec of 60 degrees?"
#                 degrees = extract_degrees(name)
#                 if degrees is not None:
#                     radians = math.radians(degrees)
#                     result = math.sec(radians)
#                     return f"The sec of {degrees} degrees is {result}"

#             elif "cosec" in name:
#                 # Example: "What is the cosec of 60 degrees?"
#                 degrees = extract_degrees(name)
#                 if degrees is not None:
#                     radians = math.radians(degrees)
#                     result = math.cosec(radians)
#                     return f"The cosec of {degrees} degrees is {result}"

#             # If the name does not match any trigonometric function, return None
#             return None

#         # Function to extract degrees from the user's name
#         def extract_degrees(name):
#             # Extract numeric values from the name (e.g., "30 degrees")
#             numeric_values = [int(word) for word in name.split() if word.isdigit()]

#             # Check if there is at least one numeric value
#             if numeric_values:
#                 return numeric_values[0]  # Return the first numeric value (assumed to be degrees)

#             return None

#         # Handle the trigonometric question
#         result = handle_trigonometric_question(name)
#         if result is not None:
#             Speak(result)  # Speak the result to the user
#         else:
#             Speak("I couldn't calculate the trigonometric expression. Please check your input.")

        
#     elif "log" in name:
#         # Split the user input into words
#         words = name.split()

#         # Find the base and number from the input
#         base = float(words[4])  # Assuming the number is always at position 4
#         number = float(words[-1])  # Assuming the base is always at the end

#         # Calculate the logarithm
#         result = math.log(number, base)

#         # Print or speak the result
#         print(f"The logarithm base {base} of {number} is {result}")
#     elif math_expression:
#         # If a mathematical expression is found, you can continue processing it here.
#         # For example, you can attempt to evaluate the mathematical expression and provide a response.
#         pass  # Add your code here if needed
#     else:
#         # Check if any arithmetic words are present in the question and replace them with their symbols
#         for token in doc:
#             if token.text in arithmetic_mapping:
#                 name = name.replace(token.text, arithmetic_mapping[token.text])
#         try :
#             result = eval(name)  # Evaluate the mathematical expression
#             Speak(f"The result is {result}")  # Speak the result to the user    
#         except Exception as e:
#             Speak("I couldn't calculate the mathematical expression. Please check your input.")
#         # Continue processing the question with the updated name, which now contains symbols.
#         # You can add code here to handle arithmetic expressions.

#         # Example: "What is 2 plus 2?"
#         # You can parse this expression and calculate the result.
#         # Once you have the result, you can add code to write down the steps of the solution
#         # and save them in the Markdown file along with the solution itself.

#     # For writing steps, you can create a list to store the steps and then write them to the file.

#     steps = []  # Create an empty list to store steps

#     # Add steps to the list as you calculate them
#     steps.append("Step 1: Parse the expression.")
#     steps.append("Step 2: Perform addition operation.")
#     steps.append("Step 3: Get the result, which is 4.")

#     # Join the steps into a single string with line breaks
#     steps_text = "\n".join(steps)

#     # Now, you can include the steps in the Markdown file along with the solution.

#     # ... (Code for calculating the result)
#     equation = name
#     # Attempt to evaluate the expression
#     result = sp.sympify(equation)
#     solution = sp.pretty(result, use_unicode=True)

#     # Determine the type of equation
#     equation_type = get_equation_type(result)

#     # Speak the equation type
#     def get_equation_type(expression):
#         if sp.has(expression, math.log):
#             return "Logarithmic Equation"
#         elif sp.has(expression, sp.Eq):
#             return "Algebric Equation"
#         elif sp.has(expression, math.sin) or math.has(expression, math.cos) or math.has(expression, math.tan) or math.has(expression, math.cot) or math.has(expression, math.sec) or math.has(expression, math.cosec):
#             return "Trigonometric Equation"
#         else:
#             return "Arithmetic Equation"

#     Speak(f"This is a {equation_type}.")

#     # Ask for a filename to save the solution
#     Speak("Please specify a filename to save the solution (without extension).")
#     file_name = Connect().lower()  # Replace with your voice input method

#     # Specify the directory path where files will be saved
#     base_directory = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Database\\maths"

#     # Create the full file path including the directory and .md extension
#     full_file_path = os.path.join(base_directory, f"{file_name}.md")

#     # After calculating the result, include the steps in the Markdown file
#     # Save the solution in a Markdown file
#     with open(full_file_path, "w") as md_file:
#         md_file.write(f"# {equation_type}\n\n")
#         md_file.write(f"**Mathematical Expression**: {equation}\n\n")
#         md_file.write(f"**Solution**: {result}\n\n")
#         md_file.write(f"**Steps**:\n\n{steps_text}")  # Include steps in the file

#     Speak(f"Solution saved as '{file_name}.md' in the specified location.")

        # Continue with the response, mentioning that steps are included in the file.

        # code for solving equations
# import math  # Import the math module
# import sympy as sp  # Import the SymPy library
# import os
# import re
# import spacy
# from Body.Listen import Connect 
# from Body.Speak import Speak
# import spacy

# # Load the spaCy NLP model
# nlp = spacy.load("en_core_web_sm")

# def detect_equation_type(query):
#     # Process the user's query using spaCy
#     doc = nlp(query.lower())

#     # Define keywords and operators for each equation type
#     arithmetic_operators = ['+', '-', '*', '/', '^', '%']
#     algebraic_keywords = ['x','y','z','a','b','c']
#     logarithmic_keywords = ['log', 'logarithm','and','of']
#     trigonometric_keywords = ['sin', 'cos', 'tan', 'cot', 'sec', 'cosec']

#     # Check if it's a simple arithmetic calculation
#     if all(token.text.isnumeric() or token.text in arithmetic_operators for token in doc):
#         print("Arithmetic Equation")
#         return "arithmetic"

#     # Check if it's a logarithmic equation with variables
#     elif any(keyword in doc.text for keyword in logarithmic_keywords):
#         print("Logarithmic Equation")
#         return "logarithmic"

#     # Check if it's a trigonometric equation with variables
#     elif any(keyword in doc.text for keyword in trigonometric_keywords):
#         print("Trigonometric Equation")
#         return "trigonometric"

#     # Check if it's an algebraic equation with variables
#     elif all(token.is_alpha for token in doc if token.text.isalpha()):
#         print("Algebraic Equation")
#         return "algebraic"
    

#     # Calculate probabilities for each equation type based on keyword presence
#     probability = {
#         'arithmetic': sum(1 for token in doc if token.text in arithmetic_operators) / len(arithmetic_operators),
#         'algebraic': sum(1 for token in doc if token.text in algebraic_keywords) / len(algebraic_keywords),
#         'logarithmic': sum(1 for token in doc if token.text in logarithmic_keywords) / len(logarithmic_keywords),
#         'trigonometric': sum(1 for token in doc if token.text in trigonometric_keywords) / len(trigonometric_keywords),
#     }

#     # Determine the equation type with the highest probability
#     most_likely_equation_type = max(probability, key=probability.get)
#     max_probability = probability[most_likely_equation_type]

#     # Set a threshold for probability (e.g., 0.7)
#     threshold = 0.7

#     # If the highest probability exceeds the threshold, return the equation type
#     if max_probability >= threshold:
#         return most_likely_equation_type
#     else:
#         return "unknown"  # If none of the types meet the threshold

# # Function to handle arithmetic equations
# def handle_arithmetic_equation(query):
#     try:
#         # Remove any non-mathematical words and punctuation from the query
#         query = query.replace("Calculate", "").strip()
#         query = query.replace(" ","").replace("raised to the power of", "**").replace("to the power of", "**").replace("power", "**").replace("^","**").replace("minus", "-").replace("plus", "+").replace("multiplied by", "*").replace("divided by", "/").replace("divide by","/").replace("modulus", "%").replace("remainder", "%").replace("percentage","%").replace("percent","%")
#         query = ''.join(filter(lambda x: x in '0123456789+-*/', query))

#         # Evaluate the arithmetic expression
#         equation_type = "Arithmetic Equation"
#         result = eval(query)
#         Speak(f"The result is {result}")
#         Speak("you want to save this in file?")
#         ans = Connect().lower() 
#         if ans == "yes" or ans == "ya" or ans == "yup" or ans == "yep" or ans == "yeah" or ans == "ha":
#             # Save the solution to a file
#             save_solution_to_file(query, result, "N/A", equation_type)
#         else:
#             Speak("okay sir...")
#     except Exception as e:
#         Speak("I couldn't calculate the arithmetic expression. Please check your input.")

# # Function to handle algebric equations
# def handle_algebraic_equation(query):
#     try:
#         # Standardize the input by removing extra whitespace and "solve"
#         query = query.strip().replace("solve ", "")
#         query = query.replace("equal to","=")

#         # Add "*" operator between coefficients and variables if missing
#         query = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', query)

#         # Split the equation by "=" to separate the left and right sides
#         sides = query.split("=")

#         # Check if there are exactly two sides
#         if len(sides) != 2:
#             print("Invalid input format. Please include '=' to specify the result.")
#             return

#         left_side, right_side = sp.sympify(sides[0].strip()), sp.sympify(sides[1].strip())

#         # Define symbolic variables
#         x, y, z, a, b, c = sp.symbols('x y z a b c')

#         # Create an equation with the left and right sides
#         equation = sp.Eq(left_side, right_side)

#         # Attempt to solve the equation for 'y'
#         solution = sp.solve([equation], (x, y, z, a, b, c))

#         if solution:
#             for variable, value in solution.items():
#                 # print(f"Solve for {variable}: {value}")
#                 Speak(f"Solve for {variable}: {value}")

#             # Prepare the steps text
#             steps_text = f"Step 1: Parse the equation.\n"
#             steps_text += f"Step 2: Solve the equation.\n"
#             steps_text += f"Equation: {equation}\n\n"
#             for variable, value in solution.items():
#                 steps_text += f"Solve for {variable}: {value}\n"
                
#             # Call the function to save the solution to a file
#             save_solution_to_file(query, solution, steps_text, "Algebraic Equation")

#         else:
#             print("No solution found for the given equation.")

#     except Exception as e:
#         error_message = f"An error occurred while solving the equation. error: {str(e)}"
#         print(error_message)
#     # Example usage to solve for 'y'
#     # handle_algebraic_equation("2x + 2y = 10x + 5y")

# # Function to handle logarithmic equations
# def handle_logarithmic_equation(query):
#     try:
#         # Standardize the input by removing extra whitespace and "equal to"
#         query = query.strip().replace("equal to", "=")

#         # Add "solve" to the query if it's not present
#         if not query.lower().startswith("solve "):
#             query = "solve " + query

#         # Define a regular expression pattern to match the input format
#         log_match = re.search(r'solve\s*log\s*(\d+)\s*and\s*(\d+)\s*=\s*(\w+)', query)

#         if log_match:
#             base = float(log_match.group(1))
#             number = float(log_match.group(2))
#             result = log_match.group(3)

#             # Calculate the logarithmic equation
#             if base > 0 and base != 1 and number > 0:
#                 x = round(math.log(number, base), 4)
#                 result_text = f"{result} = {x:.4f}"
#             else:
#                 result_text = "Invalid input. Base and number must be positive, and base cannot be 1."

#             # print(f"Solved: {result_text}")
#             Speak(f"Solved: {result_text}")

#             # Prepare the steps text
#             steps_text = f"Step 1: Parse the equation.\n"
#             steps_text += f"Step 2: Solve the equation.\n"
#             steps_text += f"Equation: log({base})({number}) = {result}\n\n"
#             steps_text += f"Solved: {result_text}\n"

#             # Call the function to save the solution to a file
#             # Assuming you have the `save_solution_to_file` function defined
#             save_solution_to_file(query, result_text, steps_text, "Logarithmic Equation")

#         else:
#             print("Invalid input format. Please use the format 'solve log(base) and number = result'.")

#     except Exception as e:
#         error_message = f"An error occurred while solving the equation. Error: {str(e)}"
#         print(error_message)
#     # handle_logarithmic_equation("log 3 and 24 = x")

# # Function to handle trigonometric equations
# def handle_trigonometric_equation(query):
#     try:
#         # Standardize the input by removing extra whitespace and "equal to"
#         query = query.strip().replace("equal to", "=")

#         # Add "solve" to the query if it's not present
#         if not query.lower().startswith("solve "):
#             query = "solve " + query

#         # Define a regular expression pattern to match various query formats
#         trig_match = re.search(r'(sin|cos|tan|cot|sec|cosec)\s*([a-zA-Z]+)?\s*=\s*(\d+(\.\d+)?)', query)

#         if trig_match:
#             trig_function = trig_match.group(1)
#             angle = trig_match.group(2)
#             result = float(trig_match.group(3))  # Convert result to a float

#             # Automatically add brackets around the variable if it's not empty
#             if angle:
#                 angle = f"({angle})"

#             # Handle the trigonometric equation here
#             equation = f"{trig_function}{'' if angle is None else angle} = {result}"

#             # Solve the equation symbolically
#             x = sp.symbols('x')
#             symbolic_eq = sp.Eq(sp.sin(x), result)  # Change 'sin' to the appropriate trigonometric function
#             solutions = sp.solve(symbolic_eq, x)

#             # Check if there are solutions
#             if solutions:
#                 result_text = f"Trigonometric equation: {equation}\nSolutions for {angle if angle else 'x'}:"
#                 for solution in solutions:
#                     result_text += f"\n{angle if angle else 'x'} = {solution.evalf()}"
#             else:
#                 result_text = f"Trigonometric equation: {equation}\nNo solutions found."

#             # print(f"Solved: {result_text}")
#             Speak(f"Solved: {result_text}")

#             # Prepare the steps text
#             steps_text = f"Step 1: Parse the equation.\n"
#             steps_text += f"Step 2: Solve the equation symbolically.\n"
#             steps_text += f"Equation: {equation}\n\n"
#             steps_text += f"Solved: {result_text}\n"

#             # Call the function to save the solution to a file
#             # Assuming you have the `save_solution_to_file` function defined
#             save_solution_to_file(query, result_text, steps_text, "Trigonometric Equation")

#         else:
#             print("Invalid input format. Please use the format 'solve trig_function(variable) = result'.")

#     except Exception as e:
#         error_message = f"An error occurred while solving the equation. Error: {str(e)}"
#         print(error_message)
#     # handle_trigonometric_equation("sin x equal to 0.5")

# # Function to generate solution and steps
# def generate_solution_and_steps(equation):
#     steps = []  # Create an empty list to store steps

#     # Add steps to the list as you calculate them
#     steps.append("Step 1: Parse the expression.")
#     steps.append("Step 2: Perform the necessary operations.")
#     steps.append("Step 3: Get the result.")

#     # Join the steps into a single string with line breaks
#     steps_text = "\n".join(steps)

#     # Attempt to evaluate the expression based on its type
#     result = None
#     if "arithmetic" in equation:
#         result = solve_arithmetic_equation(equation)
#     elif "algebraic" in equation:
#         result = solve_algebraic_equation(equation)
#     elif "logarithmic" in equation:
#         result = solve_logarithmic_equation(equation)
#     elif "trigonometric" in equation:
#         result = solve_trigonometric_equation(equation)

#     return result, steps_text

# # Function to save solution and steps in a Markdown file
# def save_solution_to_file(equation, result, steps_text, equation_type):
#     # Specify the directory path where files will be saved
#     base_directory = "C:\\Users\\qures\\OneDrive\\Desktop\\khizer\\AI3\\Database\\maths"

#     # Ask for a filename to save the solution
#     Speak("Please specify a filename to save the solution (without extension).")
#     file_name = Connect().lower()  # Replace with your voice input method

#     # Create the full file path including the directory and .md extension
#     full_file_path = os.path.join(base_directory, f"{file_name}.md")

#     # Save the solution in a Markdown file
#     with open(full_file_path, "w") as md_file:
#         md_file.write(f"# {equation_type}\n\n")
#         md_file.write(f"**Mathematical Expression**: {equation}\n\n")
#         md_file.write(f"**Solution**: {result}\n\n")
#         md_file.write(f"**Steps**:\n\n{steps_text}")  # Include steps in the file

#     Speak(f"Solution saved as '{file_name}.md' in the specified location.")

# # Main function for the calculator
# def main_calculator():
#     query = Connect().lower() # Getting user input by speaking to the microphone
#     # query = input("Enter your query: ")
#     # Detect the type of mathematical equation
#     equation_type = detect_equation_type(query)

#     # Set a threshold for probability (e.g., 0.7)
#     threshold = 0.7

#     # Route the query to the appropriate handler based on the detected equation type and probability
#     if equation_type == "arithmetic":
#         handle_arithmetic_equation(query)
#     elif equation_type == "algebraic":
#         handle_algebraic_equation(query)
#     elif equation_type == "logarithmic":
#         handle_logarithmic_equation(query)
#     elif equation_type == "trigonometric":
#         handle_trigonometric_equation(query)
#     else:
#         Speak("I couldn't determine the type of mathematical equation. Please check your input.")

# # Call the main calculator function
# main_calculator()


# # Call the modified handle_algebraic_equation function
# handle_algebraic_equation("solve 2*x + 2*y = 10")

# import tkinter as tk
# from tkinter.font import Font
# from PIL import Image, ImageTk, ImageDraw
# from tkinter import PhotoImage

# # Gui.py

# def start_gui():

#     # Create the main window
#     root = tk.Tk()

#     # Remove window decorations
#     root.overrideredirect(True)

#     # Get screen dimensions
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     # Set the window size to occupy the full screen
#     root.geometry(f"{screen_width}x{screen_height}")

#     # Set the background color to black
#     # root.configure(bg="#000000")
#     # Load your background image
#     file_path = "Database\\background.png"
#     background_image = tk.PhotoImage(file=file_path)

#     # Create a canvas to draw the circles and concentric borders
#     canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="#000000", highlightthickness=0)
#     canvas.pack()

#     # Display the background image
#     canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

#     # Calculate the scaling factor based on the original coordinates
#     original_width = 350 - 50
#     original_height = 350 - 50
#     desired_width = 315 - 85
#     desired_height = 315 - 85

#     width_scale = desired_width / original_width
#     height_scale = desired_height / original_height

#     # Calculate the coordinates to center the circles
#     center_x = screen_width // 2
#     center_y = screen_height // 2

#     big_circle_radius = (original_width / 2)
#     small_circle_radius = (desired_width / 2)

#     # Define the shades for big and small circles
#     shade_colors_big = ["#20ab49", "#22b14c", "#23b84f", "#24bf52", "#26c655"]
#     shade_colors_small = ["#09f36b","#36f787", "#65f9a3", "#94fabf", "#c4fcdb"]

#     # Function to create concentric borders
#     def create_concentric_borders(x, y, inner_radius, outer_radius, outline_colors, border_width):
#         for i, color in enumerate(outline_colors):
#             canvas.create_oval(
#                 x - outer_radius - i * border_width,
#                 y - outer_radius - i * border_width,
#                 x + outer_radius + i * border_width,
#                 y + outer_radius + i * border_width,
#                 outline=color,
#                 width=border_width
#             )
#             canvas.create_oval(
#                 x - inner_radius + i * border_width,
#                 y - inner_radius + i * border_width,
#                 x + inner_radius - i * border_width,
#                 y + inner_radius - i * border_width,
#                 outline=color,
#                 width=border_width
#             )

#     # Create concentric borders for the big circle
#     create_concentric_borders(center_x, center_y, big_circle_radius - 1, big_circle_radius, shade_colors_big, 1)

#     # Create concentric borders for the small circle
#     create_concentric_borders(center_x, center_y, small_circle_radius - 1, small_circle_radius, shade_colors_small, 2)

#     # Draw the bigger circle with neon-like color
#     canvas.create_oval(
#         center_x - big_circle_radius,
#         center_y - big_circle_radius,
#         center_x + big_circle_radius,
#         center_y + big_circle_radius,
#         outline="#22B14C",
#         width=10,
#         fill=""
#     )

#     # Draw the smaller circle with neon-like color
#     canvas.create_oval(
#         center_x - small_circle_radius,
#         center_y - small_circle_radius,
#         center_x + small_circle_radius,
#         center_y + small_circle_radius,
#         outline="#7DFAB1",
#         width=10,
#         fill=""
#     )


#     # Write "BUDDY" in the center with Orbitron font
#     canvas.create_text(center_x, center_y, text="BUDDY", font=("Orbitron", 30), fill="#FFFFFF")


#     # Main loop to display the GUI
#     root.mainloop()

# start_gui()

# # big_circle_coords = (50, 50, 350, 350)  # (x1, y1, x2, y2)
# # small_circle_coords = (85, 85, 315, 315)  # (x1, y1, x2, y2)

# import tkinter as tk
# from tkinter.font import Font
# from PIL import Image, ImageTk, ImageDraw
# from tkinter import PhotoImage
# import time

# # Create the main window
# root = tk.Tk()

# # Remove window decorations
# root.overrideredirect(True)

# # Get screen dimensions
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# # Set the window size to occupy the full screen
# root.geometry(f"{screen_width}x{screen_height}")

# # Set the background color to black
# # root.configure(bg="#000000")
# # Load your background image
# file_path = "Database\\background.png"
# background_image = tk.PhotoImage(file=file_path)

# # Create a canvas to draw the circles and concentric borders
# canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="#000000", highlightthickness=0)
# canvas.pack()

# # Display the background image
# canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# # Calculate the scaling factor based on the original coordinates
# original_width = 350 - 50
# original_height = 350 - 50
# desired_width = 315 - 85
# desired_height = 315 - 85

# width_scale = desired_width / original_width
# height_scale = desired_height / original_height

# # Calculate the coordinates to center the circles
# center_x = screen_width // 2
# center_y = screen_height // 2

# big_circle_radius = (original_width / 2)
# small_circle_radius = (desired_width / 2)

# # Define the shades for big and small circles
# shade_colors_big = ["#20ab49", "#22b14c", "#23b84f", "#24bf52", "#26c655"]
# shade_colors_small = ["#09f36b", "#36f787", "#65f9a3", "#94fabf", "#c4fcdb"]

# # Function to create concentric borders
# def create_concentric_borders(x, y, inner_radius, outer_radius, outline_colors, border_width):
#     for i, color in enumerate(outline_colors):
#         canvas.create_oval(
#             x - outer_radius - i * border_width,
#             y - outer_radius - i * border_width,
#             x + outer_radius + i * border_width,
#             y + outer_radius + i * border_width,
#             outline=color,
#             width=border_width
#         )
#         canvas.create_oval(
#             x - inner_radius + i * border_width,
#             y - inner_radius + i * border_width,
#             x + inner_radius - i * border_width,
#             y + inner_radius - i * border_width,
#             outline=color,
#             width=border_width
#         )

# # Create concentric borders for the big circle
# create_concentric_borders(center_x, center_y, big_circle_radius - 1, big_circle_radius, shade_colors_big, 1)

# # Create concentric borders for the small circle
# create_concentric_borders(center_x, center_y, small_circle_radius - 1, small_circle_radius, shade_colors_small, 2)

# # Initialize animation variables
# animation_running = False
# animation_direction = 1
# animation_speed = 2

# # Create empty lists to store the shaded circle objects
# shaded_big_circles = []
# shaded_small_circles = []

# # Define animation function
# def animate_circles():
#     global big_circle_radius, small_circle_radius, animation_direction, animation_speed

#     if animation_running:
#         big_circle_radius += animation_direction * animation_speed
#         small_circle_radius -= animation_direction * animation_speed

#         # Check if the animation should reverse
#         if big_circle_radius >= (original_width / 2):
#             animation_direction = -1
#         elif big_circle_radius <= (desired_width / 2):
#             animation_direction = 1

#         # Update the circle sizes
#         canvas.coords(big_circle, center_x - big_circle_radius, center_y - big_circle_radius,
#                       center_x + big_circle_radius, center_y + big_circle_radius)
#         canvas.coords(small_circle, center_x - small_circle_radius, center_y - small_circle_radius,
#                       center_x + small_circle_radius, center_y + small_circle_radius)

#         # Update the shaded circle sizes and positions
#         for i, shaded_big_circle in enumerate(shaded_big_circles):
#             canvas.coords(shaded_big_circle, center_x - big_circle_radius - i * 15,
#                           center_y - big_circle_radius - i * 15,
#                           center_x + big_circle_radius + i * 15,
#                           center_y + big_circle_radius + i * 15)
#         for i, shaded_small_circle in enumerate(shaded_small_circles):
#             canvas.coords(shaded_small_circle, center_x - small_circle_radius - i * 15,
#                           center_y - small_circle_radius - i * 15,
#                           center_x + small_circle_radius + i * 15,
#                           center_y + small_circle_radius + i * 15)

#         # Schedule the next animation frame
#         root.after(10, animate_circles)

# # Create bigger circle with neon-like color
# big_circle = canvas.create_oval(
#     center_x - big_circle_radius,
#     center_y - big_circle_radius,
#     center_x + big_circle_radius,
#     center_y + big_circle_radius,
#     outline="#22B14C",
#     width=10,
#     fill=""
# )

# # Create smaller circle with neon-like color
# small_circle = canvas.create_oval(
#     center_x - small_circle_radius,
#     center_y - small_circle_radius,
#     center_x + small_circle_radius,
#     center_y + small_circle_radius,
#     outline="#7DFAB1",
#     width=10,
#     fill=""
# )

# # Create shaded big circles
# for _ in range(5):
#     shaded_big_circle = canvas.create_oval(0, 0, 0, 0, outline="#20ab49", width=10, fill="#000000")
#     shaded_big_circles.append(shaded_big_circle)

# # Create shaded small circles
# for _ in range(5):
#     shaded_small_circle = canvas.create_oval(0, 0, 0, 0, outline="#09f36b", width=10, fill="#000000")
#     shaded_small_circles.append(shaded_small_circle)

# # Write "BUDDY" in the center with Orbitron font
# font_color = "#FFFFFF"
# font_size = 30
# font_id = canvas.create_text(center_x, center_y, text="BUDDY", font=("Orbitron", font_size), fill=font_color)

# # Function to start and stop the animation
# def toggle_animation():
#     global animation_running
#     if not animation_running:
#         animation_running = True
#         animate_circles()
#         canvas.itemconfig(font_id, fill="#8ed8f4")  # Change font color to #8ed8f4 when animation starts
        
#         # Hide the shaded circles when animation starts
#         for shaded_big_circle in shaded_big_circles:
#             canvas.itemconfig(shaded_big_circle, state=tk.HIDDEN)
#         for shaded_small_circle in shaded_small_circles:
#             canvas.itemconfig(shaded_small_circle, state=tk.HIDDEN)
#     else:
#         animation_running = False
#         canvas.itemconfig(font_id, fill=font_color)  # Change font color back to white when animation stops
        
#         # Show the shaded circles when animation stops
#         for shaded_big_circle in shaded_big_circles:
#             canvas.itemconfig(shaded_big_circle, state=tk.NORMAL)
#         for shaded_small_circle in shaded_small_circles:
#             canvas.itemconfig(shaded_small_circle, state=tk.NORMAL)

# def start_gui():
#     # Bind the animation toggle function to a keypress event (e.g., spacebar)
#     root.bind("<space>", lambda event: toggle_animation())

#     # Main loop to display the GUI
#     root.mainloop()

# if __name__ == "__main__":
#      start_gui()


# whatsappp---------------
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import os
# from time import sleep
# import pathlib
# from urllib.parse import quote
# from selenium.webdriver.common.keys import Keys

# # Initialize the WebDriver service and options
# service = Service(executable_path=r'Database\\win32\\chromedriver.exe')
# options = Options()
# # options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# scriptDirectory = pathlib.Path().absolute()

# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument("--profile-directory=Default")
# options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
# os.system("")
# os.environ["WDM_LOG_LEVEL"] = "0"
# PathofDriver = "DataBase\\win32\\chromedriver.exe"

# # Initialize the WebDriver
# driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()
# driver.get("https://web.whatsapp.com/")
# # sleep(30)
# Speak("Initializing The Whatsapp Software.")

# # List of contacts and phone numbers
# ListWeb = {
#     'dhruv': "+917011024588",
#     'Source': "+91 82917 88306",
#     "pote": '+91'
# }

# def WhatsappSender(Name):
#     Speak(f"Preparing To Send a Message To {Name}")
#     Speak("What's The Message By The Way?")
#     Message = "check"
#     Number = ListWeb[Name]
#     LinkWeb = f'https://web.whatsapp.com/send?phone={Number}&text={Message}'
#     driver.get(LinkWeb)
#     sleep(20)
#     try:
#         driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
#         sleep(10)
#         Speak("Message Sent")
#     except:
#         print("Invalid Number")

# WhatsappSender("Source")

# import webbrowser
#         # Open the default web browser (usually Google Chrome)
#         # webbrowser.open("https://web.google.com/")
# import pywhatkit as kit
# import datetime
# now = datetime.datetime.now()
# hour = now.hour
# minute = now.minute + 1  
# Speak("sending message please wait")
# kit.sendwhatmsg("+9191368 48986", "This is a test message", hour, minute)
# time.sleep(10)
# Speak("Message sent")