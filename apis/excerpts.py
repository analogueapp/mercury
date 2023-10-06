import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

def get_excerpt(work, creatorList):  
    prompt_text = (f"Generate a one sentence excerpt of {work}, by {', '.join(creatorList)}.")
    completion = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=prompt_text, max_tokens=3000, temperature=0.6, n=1)       
            
    excerpt = completion.choices[0].text.strip().strip('"')
     
    if excerpt == "Unknown":
        return None
    else:
        return excerpt

## For testing purposes
# if __name__ == "__main__":
#     get_excerpt("Boojababa", ["Clint Foreskin"])