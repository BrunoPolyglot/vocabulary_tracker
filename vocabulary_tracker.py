import re
from itertools import zip_longest
import pandas as pd
import sys 


#VARIABLES

languages = {
    "english": {"unknown_words": 0,"vocabulary_database":0},
    "french": {"unknown_words":0,"vocabulary_database":0},
    "german": {"unknown_words":0, "vocabulary_database":0},
    "italian": {"unknown_words":0,"vocabulary_database":0},
    "portuguese": {"unknown_words":0, "vocabulary_database":0},
    "spanish": {"unknown_words":0,"vocabulary_database":0},
    "swedish": {"unknown_words":0,"vocabulary_database":0},
}

count_info = {
    "words_with_repetition": {"new_words": 0, "known_words":0,"total_of_words":0, "capacity_of_reading":0},
    "words_without_repetition": {"new_words": 0, "known_words":0,"total_of_words":0, "capacity_of_reading":0},
}

file_handles = {}
count_database = {}
count = {}
word_count = {}
words_book = []
new_words = []
words_book = []
vocab_split = []
count_book = []
new_vocab_split = []
formatted_percent = 0
formatted_percent_rep = 0



     


def display():
    option =input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"
                 "\n Please type the letter of your choice:\n")
    return option

#function to open the file that will have to be in the same directory as the code

def file_input():
    filename = input("Enter name of input file: ")
    try:
        inputfile = open(filename)
        read_file = inputfile.read()
        file_list = read_file.split()
    except FileNotFoundError:             
        print("Please make sure that the file's name is correct.")
        return None
    else:

#clean the words of any language in the list 

        
        for line in file_list:
            line = line.strip().lower()
            line = re.sub(r"^.*?['`]", '', line)
            line = re.sub(r'^A-Za-zåäöüéßùàìèòàçèíóñáâãêëíîïôõúû', '', line)
            words_book.append(line)
        return words_book
    
    
#read the vocabularies 
def read_vocab(vocab, new_vocab):    
    
    vocab_split = vocab.read().split()
    new_vocab_split = new_vocab.read().split()
    return vocab_split, new_vocab_split

#count number of each word in the book 

def count_word():
    for line in words_book:
        if line in word_count:
            word_count[line] += 1
        else:
            word_count[line] = 1   
    return word_count

lang = input(
         "\n Please write one of the following language:"
         "\nGERMAN"
         "\nSWEDISH"
         "\nITALIAN"
         "\nFRENCH"
         "\nSPANISH"
         "\nPORTUGUESE"
         "\nENGLISH"
         "\nDATABASE\n").lower()

#open all the files to give how many words there are in order to compare vocabularies        
#  
if lang == 'database':
    
    for lang, files in languages.items():
        for file_type in files:
            file_path = f'data/{lang}_{file_type}.txt'
            with open(file_path, "r+") as file:
                count = len(file.readlines())
                if files == "unknown_words":
                    languages[lang]['unknown_words'] += count
                else:
                    languages[lang]['vocabulary_database'] += count
    df = pd.DataFrame(languages)
    print("see below the information about your vocabulary:\n", df)
                
elif lang not in languages:
    print("Please write a valid language")
else:
    with open(f"data/{lang}_vocabulary_database.txt", "r+") as vocab, open(f"data/{lang}_unknown_words.txt", "r+") as new_vocab:
        
#----------------------------------Languages-----------------------------------------
        option = display()
        
#return the data from the function file_input and create a list 

        words_book = file_input()      
        if words_book is None:
            sys.exit()
        else:
            vocab_split, new_vocab_split = read_vocab(vocab, new_vocab)

#count all the words from the book 

        if option == "c":
            count_word()
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#count all the unkown words in the book

        elif option == "w":
            for line in words_book:
                if line not in vocab_split:
                    if line in count:
                        count[line] += 1
                    else:
                        count[line] = 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)  

#display all words for recognition that are neither in the vocabulary file nor in the unkown words file

        elif option == "r":
            for line in words_book:
                if line not in vocab_split and line not in new_vocab_split:
                    new_words.append(line)
            chunks = zip_longest(*[iter(new_words)] * 20)
            for chunk in chunks:                   
                print(chunk)
                rec = input("type the words that you know from the list:")
                rec_split = rec.split()
                new = input('Please type the words that you want to save the unkown words file:\n')
                new_split = new.split()
                for word in rec_split:
                    vocab.write(str(word) + '\n')
                for word in new_split:
                    new_vocab.write(str(word) + '\n')
                cont = input("do you want to continue?(y/n)").lower()
                if cont == 'n':
                    break
                else:
                    continue

#display information about the book compared to the database

        elif option == "i":
            count_book = count_word()
            for key, value in count_book.items():
                count_info['words_without_repetition']['total_of_words'] += 1
                if key in vocab_split:
                    count_info['words_without_repetition']['known_words'] += 1
                else:
                    count_info['words_without_repetition']['new_words'] += 1

            for word in words_book:
                count_info['words_with_repetition']['total_of_words'] += 1
                if word in vocab_split:
                    count_info['words_with_repetition']['known_words'] += 1
                else:
                    count_info['words_with_repetition']['new_words'] += 1

            percent = (100*count_info['words_without_repetition']['known_words'])/count_info['words_without_repetition']['total_of_words']
            formatted_percent = "{:.2f}".format(percent)
            count_info['words_without_repetition']['capacity_of_reading'] = formatted_percent
            percent_rep = (100*count_info['words_with_repetition']['known_words'])/count_info['words_with_repetition']['total_of_words']
            formatted_percent_rep = "{:.2f}".format(percent_rep)
            count_info['words_with_repetition']['capacity_of_reading'] = formatted_percent_rep
            df = pd.DataFrame(count_info)
            print(df)
