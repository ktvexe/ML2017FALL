#!/usr/bin/python

def main():
    count_dict = dict()
    flag_dict = dict()
    
    with open("words.txt","r") as file_input:
        word_list = file_input.read().rstrip().split(" ")
    for word in word_list:
        if(word not in count_dict):
            count_dict[word] = 1
            flag_dict[word] = True
        else:
            count_dict[word] = count_dict[word]+1
    
    i = 0
    for word in word_list:
        if(flag_dict[word] == True):
            print word+" "+str(i)+" "+str(count_dict[word])
            flag_dict[word] = False
            i = i+1

if __name__ == "__main__":
    main()
