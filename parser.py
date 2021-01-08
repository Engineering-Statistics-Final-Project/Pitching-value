import requests
from bs4 import BeautifulSoup

for month in range(1995,2020):
    url_string = "https://www.fangraphs.com/leaders.aspx?pos=all&stats=pit&lg=all&qual=0&type=6&season="
    url_month  = str(month)
    url_string2 = "&month=0&season1="
    url_string3 = "&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=&enddate="
    __url__ = url_string+url_month+url_string2+url_month+url_string3

    response = requests.get(__url__)
    __html_parser__ = BeautifulSoup(response.text,"html.parser")

    regular_str = "id=LeaderBoard1_dg1_ctl00__"
    result = []

    __file__ = "DATA/"+str(month)+"_tmp.txt" 
    FILE = open(__file__,mode="w")

    for idx in range(0,30):
        tmp_class_bs4 = __html_parser__.find("tr",id=("LeaderBoard1_dg1_ctl00__"+str(idx)))
        result.append(tmp_class_bs4)
        FILE.write(str(tmp_class_bs4))
        FILE.write("")

    print("Build "+ str(month) +" Successfully!")
    FILE.close()

    

for month2 in range(1995,2020):
    __file2__ = "DATA/"+str(month2)+"_tmp.txt" 
    FILE2 = open(__file2__,mode="r")

    __file_ans = "DATA/"+str(month2)+".txt"
    FILE_ans = open(__file_ans,mode="w")

    all_str = FILE2.readlines()
    ans = []
    
    if(month2>1997):
        for i in range(0,30):
            idx1 = i*2
            idx2 = i*2+1
            str1 = all_str[idx1]
            str2 = all_str[idx2]
            str1_len = len(str1)
            str2_len = len(str2)
            
            for k in range(0,50):
                flag = 0
                __str__ = ""
                for j in range(0,str2_len):
                    if(str2[j]=='<' and flag==k): break
                    if(flag==k): __str__=__str__+str2[j]
                    if(str2[j]=='>'): flag = flag +1
                if(len(__str__)!=0):ans.append(__str__)

        #print(len(ans))
        for i in range(0,30):
            for j in range(1,9):
                if(j==1): FILE_ans.write('{:15}'.format('"'+ans[i*10+j]+'"'))
                else: FILE_ans.write('{:13}'.format('"'+ans[i*10+j]+'"'))
            FILE_ans.write("\n")
        
        print("Parse " + str(month2) +" Successfully!")
        FILE2.close()
        FILE_ans.close()
    else:
        for i in range(0,28):
            idx1 = i*2
            idx2 = i*2+1
            str1 = all_str[idx1]
            str2 = all_str[idx2]
            str1_len = len(str1)
            str2_len = len(str2)
            
            for k in range(0,50):
                flag = 0
                __str__ = ""
                for j in range(0,str2_len):
                    if(str2[j]=='<' and flag==k): break
                    if(flag==k): __str__=__str__+str2[j]
                    if(str2[j]=='>'): flag = flag +1
                if(len(__str__)!=0):ans.append(__str__)

        #print(len(ans))
        for i in range(0,28):
            for j in range(1,9):
                if(j==1): FILE_ans.write('{:15}'.format('"'+ans[i*10+j]+'"'))
                else: FILE_ans.write('{:13}'.format('"'+ans[i*10+j]+'"'))
            FILE_ans.write("\n")
        
        print("Parse " + str(month2) + " Successfully!")
        FILE2.close()
        FILE_ans.close()