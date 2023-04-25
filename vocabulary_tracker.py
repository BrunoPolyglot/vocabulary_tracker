import re
from itertools import zip_longest
import binascii
import collections


#options
lang = input("|--------------------------------|"
         "\n|_Type_|__choose_a_language:_____|"
         "\n|__g___|_______German____________|"
         "\n|__s___|_______swedish___________|"
         "\n|__i___|_______Italian___________|"
         "\n|__f___|_______french____________|"
         "\n|__s___|_______spanish___________|"
         "\n|__p___|_______portuguese________|"
         "\n|__e___|_______english___________|"
         "\n|--------------------------------|"
         "\n|______|____INFORMATION__________|"
         "\n|___d__|______database___________|"
         "\n|___u__|______unkown words_______|"
         "\n|--------------------------------|"
         "\n"
         "\n Please type the letter of your choice:\n")

#German
if lang == "g":
    #opening the files
    option = input("|--------------------------------|"
                 "\n|_Tyoe|____Choose_one_option_____|"
                 "\n|__c__|____count all words_______|"
                 "\n|__w__|___count unkown words_____|"
                 "\n|__r__|____save known words______|"
                 "\n|--------------------------------|")

    with open("german_vocabulary_database.txt", "r+") as vocab, open("german_unkown_words.txt", "r+") as new_vocab:


        #this option show how many times each word appears in the text
        if option == "c":
            #the user has to enter a valid file name, if he does not, a message will be displayed 
            while True:
                for option in range(3):
                    #open a file
                    word_count= {}
                    filename = input("Enter name of input file: ")
                    try:
                        inputfile = open(filename)
                    except FileNotFoundError:
                        print("Please type a valid file's name.")
                else:
                    print("please checkout the name of your file again or make sure that the file is in the same directory of the code and try again later.")
                break




            #cleaning the words before counting them
                read_file = inputfile.read()
                file_list = read_file.split()
                for line in file_list:
                    line = line.strip().lower().replace("ã¤", "ä").replace("ãÿ", "ß").replace("ã¼", "ü").replace("ã¶", "ö").replace("ã©", "é").replace(" ", "")
                    line = re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line)
                    if line in word_count:
                        word_count[line] += 1
                    else:
                        word_count[line] = 1
                sorted_word_count = sorted(word_count.items(),key=lambda x: x[1],reverse=True)



        if option == "w":
            count= collections.defaultdict(int)
            read_vocab = vocab.read()
            vocab_split = read_vocab.split()


                #new words
            read_new_vocab = new_vocab.read()
            new_vocab_split = read_new_vocab.split()


                #open a file

            filename = input("Enter name of input file: ")
            inputfile = open(filename)


            read_file = inputfile.read()
            file_list = read_file.split()
            for line in file_list:
                line = line.strip().lower().replace("ã¤", "ä").replace("ãÿ", "ß").replace("ã¼", "ü").replace("ã¶", "ö").replace("ã©", "é")
                line = re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line)

                if line not in vocab_split:
                    count[line] += 1
            sorted_word_count = sorted(count.items(),key=lambda x: x[1],reverse=False)


            print(sorted_word_count)         



        if option == "r":
            
                #lists
                clean_list = list()
                word_list = list()
                words = list()
                newone =list()
                d = dict()
                total = 0
                new = 0
                known = 0
                data = 0
                #spliting files
                #vocab
                read_vocab = vocab.read()
                vocab_split = read_vocab.split()


                #new words
                read_new_vocab = new_vocab.read()
                new_vocab_split = read_new_vocab.split()


                #open a fileg


                filename = input("Enter name of input file: ")
                inputfile = open(filename)


                read_file = inputfile.read()
                file_list = read_file.split()

                #clean file
                for i in range(len(file_list)):
                    line = file_list[i].strip().lower().replace("ã¤", "ä").replace("ãÿ", "ß").replace("ã¼", "ü").replace("ã¶", "ö").replace("ã©", "é")
                    line = re.sub('[^A-Za-zåäöüéÅÄÖß]', '', line)
                    file_list[i] = line
                #count words
                    if line not in words:
                        total += 1
                        words.append(line)
                        if line in vocab_split:
                            known += 1
                        else:
                            new += 1
                            newone.append(line)

                #count words in database
                data = len(vocab_split)

                print("\nnew words: ",new, "\nknown words: ",known, "\ntotal of words: ",total)



                chunks = zip_longest(*[iter(newone)] * 20)

                for chunk in chunks:
                    print(chunk)
                    num_list = new - 20
                    rec = input("type the words that you know from the list: ")
                    rec_split = rec.split()

                    for palabra in chunk:
                        if palabra == None:
                            pass
                        elif palabra in rec_split:
                            if palabra not in vocab_split:
                                vocab.write(palabra + '\n')
                            else:
                                pass
                        else:
                            new_vocab.write(palabra + '\n')
                    cont = input("do you want to continue?(y/n")
                    if cont == 'y':
                        continue
                    else:
                        break

        
            
        
            

#swedish

if lang == "s":

#opening the files
    with open("swedish_vocabulary_database.txt", "r+") as vocab,open("swedish_unkown-words.txt", "r+") as new_vocab:

        #lists
        clean_list = list()
        word_list = list()
        words = list()
        newone =list()
        d = dict()
        total = 0
        new = 0
        known = 0
        data = 0
        #spliting files
        #vocab
        read_vocab = vocab.read()
        vocab_split = read_vocab.split()


        #new words
        read_new_vocab = new_vocab.read()
        new_vocab_split = read_new_vocab.split()


        #open a file


        filename = input("Enter name of input file: ")
        inputfile = open(filename)


        read_file = inputfile.read()
        file_list = read_file.split()

        #clean file
        for line in file_list:
            line = line.strip()
            line = line.lower()
            line = line.replace("ã¥", "å").replace("ã¤", "ä").replace("ã¶", "ö")
        #      line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', word))

        #count words
            if line not in words:
                total = total +1
                words.append(line)
                if line in vocab_split:
                    known = known + 1
                elif line not in vocab_split:
                    new = new + 1
                    newone.append(line)
            else:
                continue

        #count words in database
        for line in vocab_split:
            data = data +1


        print("\nnew words: ",new, "\nknown words: ",known, "\ntotal of words: ",total)



        chunks = zip_longest(*[iter(newone)] * 20)



        for chunk in chunks:
            print(chunk)
            num_list = new - 20
            rec = input("type the words that you know from the list: ")
            rec_split = rec.split()

            for palabra in chunk:
                if palabra == None:
                    pass
                elif palabra in rec_split:
                    if palabra not in vocab_split:
                        vocab.write(palabra + '\n')
                    else:
                        pass
                else:
                    new_vocab.write(palabra + '\n')

#italian
if lang == "i":
    vocab = open("italian_vocabulary_database.txt", "r+")
    new_vocab = open("italian_unkown-words.txt", "r+")

    #lists
    clean_list = list()
    word_list = list()
    words = list()
    newone =list()
    d = dict()
    total = 0
    new = 0
    known = 0
    data = 0
    #spliting files
    #vocab
    read_vocab = vocab.read()
    vocab_split = read_vocab.split()


    #new words
    read_new_vocab = new_vocab.read()
    new_vocab_split = read_new_vocab.split()


    #open a file



    filename = input("Enter name of input file: ")
    inputfile = open(filename)


    read_file = inputfile.read()
    file_list = read_file.split()

    #clean file
    for line in file_list:
        line = line.strip()
        line = line.lower()
        word = line.replace("Ã¥", "å").replace("Ã¤", "ä").replace("Ã¶", "ö")
        line = (re.sub('[^A-Za-zåäöüéßàèìò]', '', word))

    #count words
        if line not in words:
            total = total +1
            words.append(line)
            if line in vocab_split:
                known = known + 1
            elif line not in vocab_split:
                new = new + 1
                newone.append(line)
        else:
            continue

    #count words in database
    for line in vocab_split:
        data = data +1


    print("\nnew words: ",new, "\nknown words: ",known, "\ntotal of words: ",total)



    chunks = zip_longest(*[iter(newone)] * 20)



    for chunk in chunks:
        print(chunk)
        num_list = new - 20
        rec = input("type the words that you know from the list: ")
        rec_split = rec.split()

        for palabra in chunk:
            if palabra == None:
                pass
            elif palabra in rec_split:
                if palabra not in vocab_split:
                    vocab.write(palabra + '\n')
                else:
                    pass
            else:
                new_vocab.write(palabra + '\n')


    vocab.close()
    new_vocab.close()

#vietnamese
if lang == "v":
    # opening the files

    vocab = open("vietnamese_vocabulary_database.txt", "r+")
    new_vocab = open("vietnamese_unkown-words.txt", "r+")

    # lists
    clean_list = list()
    word_list = list()
    words = list()
    newone = list()
    d = dict()
    total = 0
    new = 0
    known = 0
    data = 0
    # spliting files
    # vocab
    read_vocab = vocab.read()
    vocab_split = read_vocab.split()

    # new words
    read_new_vocab = new_vocab.read()
    new_vocab_split = read_new_vocab.split()

    # open a file

    filename = input("Enter name of input file: ")
    inputfile = open(filename)

    read_file = inputfile.read()
    file_list = read_file.split()

    # clean file
    for line in file_list:
        line = line.strip()
        line = line.lower()
        word = line.replace("Ã¥", "å").replace("Ã¤", "ä").replace("Ã¶", "ö")
        line = (re.sub('[^A-Za-zåäöüéÅÄÖß]', '', word))

        # count words
        if line not in words:
            total = total + 1
            words.append(line)
            if line in vocab_split:
                known = known + 1
            elif line not in vocab_split:
                new = new + 1
                newone.append(line)
        else:
            continue

    # count words in database
    for line in vocab_split:
        data = data + 1

    print("\nnew words: ", new, "\nknown words: ", known, "\ntotal of words: ", total)

    chunks = zip_longest(*[iter(newone)] * 20)

    for chunk in chunks:
        print(chunk)
        num_list = new - 20
        rec = input("type the words that you know from the list: ")
        rec_split = rec.split()

        for palabra in chunk:
            if palabra == None:
                pass
            elif palabra in rec_split:
                if palabra not in vocab_split:
                    vocab.write(palabra + '\n')
                else:
                    pass
            else:
                new_vocab.write(palabra + '\n')

    vocab.close()
    new_vocab.close()


if lang == "d":
    german_vocab = open("german_vocabulary_database.txt","r+")
    swedish_vocab = open("swedish_vocabulary_database.txt","r+")
    italin_vocab = open("italian_vocabulary_database.txt", "r+")
    viet_vocab = open("vietnamese_vocabulary_database.txt","r+")

    #variables
    ger = 0
    swe = 0
    it = 0
    vie = 0
    read_german = german_vocab.read()
    german_split = read_german.split()
    read_swedish = swedish_vocab.read()
    swedish_split = read_swedish.split()
    read_italian = italin_vocab.read()
    italian_split = read_italian.split()
    read_viet = viet_vocab.read()
    viet_split = read_viet.split()


    for german in german_split:
        ger = ger + 1
    for swedish in swedish_split:
        swe = swe + 1
    for italian in italian_split:
        it = it + 1
    for viet in viet_split:
        vie = vie + 1



    print("german database:", ger,
          "\nswedish database:",swe,
          "\nvietnamese database:",vie,
          "\nitalian database:",it)

    german_vocab.close()
    swedish_vocab.close()
    italin_vocab.close()
    viet_vocab.close()
