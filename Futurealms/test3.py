def spam_delete(letter):
    letter_l=letter.split(' ')
    punct=['', ',', '.', '!', '?', ':',';']
    todelete=[]
    number_of_spam=0
    for k in range(0,len(letter_l)):
        for i in range(0,len(punct)):
            if letter_l[k]==punct[i]:
                todelete.append(k)
    for k in range(0,len(todelete)):
        del letter_l[k]
    print (letter_l)
    spam=['casino','buy','popular','acquainted']
    for k in range (0,len(spam)):
        if (letter.count(spam[k]))>0:
            number_of_spam=number_of_spam+letter.count(spam[k])
    prob=number_of_spam/len(letter_l)
    if prob>=0.5:
        return 'Spam'

