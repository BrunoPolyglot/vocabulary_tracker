import re
from itertools import zip_longest
import binascii
import collections


#options
lang = input("|-------------------------|"
         "\n|_Type_|_CHOOSE_A_LANGUAGE:_|"
         "\n|__g___|_-German____________|"
         "\n|__s___|_-Swedish___________|"
         "\n|__i___|_-Italian___________|"
         "\n|__f___|_-French____________|"
         "\n|__a___|_-Spanish___________|"
         "\n|__p___|_-Portuguese________|"
         "\n|__e___|_-English___________|____|"
         "\n|--------------------------------|"
         "\n|______|_GENERAL_INFORMATION_____|"
         "\n|___d__|______database___________|"
         "\n|___u__|______unkown words_______|"
         "\n|--------------------------------|"
         "\n"
         "\n Please type the letter of your choice:\n")

#---------------------------------GERMAN-----------------------------------------

if lang == "g":

#displaying the options 

    option = input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"

                 "\n Please type the letter of your choice:\n")
#opening the files, make sure that the book or text file is in the same fold as the code
#   
    with open("german_vocabulary_database.txt", "r+") as vocab, open("german_unkown_words.txt", "r+") as new_vocab:

#variables

        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#opening the book or text

        filename = input("Enter name of input file: ")
        try:
            inputfile = open(filename)
            read_file = inputfile.read()
            file_list = read_file.split()
        except FileNotFoundError:             
            print("Please make sure that the file's name is correct.")
        else:

#cleanig the words before counting them

            count= collections.defaultdict(int)
            for line in file_list:
                line = line.strip().lower().replace("ã¤", "ä").replace("ãÿ", "ß").replace("ã¼", "ü").replace("ã¶", "ö").replace("ã©", "é").replace(" ", "")
                line = re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line)
                words_book.append(line)

#creating lists for the vocabulary, unkown words and the book

            read_vocab = vocab.read()
            read_new_vocab = new_vocab.read()

            vocab_split = read_vocab.split()
            new_vocab_split = read_new_vocab.split()

#counting all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#counting all the unkown words in the book

        if option == "w":
            for line in words_book:
                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)                       

#displaying all words for recognition that are neither in the vocabulary file nor in the unkown words file

        if option == "r":
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

#displaying some information about the book comparing to the database

        if option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the books:",total,
                  "\n capicity of reading:", formatted_percent, "%")
            
#-----------------------SWEDISH---------------------

if lang == "s":

#displaying the options 

    option = input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"

                 "\n Please type the letter of your choice:\n")
#opening the files, make sure that the book or text file is in the same fold as the code
#   
    with open("swedish_vocabulary_database.txt", "r+") as vocab, open("swedish_unkown_words.txt", "r+") as new_vocab:

#variables

        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#opening the book or text

        filename = input("Enter name of input file: ")
        try:
            inputfile = open(filename)
            read_file = inputfile.read()
            file_list = read_file.split()
        except FileNotFoundError:             
            print("Please make sure that the file's name is correct.")
        else:

#cleanig the words before counting them

            count= collections.defaultdict(int)
            for line in file_list:
                line = line.replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
                line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line))
                words_book.append(line)

#creating lists for the vocabulary, unkown words and the book

            read_vocab = vocab.read()
            read_new_vocab = new_vocab.read()

            vocab_split = read_vocab.split()
            new_vocab_split = read_new_vocab.split()

#counting all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#counting all the unkown words in the book

        if option == "w":
            for line in words_book:
                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)                       

#displaying all words for recognition that are neither in the vocabulary file nor in the unkown words file

        if option == "r":
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

#displaying some information about the book comparing to the database

        if option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the books:",total,
                  "\n capicity of reading:", formatted_percent, "%")
            
#---------------------ITALIAN----------------------
            
if lang == "i":

#displaying the options 

    option = input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"

                 "\n Please type the letter of your choice:\n")
#opening the files, make sure that the book or text file is in the same fold as the code
#   
    with open("italian_vocabulary_database.txt", "r+") as vocab, open("italian_unkown_words.txt", "r+") as new_vocab:

#variables

        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#opening the book or text

        filename = input("Enter name of input file: ")
        try:
            inputfile = open(filename)
            read_file = inputfile.read()
            file_list = read_file.split()
        except FileNotFoundError:             
            print("Please make sure that the file's name is correct.")
        else:

#cleanig the words before counting them

            count= collections.defaultdict(int)
            for line in file_list:
                line = line.replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
                line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line))
                words_book.append(line)

#creating lists for the vocabulary, unkown words and the book

            read_vocab = vocab.read()
            read_new_vocab = new_vocab.read()

            vocab_split = read_vocab.split()
            new_vocab_split = read_new_vocab.split()

#counting all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#counting all the unkown words in the book

        if option == "w":
            for line in words_book:
                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)                       

#displaying all words for recognition that are neither in the vocabulary file nor in the unkown words file

        if option == "r":
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

#displaying some information about the book comparing to the database

        if option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the books:",total,
                  "\n capicity of reading:", formatted_percent, "%")


#---------------------FRENCH----------------------
            
if lang == "f":

#displaying the options 

    option = input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"

                 "\n Please type the letter of your choice:\n")
#opening the files, make sure that the book or text file is in the same fold as the code
#   
    with open("french_vocabulary_database.txt", "r+") as vocab, open("french_unkown_words.txt", "r+") as new_vocab:

#variables

        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#opening the book or text

        filename = input("Enter name of input file: ")
        try:
            inputfile = open(filename)
            read_file = inputfile.read()
            file_list = read_file.split()
        except FileNotFoundError:             
            print("Please make sure that the file's name is correct.")
        else:

#cleanig the words before counting them

            count= collections.defaultdict(int)
            for line in file_list:
                line = line.replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
                line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line))
                words_book.append(line)

#creating lists for the vocabulary, unkown words and the book

            read_vocab = vocab.read()
            read_new_vocab = new_vocab.read()

            vocab_split = read_vocab.split()
            new_vocab_split = read_new_vocab.split()

#counting all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#counting all the unkown words in the book

        if option == "w":
            for line in words_book:
                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)                       

#displaying all words for recognition that are neither in the vocabulary file nor in the unkown words file

        if option == "r":
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

#displaying some information about the book comparing to the database

        if option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the books:",total,
                  "\n capicity of reading:", formatted_percent, "%")
            
#--------------------SPANISH----------------------
            
if lang == "a":  



#displaying the options 

    option = input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"

                 "\n Please type the letter of your choice:\n")
#opening the files, make sure that the book or text file is in the same fold as the code
#   
    with open("spanish_vocabulary_database.txt", "r+") as vocab, open("spanish_unkown_words.txt", "r+") as new_vocab:

#variables

        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#opening the book or text

        filename = input("Enter name of input file: ")
        try:
            inputfile = open(filename)
            read_file = inputfile.read()
            file_list = read_file.split()
        except FileNotFoundError:             
            print("Please make sure that the file's name is correct.")
        else:

#cleanig the words before counting them

            count= collections.defaultdict(int)
            for line in file_list:
                line = line.replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
                line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line))
                words_book.append(line)

#creating lists for the vocabulary, unkown words and the book

            read_vocab = vocab.read()
            read_new_vocab = new_vocab.read()

            vocab_split = read_vocab.split()
            new_vocab_split = read_new_vocab.split()

#counting all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#counting all the unkown words in the book

        if option == "w":
            for line in words_book:
                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)                       

#displaying all words for recognition that are neither in the vocabulary file nor in the unkown words file

        if option == "r":
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

#displaying some information about the book comparing to the database

        if option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the books:",total,
                  "\n capicity of reading:", formatted_percent, "%")
#-------------------------PORTUGUESE-------------------            

if lang == "p":  



#displaying the options 

    option = input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"

                 "\n Please type the letter of your choice:\n")
#opening the files, make sure that the book or text file is in the same fold as the code
#   
    with open("portuguese_vocabulary_database.txt", "r+") as vocab, open("portuguese_unkown_words.txt", "r+") as new_vocab:

#variables

        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#opening the book or text

        filename = input("Enter name of input file: ")
        try:
            inputfile = open(filename)
            read_file = inputfile.read()
            file_list = read_file.split()
        except FileNotFoundError:             
            print("Please make sure that the file's name is correct.")
        else:

#cleanig the words before counting them

            count= collections.defaultdict(int)
            for line in file_list:
                line = line.replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
                line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line))
                words_book.append(line)

#creating lists for the vocabulary, unkown words and the book

            read_vocab = vocab.read()
            read_new_vocab = new_vocab.read()

            vocab_split = read_vocab.split()
            new_vocab_split = read_new_vocab.split()

#counting all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#counting all the unkown words in the book

        if option == "w":
            for line in words_book:
                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)                       

#displaying all words for recognition that are neither in the vocabulary file nor in the unkown words file

        if option == "r":
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

#displaying some information about the book comparing to the database

        if option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the books:",total,
                  "\n capicity of reading:", formatted_percent, "%")

#---------------------ENGLISH------------------------
if lang == "e":  



#displaying the options 

    option = input("|---------------------------|"
                 "\n|_Type|_TEXT_OPTION_________|"
                 "\n|__c__|_-Count all words____|"
                 "\n|__w__|_-Count unkown words_|"
                 "\n|__r__|_-Save_known_words___|"
                 "\n|__i__|_-Information________|"
                 "\n|---------------------------|"
                 "\n"

                 "\n Please type the letter of your choice:\n")
#opening the files, make sure that the book or text file is in the same fold as the code
#   
    with open("english_vocabulary_database.txt", "r+") as vocab, open("english_unkown_words.txt", "r+") as new_vocab:

#variables

        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#opening the book or text

        filename = input("Enter name of input file: ")
        try:
            inputfile = open(filename)
            read_file = inputfile.read()
            file_list = read_file.split()
        except FileNotFoundError:             
            print("Please make sure that the file's name is correct.")
        else:

#cleanig the words before counting them

            count= collections.defaultdict(int)
            for line in file_list:
                line = line.replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
                line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line))
                words_book.append(line)

#creating lists for the vocabulary, unkown words and the book

            read_vocab = vocab.read()
            read_new_vocab = new_vocab.read()

            vocab_split = read_vocab.split()
            new_vocab_split = read_new_vocab.split()

#counting all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#counting all the unkown words in the book

        if option == "w":
            for line in words_book:
                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)                       

#displaying all words for recognition that are neither in the vocabulary file nor in the unkown words file

        if option == "r":
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

#displaying some information about the book comparing to the database

        if option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the books:",total,
                  "\n capicity of reading:", formatted_percent, "%")
