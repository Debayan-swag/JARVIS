import webbrowser , os , json
from google import genai 

client = genai.Client(api_key="YOUR - GEMINI - KEY")
# loads the memory of the jarvis from json file we have created
try:
    if os.path.exists("jarvis_memory.json"):
        with open("jarvis_memory.json", "r") as f:
            conversation_text = json.load(f)
except Exception as e: # exception handeling for any empty page of json
    conversation_text = "You are Jarvis, a helpful AI assistant."
    
while True:
    user_input = input("\nUser : ")
    
    if user_input.upper() in ["QUIT" , "EXIT" , "STOP"] :
        print ("Jarvis : GoodBye, have a Great Day .")
        break
    # list of servers the user can open directly through command
    servers = [
      "GOOGLE", "YOUTUBE", "FACEBOOK", "INSTAGRAM", "LINKEDIN", "TWITTER","REDDIT", "KAGGLE", "GITHUB", "STACKOVERFLOW", "QUORA", "AMAZON","FLIPKART", "NETFLIX", "SPOTIFY", "APPLE", "MICROSOFT", "IBM","ORACLE", "OPENAI", "TWITCH", "STEAM", "DISCORD", "SLACK","NOTION", "TRELLO", "FIGMA", "CANVA", "BEHANCE", "DRIBBBLE","ADOBE", "BBC", "CNN", "NYTIMES", "REUTERS", "ZEE5","SONYLIV", "JIOCINEMA", "BOOKMYSHOW", "SWIGGY", "ZOMATO", "OLA","UBER", "IRCTC", "PAYTM", "PHONEPE", "GOOGLEPAY","CLOUDFLARE", "HEROKU", "AWS", "AZURE", "DIGITALOCEAN", "VERCEL", "NETLIFY","WIKIPEDIA", "WORDPRESS", "MOZILLA", "ARCHIVE", "NPR", "GIRLSWHOCODE","MSF", "HABITAT", "HUMANESOCIETY", "NATIONALGEOGRAPHIC","WORLDWILDLIFE","REDCROSS", "UN", "AMNESTY", "OXFAM", "WHO", "IFRC", "HRW", "EDF", "NATURE"
    ]

    key_words = user_input.upper().split(" ") # splits the text of the users in the list to see the matching keywords present in servers list or not
    url = ""
    for key in key_words:
        
        if key in ["GOOGLE", "YOUTUBE", "FACEBOOK", "INSTAGRAM", "LINKEDIN", "TWITTER","REDDIT", "KAGGLE", "GITHUB", "STACKOVERFLOW", "QUORA", "AMAZON","FLIPKART", "NETFLIX", "SPOTIFY", "APPLE", "MICROSOFT", "IBM","ORACLE", "OPENAI", "TWITCH", "STEAM", "DISCORD", "SLACK","NOTION", "TRELLO", "FIGMA", "CANVA", "BEHANCE", "DRIBBBLE","ADOBE", "BBC", "CNN", "NYTIMES", "REUTERS", "ZEE5","SONYLIV", "JIOCINEMA", "BOOKMYSHOW", "SWIGGY", "ZOMATO", "OLA","UBER", "IRCTC", "PAYTM", "PHONEPE", "GOOGLEPAY"]:
            
            url = f"https://www.{key}.com/"
            
        elif key in ["CLOUDFLARE", "HEROKU", "AWS", "AZURE", "DIGITALOCEAN", "VERCEL", "NETLIFY"]:
            
            url = f"https://www.{key}.cloud/"
            
        elif key in ["WIKIPEDIA", "WORDPRESS", "MOZILLA", "ARCHIVE", "NPR", "GIRLSWHOCODE","MSF", "HABITAT", "HUMANESOCIETY", "NATIONALGEOGRAPHIC","WORLDWILDLIFE","REDCROSS", "UN", "AMNESTY", "OXFAM", "WHO", "IFRC", "HRW", "EDF", "NATURE"]:
            
            url = f"https://www.{key}.org/"
    # for opening the required browser the user wanted , also giving exception handeling
    try:
        webbrowser.open(url)
    except Exception as e:
        print (f"Can't open the browser {url} , error is {e}") 
           
    conversation_text += f"user:{user_input}\nJARVIS:"
     
    # getting response from the model   
    response = client.models.generate_content(
        model = "gemini-2.5-flash", 
        contents = conversation_text
    ) 
    text = response.text.replace("**","").strip()
    print(f"Jarvis : {text}")
   
   # writes the memory in the json file, for the chatbot to again load and remember
    conversation_text += f" {text}"
    with open("jarvis_memory.json", "w") as f:
        json.dump(conversation_text, f)