# WEB-SCRAPING
Web scraping and visualization of quote data:
This project scrapes quotes and authors from http://quotes.toscrape.com using Python and visualizes the data. 

Steps:
1.Setup: Installed Requests, BeautifulSoup, and Pandas. 
2. Connection check: Added an interactive window to manage Internet access.
3.Scraping: Extracted quotes and authors from all pages. 
4.Data Storage: Saved data in `quotes_data.csv` with UTF-8 encoding to handle special characters.
5.Visualization: Created a bar chart for the top 10 authors by quote count. 

Tools:
- Python (Requests, BeautifulSoup, Pandas, Seaborn, Matplotlib) 
- Website: http://quotes.toscrape.com 

Outputs:
- quotes_data.csv: Scraped quotes and authors. 
- author_quotes.png: Bar chart of top 10 authors. 

Files:
-WebScraping.py
-quotes_data.csv
-author_quotes.png

How to Run:
1.	Set up the environment(Install required libraries)
2.	Run the WebScraping.py code in VSCODE 

Challenges and Solutions:
-Issue: Special characters (e.g., smart quotes) appeared incorrectly in the CSV file.
-Solution: Used encoding='utf-8-sig' in to_csv method and replaced smart quotes with standard quotes.
-Issue: The colors of the chart were not attractive enough.
-Solution: The color_palette function from seaborn module was used to properly organize the colors.
-Issue: Internet connection interruptions could stop the scraping process. 
-Solution: Implemented a tkinter interactive window with "Retry" and "Exit" buttons to handle connection errors, allowing users to retry scraping or exit.
