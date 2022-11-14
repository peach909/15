if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as fileptr:
        sentences = f.readlines()

        for sentence in sentences:
            if "," in sentences:
                print(sentences)
