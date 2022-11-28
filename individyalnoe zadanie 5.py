if __name__ == "__main__":
    k=0
    f=0
    with open ("prosto text.txt","r", encoding="utf-8") as f:
        sentences =f.readlines()
    for sentence in sentences:
        if "друг" in sentence:
            k=k+1
        print(k)
