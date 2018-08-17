
def get_line_str(arr):
    return " ".join(str(x) for x in arr)

def main():
    file = open(r"word.in", "r", encoding="utf-8-sig")
    content = file.readlines()
    wordcount={}
    l = 1
    for line in content:
        for word in line.split():
            if word not in wordcount:
                wordcount[word] = {}
                wordcount[word]["line"] = [l]
                wordcount[word]["count"] = 1
            else:
                if l not in wordcount[word]["line"]:
                    wordcount[word]["line"].append(l)
                wordcount[word]["count"] += 1
        l += 1
    for w, a in wordcount.items():
        print(a["count"], w, get_line_str(a["line"]))

main()