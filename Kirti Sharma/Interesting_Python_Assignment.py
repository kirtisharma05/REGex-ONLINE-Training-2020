# Ques1 : You have to scrap any website (example: Cricbuzz) to find out five top repeated words.
# a- how many times the word has been repeated.
# b- you have to plot a graph of the output.

# Solution :

import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 

import matplotlib.pyplot as plt 
  
def start(url): 
  
    # empty list to store the contents of  
    # the website fetched from our web-crawler 
    wordlist = [] 
    source_code = requests.get(url).text 
  
    # BeautifulSoup object which will 
    # ping the requested url for data 
    soup = BeautifulSoup(source_code, 'html.parser') 
  
    # Text in given web-page is stored under 
    # the <div> tags with class <entry-content> 
    for each_text in soup.findAll('div', {'class':'entry-content'}): 
        content = each_text.text 
  
        # use split() to break the sentence into  
        # words and convert them into lowercase  
        words = content.lower().split() 
          
        for each_word in words: 
            wordlist.append(each_word) 
        clean_wordlist(wordlist) 
  
# Function removes any unwanted symbols 
def clean_wordlist(wordlist): 
      
    clean_list =[] 
    for word in wordlist: 
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
          
        for i in range (0, len(symbols)): 
            word = word.replace(symbols[i], '') 
              
        if len(word) > 0: 
            clean_list.append(word) 
    create_dictionary(clean_list) 
  
# Creates a dictionary conatining each word's count and top_5 ocuuring words 
def create_dictionary(clean_list): 
    word_count = {} 
      
    for word in clean_list: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
              
      
    c = Counter(word_count)                      # Count of each word
      
    # returns the most occurring elements 
    top = c.most_common(5) 
    print('5 Most Common Words along with number of repeatitions : ')
    print(top) 
    

    # Ploting Graph

    # x-coordinates of left sides of bars 
    left = [1, 2, 3, 4, 5] 
    
    # heights of bars 
    height = []
    for i in range(5):
        height.append(top[i][1]) 
  
    # labels for bars 
    tick_label = []
    for i in range(5):
        tick_label.append(top[i][0])
  
    # plotting a bar chart 
    plt.bar(left, height, tick_label = tick_label, 
    width = 0.8, color = ['blue', 'grey']) 
  
    # naming the x-axis 
    plt.xlabel('Most Common Words') 
    # naming the y-axis 
    plt.ylabel('Number of repeatitions') 
    # plot title 
    plt.title('5 Most Common Words along with the number of repeatitions (in graph) :') 
  
    # function to show the plot 
    print(plt.show())

    
start("https://www.geeksforgeeks.org/programming-language-choose/") 



# Ques 2: You have to get input from the users and it is recommended to be in voice command and you need to do a sentimental analysis of the given input [ hint: use textblob library ].
# Ans :
import textblob as tx 
import speech_recognition as sr 
r = sr.Recognizer()
while(True):
    with sr.Microphone() as source:
        print("- Say Something -")
        audio = r.listen(source)
        print("- Time Over -")
    try:
        word = r.recognize_google(audio)
        print(word)
        a = tx.TextBlob(word)
        b = a.sentiment.polarity
        print(b)
    except:
        pass