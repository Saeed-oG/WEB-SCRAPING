import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from seaborn import color_palette
import tkinter as tk
from tkinter import messagebox,Toplevel
#Intractive window function:
def show_retry_window():
    retry_window = Toplevel()  #Creat new window
    retry_window.title("Connection Error!")
    retry_window.geometry("300x150")
    tk.Label(retry_window, text="Try again after checking the internet.", font=("Times New Roman", 12), pady=20).pack() #Error message box
    retry_choice = tk.BooleanVar(value=False)  #Variable for user choice
    #Intractive bUttons
    tk.Button(retry_window, text="Retry", command=lambda: [retry_choice.set(True), retry_window.destroy()], width=10).pack(pady=10)
    tk.Button(retry_window, text="Exit", command=lambda: [retry_choice.set(False), retry_window.destroy()], width=10).pack(pady=5)
    #Wait for user decision
    retry_window.grab_set()
    retry_window.wait_window()
    return retry_choice.get()
#Web scraping main function
def scrape_quotes():
    data = []
    url = "http://quotes.toscrape.com"
    while url:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status() #HTTP error analysis
            # print(response.text[:500]) #shows first 500 characters
            #Data extraction
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                data.append({'Quote': text, 'Author': author})
            #Finding the next page link
            next_page = soup.find('li', class_='next')
            url = "http://quotes.toscrape.com" + next_page.find('a')['href'] if next_page else None
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            if show_retry_window():
                print("Try again after checking the internet.")
                #messagebox.showerror("Connection failed!", "Try again after checking the internet.")
                continue  #Try again
            else:
                break  #Stop running if an error occurs
    if data:
        odata = pd.DataFrame(data)
        odata.to_csv('quotes_data_final.csv', index=False, encoding='utf-8-sig')
    return data
#Visualization function
def visualize_data(data):
    if data:
        odata = pd.DataFrame(data)
        #Calculating quotes for each auther:
        author_counts = odata['Author'].value_counts().head(10)
        #Drawing bar chart:
        colors = color_palette('Greens', n_colors=len(odata))
        colors = colors[::-1] # Inverse highlight colors sequence
        plt.figure(figsize=(10, 6))
        sns.barplot(x=author_counts.values, y=author_counts.index, hue=author_counts.index, palette=colors, legend=False)
        # plt.xticks(rotation=90, fontsize=8) #rotate x-axis tags
        # plt.tight_layout()
        plt.title('Top 10 Authors by Number of Quotes', fontsize=14)
        plt.xlabel('Number of Quotes', fontsize=12)
        plt.ylabel('Author', fontsize=12)
        plt.grid(True)
        plt.savefig('author_quotes.png', dpi=300)
        plt.show()
    else:
        print('No data collected!')
#Run
if __name__ == "__main__":   #If current script run directly(Not when used as a module elsewhere) then do...
    root = tk.Tk()
    root.withdraw()
    data = scrape_quotes()
    visualize_data(data)
    root.destroy()