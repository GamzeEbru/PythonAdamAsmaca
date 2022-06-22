#Gamze Ebru Altikulac 

import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    print("Dosyadan kelime listesi yükleniyor...\n")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.\n")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    string = ""
    for i in secret_word:
        if i in letters_guessed:
            string += i
        else:
            string += "_"
    return string


def get_available_letters(letters_guessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    t = ""
    for i in string:
        if i not in letters_guessed:
            t += i
    return t


def adamAsmaca(secret_word):
   print("-------ADAM ASMACA OYUNUNA HOŞGELDİN--------\n")
   print("Tahmin etmeniz gereken kelime " +
         str(len(secret_word)) + " harflidir \n")
   letters_guessed = ''
   kalanthmn = 8
   print(" ------------ \n")
   while True:
       print(str(kalanthmn) + " hakka sahipsiniz \n")
       print("Su an kullanabileceğiniz harfler : " +
             get_available_letters(letters_guessed))
       tahmin = input("Harf tahmininiz : \n")
       if tahmin in secret_word and tahmin not in letters_guessed:
           letters_guessed += tahmin
           print("Doğru tahmin : " + get_guessed_word(secret_word, letters_guessed))
       elif tahmin in letters_guessed:
           print("Zaten bu harfi denediniz! \n" +
                 get_guessed_word(secret_word, letters_guessed))
       else:
           letters_guessed += tahmin
           print("Kelimede bu harf bulunmamaktadır \n" +
                 get_guessed_word(secret_word, letters_guessed))
           kalanthmn -= 1
       

       if kalanthmn <= 0:
           print("Tahmin hakkınız bitti :( \n Doğru Kelime : a" + secret_word + ".")
           break
       if is_word_guessed(secret_word, letters_guessed):
           print("TEBRİKLER, Kelimeyi doğru tahmin ettiniz!! \n")
           break


def match_with_gaps(my_word, other_word):
    yln = my_word.replace(" ", "")
    hrfs = ""
    if len(yln) != len(other_word):
        return False
    for index in range(len(yln)):
        if yln[index] != "_":
            if yln[index] != other_word[index]:
                return False
            hrfs = hrfs + other_word[index]
        else:
            if other_word[index] in hrfs:
                return False
    return True


def show_possible_eslesme(my_word):
    eslesme = ""
    for word in wordlist:
        if match_with_gaps(my_word, word):
            eslesme = eslesme + word + " "
    print(eslesme)


def adamAsmaca_ipuclu(secret_word):
    #secret_word = "apple"
    tahmin = 6
    letters_guessed = []
    print("iPUCULU Adam Asmaca oyununa hoş geldiniz!\n")
    print("Tahmin etmeniz gereken kelime ", len(secret_word), " harflidir. \n")
    
    while not is_word_guessed(secret_word, letters_guessed) and tahmin > 0:
        
        print(tahmin, "tane tahmin hakkınız kaldı. \n")
        print("Su an kullanabileceğiniz harfler : \n", get_available_letters(letters_guessed))
        hrf= input("Lütfen bir harf tahmin edin : \n")
        if len(hrf) != 1 or not hrf.isalpha():
            if hrf== "*":
                show_possible_eslesme(get_guessed_word(secret_word, letters_guessed))
        else:
            hrf= hrf.lower()
            if hrf in letters_guessed:
                    tahmin = tahmin - 1         
            else:
                if hrf in secret_word:
                    letters_guessed.append(hrf)
                    print("İyi Tahmin:", get_guessed_word(secret_word, letters_guessed))
                    if is_word_guessed(secret_word, letters_guessed):
                     
                      print("TEBRİKLER!\n")
                      print("Skorunuz : ", tahmin * len(secret_word))
                else:
                    tahmin = tahmin - 1
                    print("Kelimede yok", get_guessed_word(secret_word,letters_guessed))
                    letters_guessed.append(hrf)

    if tahmin == 0:
        print("Bilemediniz :( \n Kelime : ", secret_word)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)
    
    

#if __name__ == "__main__":
   #secret_word = choose_word(wordlist)
   #adamAsmaca_ipuclu(secret_word)

