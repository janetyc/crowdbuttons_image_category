from datetime import datetime
import sys

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


filename = "image_category.results"
mode = 0 #False
if len(sys.argv) > 1:
    filename = sys.argv[1]
    if len(sys.argv) > 2:
        mode = 1
else:
    print "python check_result.py image_category.results"
    exit(0)

fp = open(filename,"r")
c = fp.read().strip()
lines = c.split("\n")

all_map = {}
for line in lines[1:]:
    items = line.split("\t")
    #print items
    if len(items) < 30:
        continue

    hitId = items[0][1:-1]
    url = items[13][1:-1]
    category = items[29][1:-1]
    others = items[30][1:-1]

    urls = url.split("/")
    items = urls[len(urls)-1].split("_")
    time_str = items[2][:-4]
    if time_str not in all_map:
        all_map[time_str] = []

    if category != "Others":
        if category:
            all_map[time_str].append(category)
        else:
            all_map[time_str].append(others)
    else:
        all_map[time_str].append(others)

all_data = []
summary_data = []
for key in all_map:
    url = key
    data = all_map[key]
    map={}
    for i in data:
        score = float(data.count(i))/len(data)
        map[i] = score

    output = [(j, i) for i,j in map.items()]
    output = sorted(output, reverse=True)
    result = ["%s:%.2f" %(j,i) for i,j in output]
    all_data.append((url,"|".join(result)))
    first = output[0]
    if first[0] > 0.66:
        summary_data.append(first[1])
    else:
        summary_data.append("None")

all_data = sorted(all_data)
for i, item in enumerate(all_data):
    print item
    time_str = item[0]
    dt = datetime.strptime(time_str, "%Y%m%d-%H%M")
    new_time_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    open("result.txt", "a+b").write("%s;%s;\n" % (new_time_str,item[1]))

    if mode == 1:
        open("mturk_labels.txt","a+b").write("%s;%s;\n" % (new_time_str, get_index(summary_data[i])))
