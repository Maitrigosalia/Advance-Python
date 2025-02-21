#File Handling Questions- text, binary, csv files
def Q1():
    f=open("story.txt")
    a=f.read()
    f.close()
    print(a)
Q1()

def Q2():
    f=open("story.txt")
    a=f.readline(5)
    f.close()
    print(a)
Q2()

def Q3():
    f=open("story.txt")
    a=f.readlines(1)
    f.close()
    print(a)
Q3()

def Q4():
    f=open("story.txt")
    a=f.readlines()
    for i in a:
        print(i)
Q4()

def Q5():
    f=open("story.txt")
    a=f.readlines(1)
    f.close()
    print(a)
Q5()

def Q6():
    f=open("story.txt")
    a=f.readlines()
    for i in a:
        x=i[0]
        print(x)
Q6()

def Q7():
    f=open("story.txt")
    a=f.readlines()
    for i in a:
        x=(i[0].lower())
        print(x)
Q7()

def Q8():
    f=open("story.txt")
    a=f.read()
    count=0
    for i in a:
        count=count+1
    print(count)
Q8()

def Q9():
    f=open("story.txt")
    a=f.readline()
    print(a)
    count=0
    for i in a:
        count=count+1
    print(count)        
Q9()

def Q10():
    #Find the number of characters in first line usinng readlines()    
    f=open("story.txt")
    a=f.readlines()
    
    count=0
    for i in a[0]:
        
        count=count+1
    print(count)
Q10()

def Q11():
    #program in python to display last 2 characters of all lines
    f=open("story.txt")
    a=f.readlines()
    for i in a:
        print(i[-6:])
Q11()

def Q12():
    #read all characters and display it in uppercase
    f=open("story.txt")
    a=f.readlines()
    for i in a:
        print(i.upper())
Q12()

def Q13():
    #count all uppercase characters from the file
    f=open("story.txt")
    a=f.read()
    count=0
    for i in a:
        if i.isupper():
            count=count+1
    print(count)        
Q13()

def Q14():
    #count number of spaces from the file
    f=open("story.txt")
    a=f.read()
    count=0
    for i in a:
        if ord(i)==32:
            count=count+1
    print(count)
Q14()

def Q15():
    #count number of vowels in file
    f=open("story.txt")
    a=f.read()
    count=0
    for i in a:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            count=count+1
    print(count)
Q15()

def Q16():
    #write the following data in a file
    f=open("t.txt","w")
    f.write("I am learning python")
    f.write("\ni am writing this blog")
    f.write("\nWelcome to my blog")
    f.close()

    f=open("t.txt")
    a=f.read()
    f.close()
    print(a)
Q16()

def Q17():
    #write a program to read data from one file and write it in another file
    f=open("story.txt")
    a=f.read()
    f.close()

    f=open("d.txt","w")
    f.write(a)
    f.close()

    f=open("d.txt")
    b=f.read()
    f.close()
    print(b)
Q17()

def Q18():
    #Write a program in python to copy all data from one file and copy it in another file except spaces
    f=open("story.txt")
    a=f.read()
    f.close()
    b=''

    f=open("d.txt","w")
    for i in a:
        if ord(i)!=32:
            b=b+i
    f.write(b)
    f.close()
            
    f=open("d.txt")
    c=f.read()
    f.close()
    print(c)
Q18()

def Q19():
    #Write a program in python to copy all data from one file and copy it in another file except vowels
    f=open("story.txt")
    a=f.read()
    f.close()
    b=''

    f=open("d.txt","w")
    for i in a:
        if i not in 'aeiouAEIOU':
            b=b+i
    f.write(b)
    f.close()
    
    f=open("d.txt")
    c=f.read()
    f.close()
    print(c)
Q19()

def Q20():
    #Write a python program to read all data and write alternate file and write it in another file
    f=open("story.txt")
    a=f.read()
    f.close()

    f=open("d.txt","w")
    for i in range(len(a)):
        if i%2==0:
            f.write(a[i])
    f.close()

    f=open("d.txt")
    c=f.read()
    f.close()
    print(c)
Q20()

def Q21():
    #Write a data from one file and count the frequency of the word which is input by the user
    f=open("story.txt")
    a=f.read()
    b=a.split(" ")
    print(b)
    n=input("Enter word :")
    c=0
    for i in b:
        if i==n:
            c=c + 1
    print(c)
    f.close()
Q21()

def Q22():
    #Read the data from one file and write it in another but write only those lines which starts with The
    f=open("story.txt")
    a=f.readlines()
    f.close()

    f=open("d.txt","w")
    for i in a:
        if (i[0:3]=='The'):
            f.write(i)
    f.close()
    f=open("d.txt")
    b=f.read()
    f.close()
    print(b)
Q22()

def Q23():
    #Write a program to read entire data from file using readline method
    f=open("story.txt")
    for i in range(39):
        a=f.readline()
        print(a)        
Q23()

def Q24():
    #Write a program from one file to another by swapping the cases
    f=open("story.txt")
    a=f.read()
    x=a.swapcase()
    print(x)
Q24()

def Q25():
    #Write a program to create a list of 5 number input from the user and write that list in another file
    l=eval(input("Enter no :"))
    f=open("d.txt","w")
    f.writelines(str(l))
    f.close()

    f=open("d.txt")
    a=f.read()
    f.close()
    print(a)
Q25()

def Q26():
    #Write a program to create a list of 5 numbers and write the list in file. Now read only even numbers
    l=[]
    for i in range(0,5):
        val=int(input("Enter Number : "))
        l.append(val)
    f=open("story.txt","w")
    f.writelines(str(l))
    f.close()

    f=open("story.txt","r")
    a=f.read()
    for i in a:
        print(i)
    f.close()
    print(l)
Q26()

def Q27():
    #Write a program in python to replace one word to another and write it in another file
    f=open("story.txt")
    a=f.read()
    f.close()

    a=a.replace("Lily","Maitri")
    print(a)
    f=open("d.txt","w")
    f.write(a)
    f.close()
    

    f=open("d.txt")
    b=f.read()
    f.close()
    print(b)    
Q27()

def Q28():
    #Write a program to replace a word in the same file
    f=open("story.txt")
    a=f.read()
    f.close()

    a=a.replace("Lily","Maitri")
    f=open("story.txt","w")
    f.write(a)
    f.close()
    print(a)
Q28()

def Q29():
    #Write a program to replace a word to another in a file
    f=open("story.txt")
    a=f.read()
    f.close()

    a=a.replace("The","Them")
    f=open("story.txt","w")
    f.write(a)
    f.close()
    print(a)
Q29()

def Q30():
    #Write a program to replace a character by another character in a file and accept both the character from the user
    f=open("Q30.txt","w")
    f.write("I am Maitri Gosalia, I study Python")
    f.close()

    f=open("Q30.txt")
    a=f.read()
    print(a)
    f.close()

    n1=input("Enter character :")
    n2=input("Enter ch :"),
    b=""
    for i in range(len(a)):
        if a[i]==n1:
            b=b+n2
        else:
            b=b+a[i]
    f=open("Q30.txt","w")
    f.write(b)
    f.close()
    
    f=open("Q30.txt")
    a=f.read()
    f.close()
    print(a)    
Q30()

def Q31():
    x=input("enter the first number : ")
    y=input("enter the second ch : ")
    f=open("story.txt")
    a=f.read()
    a=a.replace(x,y)
    f.close()
    print(a)
Q31()

#Poem text
def Q1():
    try:
        f=open("poem.txt","w")
        f.write("Twinkle, Twinkle little star,\n")
        f.write("How I wonder what you are!\n")
        f.write("Up above the world so high,\n")
        f.write("Like a diamond in the sky.")
        f.close()
        print("Poem")
    except:
        print("Error")
Q1()

def Q2():
    f=open("poem.txt")
    a = f.read()
    f.close()
    print(a)
Q2()

#Replae Twinkle word by Shiny

def Q3():
    try:
     
        f=open("poem.txt")
        a=f.read()
        a=a.replace("sky","cloud")
        f.close()
        f=open("poem.txt","w")
        f.write(a)
        f.close()
    except:
        print("Error")    
Q3()

#csv, binary file
def Q1():
    l=["\nHi I am Maitri Gosaliya","\nI stay near Sobo Centre"]
    '''
    f=open("maitri.txt","a") #r-w-a
    f.writelines(l)
    f.close()
    '''
    f=open("maitri.txt","r")
    a=f.readlines()
    f.close()


    for i in a:
        print(i[0].upper())
    
Q1()

def Q2():
    import pickle
    #write-dump()
    #read-load()
    '''
    f=open("data1.dat","wb")#wb+-rb+-ab+
    a="Hello All"
    pickle.dump(a,f)
    f.close()
    '''
    f=open("data1.dat","rb")
    a=pickle.load(f)
    f.close()
    print(a)
Q2()

def Q3():
    #csv - comma seperated values
    import csv
    f=open("data.csv","r")
    ans=csv.reader(f)
    for i in ans:
        print(i[1])
    
Q3()

def Q4():
    import csv
    f=open("student.csv","w",newline='')
    a=csv.writer(f)
    a.writerow(['RollNo','Name','Grade'])
    a.writerow(['101','Amit Barot','A+'])
    a.writerow(['102','Madhur Patel','A'])
    f.close()
Q4()

#Practice of File Handling- txt,dat,csv

def Q5():
    l=["\nI am Maitri Gosalia","\nI stay in Ahemdabad"]

    f=open("meet.txt","a")
    f.writelines(l)
    f.close()

    f=open("meet.txt","r")
    a=f.readlines()
    f.close()
    
    for i in a:
        print(i[2].upper())
Q5()

def Q6():
    import pickle
    f=open("car.dat","wb")
    a="Hello Maitri"
    pickle.dump(a,f)
    f.close()

    f=open("car.dat","rb")
    a=pickle.load(f)
    f.close()
    print(a)
Q6()

def Q7():
    import csv
    f=open("class.csv","w")
    a=csv.writer(f)
    a.writerow(['English','Science'])
    a.writerow(['001','032'])
    f.close()
Q7()

def Q8():
    import csv
    f=open("day.csv","r")
    a=csv.reader(f)
    for i in a:
        print(i[1])
    f.close()
Q8()

#Exception Handling
d={"k1":'maitri',"k2":'kishan'}
try:
    print(d['k5'])
except TypeError:
    print("Check error")
except NameError: 
    print("Error")
except IndexError:
    print("Check index")
except ZeroDivisionError:
    print("Zero is not divisible")
except KeyError:
    print("Check key")
finally:
    print("final done")

print(d)

d={'k1':'maitri','k2':'kishan','k3':'meet'}
try:
    if d['k4']==5:
        raise KeyError("Check key error")
    else:
        print(a)
except:
    raise

#Que1

#Take 5 marks of subject, total marks(500)if total marks is gerater then 500 then exception is generated
a=int(input("Enter subj 1 marks :"))
b=int(input("Enter subj 2 marks :"))
c=int(input("Enter subj 3 marks :"))
d=int(input("Enter subj 4 marks :"))
e=int(input("Enter subj 5 marks :"))

t=a+b+c+d+e
try:
    if t>500:
        raise TypeError("Correct error")
    else:
        print(a)
except:
    raise 
finally:
    print("Final done")

#Que2
l=[]
print("How many number of elements do you want in list ?:")
b=int(input("Enter number of elements :"))
for i in range(b):
    print("Enter",i," elements of list :")
    c=int(input())
    l.append(c)
print(l)
print("Which element do you want ?")
a=int(input("Enter index of element :"))
try:
    if a>len(l):
        raise IndexError("Index not found")
    else:
        print(l[a])
except:
    raise
finally:
    print("Final done")
    
#binary file
def Q1():
    import pickle
    f=open("book.dat","wb")
    l=[]
    while True:
        x=eval(input("Enter id :"))
        if x==0:
            break
        else:
            a=input("Author :")
            p=eval(input("Enter Price :"))
            val=[x,a,p]
            l.append(val)
    pickle.dump(l,f)
    print("successful")
    f.close()
            
    f=open("book.dat","rb")
    y=pickle.load(f)
    f.close()
    print(y)
Q1()

def Q2():
    import pickle
    f=open("student1.dat","wb")
    l=[]
    while True:
        per=eval(input("Enter Percentage :"))
        if per<75:
            break
        else:
            ano=eval(input("Enter admin no :"))
            name=input("Enter Name :")
            val=[per,ano,name]
            l.append(val)
    pickle.dump(l,f)
    print("Successful")
    f.close()

    f=open("student1.dat","rb")
    x=pickle.load(f)
    f.close()
    print(x)
Q2()

def Q3():
    import pickle
    f=open("bus.dat","wb")
    l=[]
    while True:
        d=input("Enter Destination :")
        if d=='kochin':
            no=eval(input("Enter bus no :"))
            sp=input("Starting point :")
            val=[no,sp,d]
            l.append(val)
            pickle.dump(l,f)
            print("Successful")
            f.close()

            f=open("bus.dat","rb")
            x=pickle.load(f)
            f.close()
            print(x)
        else:
            break

Q3()
            
    

             


            
            
        
    
            

    
    
        
       

    






    






    






    
        
        
    
    


        
    
    
        
    
    
    
