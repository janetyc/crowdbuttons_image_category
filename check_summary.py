from datetime import datetime

def get_index(label):
    if label == "Empty":
        return 0
    elif label == "Meeting":
        return 1
    elif label == "Lecture":
        return 2
    elif label == "Study":
        return 3
    else:
        return -2

fp = open("image_category.summary","r")
c = fp.read().strip()
lines = c.split("\n")

for line in lines[1:]:
    data = line.split("\t")
    urls = data[1].split("/")

    items = urls[len(urls)-1].split("_")
    time_str = items[2][:-4]

    dt = datetime.strptime(time_str, "%Y%m%d-%H%M")
    new_time_str = dt.strftime("%Y-%m-%d %H:%M:%S")

    if data[3] != "[no agreement]":
        print "%s;%s;%s;" % (new_time_str,data[3],data[5])
    else:
        print "%s;%s;%s;" % (new_time_str,"None","0")
        
    open("mturk_labels.txt","a+b").write("%s;%d;\n" % (new_time_str, get_index(data[3])))
        
