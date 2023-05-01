import re
from itertools import zip_longest

#options
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

valid_languages =["german", "swedish", "italian", "french", "spanish", "portuguese", "english"]

#opnening all the files to give how many words there are in order to compare vocabularies 
#           
if lang == 'database':
    uenglish_count = 0
    ufrench_count = 0
    ugerman_count = 0
    uitalian_count = 0
    uportuguese_count = 0
    uspanish_count = 0
    uswedish_count = 0
    with open("data/english_unkown_words.txt","r+") as unkown_english, \
         open("data/english_vocabulary_database.txt","r+") as database_english, \
         open("data/french_unkown_words.txt","r+") as unkown_french, \
         open("data/french_vocabulary_database.txt", "r+") as database_french, \
         open("data/german_unkown_words.txt" , "r+") as unkown_german, \
         open("data/german_vocabulary_database.txt", "r+") as database_german, \
         open("data/italian_unkown_words.txt", "r+") as unkown_italian, \
         open("data/italian_vocabulary_database.txt","r+") as database_italian, \
         open("data/portuguese_unkown_words.txt","r+") as unkown_portuguese, \
         open("data/portuguese_vocabulary_database.txt","r+") as database_portuguese, \
         open("data/spanish_unkown_words.txt","r+") as unkown_spanish, \
         open("data/spanish_vocabulary_database.txt","r+") as database_spanish, \
         open("data/swedish_unkown_words.txt","r+") as unkown_swedish, \
         open("data/swedish_vocabulary_database.txt","r+") as database_swedish:


        unkown_english_split = unkown_english.read().split()
        unkown_french_split= unkown_french.read().split()
        unkown_german_split = unkown_german.read().split()
        unkown_italian_split = unkown_italian.read().split()
        unkown_portuguese_split = unkown_portuguese.read().split()
        unkown_spanish_split = unkown_spanish.read().split()
        unkown_swedish_split = unkown_swedish.read().split()

        for word in unkown_english_split:
            uenglish_count += 1
        for word in unkown_french_split:
            ufrench_count += 1
        for word in unkown_german_split:
            ugerman_count += 1
        for word in unkown_italian_split:
            uitalian_count += 1
        for word in unkown_portuguese_split:
            uportuguese_count += 1
        for word in unkown_spanish_split:
            uspanish_count += 1
        for word in unkown_swedish_split:
            uswedish_count += 1

        denglish_count = 0
        dfrench_count = 0
        dgerman_count = 0
        ditalian_count = 0
        dportuguese_count = 0
        dspanish_count = 0
        dswedish_count = 0

        database_english_split = database_english.read().split()
        database_french_split = database_french.read().split()
        database_german_split= database_german.read().split()
        database_italian_split = database_italian.read().split()
        database_portuguese_split = database_portuguese.read().split()
        database_spanish_split = database_spanish.read().split()
        database_swedish_split = database_swedish.read().split()

        for word in database_english_split:
            denglish_count += 1
        for word in database_french_split:
            dfrench_count += 1
        for word in database_french_split:
            dgerman_count += 1
        for word in database_italian_split:
            ditalian_count += 1
        for word in database_portuguese_split:
            dportuguese_count += 1
        for word in database_spanish_split:
            dspanish_count += 1
        for word in database_swedish_split:
            dswedish_count += 1

        


#printing how many words there are in the database and unkown words files

        print("here is the list of languages and the number of words that you know:",
              "\nENGLISH:    ",denglish_count,
              "\nFRENCH:     ",dfrench_count,
              "\nGERMAN:     ",dgerman_count,
              "\nITALIAN:    ",ditalian_count,
              "\nPORTUGUESE: ",dportuguese_count,
              "\nSPANISH:    ",dspanish_count,
              "\nSWEDISH:    ",dswedish_count,
              "\n\nhere is the list of unkown words that you saved:"
              "\nENGLISH:    ",uenglish_count,
              "\nFRENCH:     ",ufrench_count,
              "\nGERMAN:     ",ugerman_count,
              "\nITALIAN:    ",uitalian_count,
              "\nPORTUGUESE: ",uportuguese_count,
              "\nSPANISH:    ",uspanish_count,
              "\nSWEDISH:    ",uswedish_count,)

elif lang not in valid_languages:
    print("Please write a valid language")

else:
    with open("data/" + lang + "_vocabulary_database.txt", "r+") as vocab, open("data/" + lang +"_unkown_words.txt", "r+") as new_vocab:

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
            else:

#cleaning the words of any language in the list 

                words_book = []
                for line in file_list:
                    line = line.strip().lower().replace("ã¤", "ä").replace("ãÿ", "ß").replace("ã¼", "ü").replace("ã¶", "ö").replace("ã©", "é").replace(" ", "").replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
                    line = re.sub(r"^.*?['`]", '', line)
                    line = re.sub('[^A-Za-zåäöüéßùàìèòàçèíóñáâãêëíîïôõúû]', '', line)
                    words_book.append(line)
                return words_book

#reading the vocabularies 

        def read_vocab(vocab, new_vocab):    
            vocab_split = []
            new_vocab_split = []
            vocab_split = vocab.read().split()
            new_vocab_split = new_vocab.read().split()
            return vocab_split, new_vocab_split
#----------------------------------Languages-----------------------------------------

#displaying the options 

        option = display()

#variables

        count = {}
        word_count = {}
        words_book = []
        new_words = []
        total = 0
        new = 0 
        percent = 0 
        known = 0
        formatted_percent = 0

#returning the data from the function file_input and making it a list 

        words_book = list(file_input())        
        vocab_split, new_vocab_split = read_vocab(vocab, new_vocab)

#countig all the words from the book 

        if option == "c":
            for line in words_book:
                if line in word_count:
                    word_count[line] += 1
                else:
                    word_count[line] = 1
            sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)
            print(sorted_word_count)

#countig all the unkown words in the book

        elif option == "w":
            for line in words_book:
                if line not in vocab_split:
                    if line in count:
                        count[line] += 1
                    else:
                        count[line] = 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)
            print(sorted_word_count)      

#displaing all words for recognition that are neither in the vocabulary file nor in the unkown words file

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

#displaing some information about the book comparing to the database

        elif option == "i":
            for word in words_book:
                total += 1
                if word in vocab_split:
                    known += 1
                else:
                    new += 1
            percent = (100*known)/total
            formatted_percent = "{:.2f}".format(percent)
            print("the number of unknown words in the book:",new,
                  "\nthe number of words in the book:",total,
                  "\n capicity of reading:", formatted_percent, "%")