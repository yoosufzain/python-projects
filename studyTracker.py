study_data = {}
while True:
    subject = input("Enter subject")
    if subject == "":
        break
    hours = int(input("Enter studied hour"))
    study_data[subject] = hours
def create_chart(data):
    title = f"{'Chart of your data':-^30}"
    lengths = [i for i in data.values()]
    max_length = max(lengths)
    chart = ""
    lines = ""
    for i in range((max_length+1),-1,-1):
        lines += f"{i:>3}|"
        for l in lengths:
            if i<= l:
                lines +=" o "
            else:
                lines +="   "
        lines +="\n"
    under_line = "   "
    for i in range(len(lengths)*3+1):
        under_line+="-"
    subjects = [s for s in data.keys()]
    max_length= max([len(l) for l in subjects])
    formatted_subject = [s.ljust(max_length) for s in subjects]
    text = ""
    for i in range(max_length):
        text += "   "
        for t in formatted_subject:
            text += "  "+t[i]
        text +="\n"
    chart = title+"\n"+lines+under_line+"\n"+text
    print(chart)
create_chart(study_data)
