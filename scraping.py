import os
import json

input_file = open('./.tmp_json/data.json', 'r')
#convert json to list
conv = json.load(input_file)


#LIST EN OUTPUT :
links = [my_list['url-href'] for my_list in conv]

#list to str
#faire la modif pour toute les pages
list_to_str = '!++delim++!'.join(links)
str_to_list = list_to_str.split("https://www.afnic.fr/noms-de-domaine/tout-savoir/annuaire-bureaux-enregistrement/page/1/?")

#Parser les liens et enlever 'https://www.' | 'http://www.' | 'www.' | 'https://' | 'http://'

list_to_str1 = ''.join(str_to_list)
str_to_list1 = list_to_str1.split("https://www.")

list_to_str2 = ''.join(str_to_list1)
str_to_list2 = list_to_str2.split("http://www.")

list_to_str3 = ''.join(str_to_list2)
str_to_list3 = list_to_str3.split("https://")

list_to_str4 = ''.join(str_to_list3)
str_to_list4 = list_to_str4.split("http://")

list_to_str5 = ''.join(str_to_list4)
str_to_list5 = list_to_str5.split("www.")

list_to_str6 = ''.join(str_to_list5)
str_to_list6 = list_to_str6.split("!++delim++!")

prefix = ['developer.', 'developers.']

def check_without_s():
    pos = 0
    while pos < len(str_to_list6):
        print("pos " + str(pos) + " : " + str_to_list6[pos])
        url_without_s = prefix[0] + str_to_list6[pos]
        response = os.system("curl --request GET \
        --url " + url_without_s)

        file = open("./csv/links_verified.csv", "a")
        if response == 0:
            print("-------------------- " + url_without_s, "is up! --------------------")
            file.write(url_without_s)
            file.write('\n')
            file.close()
        else:
            print(url_without_s, 'is not working!')
        pos += 1


def check_with_s():
    i = 0
    while i < len(str_to_list6):
        print("pos " + str(i) + " : " + str_to_list6[i])
        url_with_s = prefix[1] + str_to_list6[i]
        response = os.system("curl --request GET \
        --url " + url_with_s)

        file = open("./csv/links_verified.csv", "a")
        if response == 0:
            print("-------------------- " + url_with_s, "is up! --------------------")
            file.write(url_with_s)
            file.write('\n')
            file.close()
        else:
            print(url_with_s, 'is not working!')
        i += 1


def main():
    check_without_s()
    check_with_s()


if __name__ == main():
    main()