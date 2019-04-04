# alphaNews
Evaluate to what extent good or bad news impacts stock prices

To run:
Add your apikey to the key.json file
Run the packages.sh file to install all required packages

Code flow:
- UI search box takes general field search query (ie Medical Robotics)
- Query is sent to the news scanner API which gathers relevant articles
- Each article has its publish date and pertinent company extracted
- Sentiment analysis is run on each article for each company
- Stock information is retrieved for each company and a delta is found for the week after each article
- The complete object is returned to the dashboard for display