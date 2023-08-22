# import the following modules
import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
  
  
def get_fun_fact(_):
    
    # Clear the screen
    clear()
  
    # some html and a clown 
    put_html("<p align=""left""><h1><img src=""https://www.popsci.com/uploads/2023/05/19/clown2.png"" width=""25%"">   Fun Fact Generator</h1></p>")
      
    # URL from where we will fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
      
    # Use GET request
    response = requests.request("GET", url)  
      
    # Load the request in json file
    data = json.loads(response.text)
               
    # we will need 'text' from the list, so 
    # pass 'text' in the list
    useless_fact = data['text']
               
    # Put the facts in the blue colour
    # Put the click me button
    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    put_buttons(
        [dict(label='Click me', value='outline-success', 
              color='outline-success')], onclick=get_fun_fact)  

def main():

    get_fun_fact(_)
  
# Driver Function
if __name__ == '__main__':
      
    # Put a heading "Fun Fact Generator" and a clown
    put_html("<p align=""left""><h1><img src=""https://www.popsci.com/uploads/2023/05/19/clown2.png"" width=""25%"">   Fun Fact Generator</h1></p>")

    # hold the session for long time
    # Put a Click me button
    put_buttons([dict(label='Click me', value='outline-success', color='outline-success')], onclick=get_fun_fact)  
    hold()  

    main()



