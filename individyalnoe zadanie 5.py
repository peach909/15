if __name__ == "__main__":
    k=0
    with open ("prosto text.txt","r", encoding="utf-8") as fileptr:
        sentences =f.readlines()
        fileptr.close()
        print(k)
        for sentence in sentences:
            if "друг" in sentence:
                 k=k+1
                
