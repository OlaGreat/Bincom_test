import re

baby_name_pattern = r'<td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>'
file_url = r'C:\Users\DELL\Documents\bincom_python_class\2nd_contact_assignment\baby_name\baby2008.html'
baby_nameFile = open("baby_names.txt", "w")


def extract_baby_names(filename):
    
    with open(filename, 'r') as baby_html:
        baby_name =[]
        baby_data = baby_html.read()
        baby_file = re.findall(baby_name_pattern, baby_data)

        for i in baby_file:
            for j in i[1:3]:
                baby_name.append(j)

    arrange_baby_names(baby_name)

def arrange_baby_names(baby_name):
    count = 0
    while count < len(baby_name):
        name = baby_name[count] + " " + baby_name[count+1]
        baby_nameFile.write(name + "\n")
        count+=2
        

extract_baby_names(file_url)
baby_nameFile.close()