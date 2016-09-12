#Marilu D
#Q4

#Encoder Function
def encoder(string1):#calls the encoder
    '''decoding for problem 4 a'''
    len1 = len(string1)#defines
    newList = []
    counter = 1
    for i in range(len1):#indexes the length of the string
        lsts = []
        lsts.append(string1[i])#adding the index 
        print(string1[i])
        if i+1 == len1:
            lsts.append(counter)#adding the counter
            newList.append(lsts)
        elif string1[i] != string1[i+1]:
            lsts.append(counter)
            newList.append(lsts)
            counter = 1
        else:
            counter += 1#ends loop
    return newList#returns list

def decoder(lst1):#calls decoder
    ''' decoder for problem 4 b'''
    newStr = ""
    for coder in lst1:
        newStr += coder[0]*coder[1]
    return newStr #returns new list

def main1():
    '''main function for problem 4a'''
    string1 = "aadccccaa"
    print("The code of the string",string1, "is", encoder(string1))

def main2():
    '''main function for problem 4b'''
    lst1 = [['a',2],['d',1],['c',4],['a',2]]
    print("The list",lst1,"turns into the string",decoder(lst1))
    
    
