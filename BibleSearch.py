import string
def s(w):
    n = w.split(':')
    try:
        if n[0].isnumeric() and n[1].isnumeric():
            return True
        else:
            return False
    except:
        return False

def srh(inp):
    print("\n'{}'\n".format(inp))
    chek = False
    bible = open("Bible.txt", "r")
    for line in bible:
        d = dict()
        c = None
        if line.startswith("@@@"):
            print(line,"\n")
        if line.startswith("***"):
            #print(line)
            savedline = line
            line = next(bible)
            book = " "
            while line.startswith("!!!") is False:
                book = book + line.lower()
                try:
                    line= next(bible)
                except:
                    break
            v = book.split()
            for i in v:
                if s(i) is True:
                    if c is not None: d[c] = lst
                    c = i
                    lst = list()
                    continue
                elif c is None: continue
                lst.append(i)
            x = inp.lower()
            count = 0
            cond = False
            verlst = list()
            for k , v in d.items():
                for itm in v:
                    itm = itm.translate(str.maketrans('','',string.punctuation))
                    if itm == x:
                        verlst.append(k)
                        cond = True
                        count +=1
                        chek = True
            if cond == False:
                #print("No such word in", savedline.replace('***',""))
                continue
            else:
                print(savedline.rstrip())
                for i in verlst:
                    print(i)
                print("The word '{}' appeared {} times.".format(inp,count))
            print("\n")
        else: continue
    if chek == False:
        print("No such word in The Bible\n")
def asku():
    X = input("Enter a word to search: ")
    if ' ' in X:
        print("You entered more than one word!\n")
        asku()
    elif X == "exit":
        print('GoodBye!')
        exit()
    else:
        srh(X)
        asku()
asku()
