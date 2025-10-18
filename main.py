import webbrowser
from google import genai

client = genai.Client(api_key="AIzaSyCo_0_p3-CImDY4R8h0CjUNFLfHP-C0OJQ")

while True:
    user_input = input("\nUser : ")
    
    if user_input.upper() in ["QUIT" , "EXIT" , "STOP"] :
        print ("Jarvis : GoodBye, have a Great Day .")
        break
    
    servers = [
      "GOOGLE", "YOUTUBE", "FACEBOOK", "INSTAGRAM", "LINKEDIN", "TWITTER","REDDIT", "KAGGLE", "GITHUB", "STACKOVERFLOW", "QUORA", "AMAZON","FLIPKART", "NETFLIX", "SPOTIFY", "APPLE", "MICROSOFT", "IBM","ORACLE", "OPENAI", "TWITCH", "STEAM", "DISCORD", "SLACK","NOTION", "TRELLO", "FIGMA", "CANVA", "BEHANCE", "DRIBBBLE","ADOBE", "BBC", "CNN", "NYTIMES", "REUTERS", "ZEE5","SONYLIV", "JIOCINEMA", "BOOKMYSHOW", "SWIGGY", "ZOMATO", "OLA","UBER", "IRCTC", "PAYTM", "PHONEPE", "GOOGLEPAY","CLOUDFLARE", "HEROKU", "AWS", "AZURE", "DIGITALOCEAN", "VERCEL", "NETLIFY","WIKIPEDIA", "WORDPRESS", "MOZILLA", "ARCHIVE", "NPR", "GIRLSWHOCODE","MSF", "HABITAT", "HUMANESOCIETY", "NATIONALGEOGRAPHIC","WORLDWILDLIFE","REDCROSS", "UN", "AMNESTY", "OXFAM", "WHO", "IFRC", "HRW", "EDF", "NATURE"
    ]

    key_words = user_input.upper().split(" ")
    
    for key in key_words:
        
        if key in ["GOOGLE", "YOUTUBE", "FACEBOOK", "INSTAGRAM", "LINKEDIN", "TWITTER","REDDIT", "KAGGLE", "GITHUB", "STACKOVERFLOW", "QUORA", "AMAZON","FLIPKART", "NETFLIX", "SPOTIFY", "APPLE", "MICROSOFT", "IBM","ORACLE", "OPENAI", "TWITCH", "STEAM", "DISCORD", "SLACK","NOTION", "TRELLO", "FIGMA", "CANVA", "BEHANCE", "DRIBBBLE","ADOBE", "BBC", "CNN", "NYTIMES", "REUTERS", "ZEE5","SONYLIV", "JIOCINEMA", "BOOKMYSHOW", "SWIGGY", "ZOMATO", "OLA","UBER", "IRCTC", "PAYTM", "PHONEPE", "GOOGLEPAY"]:
            
            try:
                webbrowser.open(f"https://www.{key}.com/")
            except Exception as e:
                print (f"Failed to open the server, error is {e}")
            
        elif key in ["CLOUDFLARE", "HEROKU", "AWS", "AZURE", "DIGITALOCEAN", "VERCEL", "NETLIFY"]:
            
            try:
                webbrowser.open(f"https://www.{key}.cloud/")   
            except Exception as e:
                print (f"Failed to open the server, error is {e}")
            
        elif key in ["WIKIPEDIA", "WORDPRESS", "MOZILLA", "ARCHIVE", "NPR", "GIRLSWHOCODE","MSF", "HABITAT", "HUMANESOCIETY", "NATIONALGEOGRAPHIC","WORLDWILDLIFE","REDCROSS", "UN", "AMNESTY", "OXFAM", "WHO", "IFRC", "HRW", "EDF", "NATURE"]:
            
            try:
                webbrowser.open(f"https://www.{key}.org/")
            except Exception as e:
                print (f"Failed to open the server, error is {e}")
        
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=user_input
    ) 
    text = response.text.replace("**","").strip()
    print(f"Jarvis : {text}")
