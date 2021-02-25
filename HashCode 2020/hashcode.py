# def readFile(fileName):
#     with open(fileName) as f:
#         lst = [i.strip().split() for i in f]
#     line1 = lst[0]
#     scores = lst[1]
#     sc = []
#     for count,ele in enumerate(scores):
#         sc.append((count,ele))
#     sc = sorted(sc,key=lambda x: x[1],reverse = True)
#     dic = {}
#     count = 0
#     for j in lst[2:]:
#         if not str(count) in dic:
#             print(j[2])
#             dic[str(count)] = {'scant': j[1],'shipn':j[2]}
#             continue
#         else:
#             for b in j:
#                 if 'books' in dic[str(count)]:
#                     dic[str(count)]['books'].append((int(b),int(scores[int(b)])))
#                 else:
#                     dic[str(count)]['books'] = [(int(b),int(scores[int(b)]))]
#         count +=1
#     return dic,sc, int(line1[2]), int(line1[1])

"dic - {#lib : [{scant:#days, shipn:#book, books:[7,18,3]}]}"
"sc - scoores"
def readFile(fileName):
    with open(fileName) as f:
        
        score = list()
        line = f.readline()
        line = line.strip("\n").split(" ")
        B = int(line[0])
        L = int(line[1])
        D = int(line[2])
        line = f.readline()
        tempScore = line.strip().split()
        for e in tempScore:
            score.append(int(e))
        lastId = 0
        dic = dict()
        for line in f: 
            line = line.strip().split()
            if not lastId in dic:
                dic[lastId] = {'scant': int(line[1]), 'shipn': int(line[2])}
                continue
            else:
                book = list()
                tempBook = line
                for e in tempBook:
                    book.append((int(e), score[int(e)]))
                    dic[lastId]['books'] = book
            lastId += 1
        return L, D, dic

def ratio(dic):
    libDic = dict()
    libDic1 = dict()
    tup = tuple()
    for k in dic.keys():
        books = dic[k]['books']
        B = len(books)
        scant = int(dic[k]['scant'])
        ratio = B / scant
        shipn = int(dic[k]['shipn'])
        k = int(k)
        tempDic = {'scant': scant, 'shipn': shipn, 'ratio': ratio, 'books': books}
        libDic[k] = tempDic
    return libDic

def ratioPerm(dic, D, L):
    count2 = 0
    id = list()
    repB = list()
    count = 0
    sum = 0
    lst = list()
    for k in dic.keys():
        lst.append((k, dic[k]['ratio']))
    lst = sorted(lst, key= lambda x: x[1], reverse=True)
    while D > 0 and count != L:
        for tup in lst:
            count += 1
            lib = tup[0]
            books = dic[lib]['books']
            shipn = dic[lib]['shipn']
            books = sorted(books, key=lambda x: x[1], reverse=True)
            D = D - dic[lib]['scant']
            nBooks = D * shipn
            bookSend = list()
            count2 = 0
            for i in range(nBooks):
                if i == len(books):
                    break
                sc = books[i][1]
                book = books[i][0]
                if book in repB:
                    continue
                else:
                    repB.append(book)
                sum += sc
                count2 += 1
                bookSend.append(book)
            id.append((lib, count2, bookSend))
    return count, id

def output(count, id, fileName):
    fName = fileName[0:len(fileName) - 4] + "_output.txt"
    with open(fName, "w") as f:
        f.write(str(count))
        for tup in id:                     
            if tup[1] == 0:
                continue
            f.write("\n")
            f.write(str(tup[0]) + " " + str(tup[1]) + "\n")
            for e in tup[2]:
                f.write(str(e) + " ")
            

def main():
    fileNames = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt",
                  "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]
    for fileName in fileNames:
        L, D, dic = readFile(fileName)
        dic = ratio(dic)
        count, id  = ratioPerm(dic, D, L)
        output(count, id, fileName)

main()