with open("sample.txt","r") as file:
    text=file.read()

text=text.lower()
for p in['.',',','?','-',':']:
    text=text.replace(p,'')

words=text.split()
fd={}
for w in words:
    if w in fd:
        fd[w]+=1
    else:
        fd[w]=1

  #Add the text file in the same working directory as the python program
