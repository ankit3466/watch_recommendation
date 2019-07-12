#! /usr/bin/python3
import cgi
import subprocess

#these 3 lines are optional
import cgitb
#to show common error in browser
cgitb.enable()

print("content-type:text/html")
print("")

webdata=cgi.FieldStorage()      #this will collect all the html code with data
#now extracting value of x
data=webdata.getvalue('x')
#sending output to client via web server
#print(data)
#output=subprocess.getoutput(data)
if data.lower()=='tshirt' :
        print("""<meta name="viewport" content="width=device-width, initial-scale=1">""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?bbn=1968123031&rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_n_feature_three_browse-bin%3A3765389031&dc&fst=as%3Aoff&qid=1562575372&rnid=1974917031&ref=lp_1968123031_nr_p_n_feature_three_br_2'" value='all tshirts'>""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968123031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_n_feature_three_browse-bin%3A3765389031%2Cp_n_size_two_browse-vebin%3A1975318031%7C1975328031%7C1975331031&dc&fst=as%3Aoff&fst=as%3Aoff&qid=1562606176&qid=1562606176&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_14'" value='blue'>""")

        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968123031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_n_feature_three_browse-bin%3A3765389031%2Cp_n_size_two_browse-vebin%3A1975323031%7C1975332031&dc&fst=as%3Aoff&fst=as%3Aoff&qid=1562576691&qid=1562576691&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_3 '" value='white'>""")

        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968123031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_n_feature_three_browse-bin%3A3765389031%2Cp_n_size_two_browse-vebin%3A1975317031&dc&fst=as%3Aoff&fst=as%3Aoff&qid=1562606110&qid=1562606110&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_1'" value='black'>""")
        
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968123031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_n_feature_three_browse-bin%3A3765389031%2Cp_n_size_two_browse-vebin%3A1975326031%7C1975333031&dc&fst=as%3Aoff&qid=1562607634&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_9'" value=' orange and yellow'>""")

        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968123031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_n_size_two_browse-vebin%3A1975321031%2Cp_n_feature_three_browse-bin%3A3765389031&dc&fst=as%3Aoff&qid=1562860652&rnid=1974917031&ref=sr_nr_p_n_feature_three_browse-bin_3'" value='green'>""")

        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968123031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968120031%2Cn%3A1968123031%2Cp_n_feature_three_browse-bin%3A3765389031%2Cp_n_size_two_browse-vebin%3A1975329031&dc&fst=as%3Aoff&qid=1562607702&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_8'" value='red'>""")






elif data.lower()=='shirt':
        print("""<meta name="viewport" content="width=device-width, initial-scale=1">""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?bbn=1968094031&rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968093031%2Cn%3A1968094031%2Cp_n_feature_three_browse-bin%3A1974920031&dc&fst=as%3Aoff&qid=1562575618&rnid=1974917031&ref=lp_1968094031_nr_p_n_feature_three_br_3'" value='all shirts'>""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968094031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968093031%2Cn%3A1968094031%2Cp_n_feature_three_browse-bin%3A1974920031%2Cp_n_size_two_browse-vebin%3A1975318031%7C1975328031%7C1975331031&dc&fst=as%3Aoff&qid=1562607919&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_14'" value='blue'>""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968094031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968093031%2Cn%3A1968094031%2Cp_n_feature_three_browse-bin%3A1974920031%2Cp_n_size_two_browse-vebin%3A1975332031&dc&fst=as%3Aoff&qid=1562576013&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_13'" value='white'>""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968094031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968093031%2Cn%3A1968094031%2Cp_n_feature_three_browse-bin%3A1974920031%2Cp_n_size_two_browse-vebin%3A1975317031%7C1975322031&dc&fst=as%3Aoff&qid=1562608085&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_3'" value='black'>""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?i=apparel&bbn=1968094031&rh=n%3A1571271031%2Cn%3A1571272031%2Cn%3A1968024031%2Cn%3A1968093031%2Cn%3A1968094031%2Cp_n_feature_three_browse-bin%3A1974920031%2Cp_n_size_two_browse-vebin%3A1975326031%7C1975333031&dc&fst=as%3Aoff&qid=1562608013&rnid=1974754031&ref=sr_nr_p_n_size_two_browse-vebin_9'" value='orange and yellow'>""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?bbn=1968093031&rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968093031%2Cp_n_size_two_browse-vebin%3A1975321031&dc&fst=as%3Aoff&qid=1562608800&rnid=1974754031&ref=lp_1968093031_nr_p_n_size_two_browse-_10'" value='green'>""")
        print("""<input type=button onClick="location.href='https://www.amazon.in/s?bbn=1968093031&rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1968024031%2Cn%3A1968093031%2Cp_n_size_two_browse-vebin%3A1975321031&dc&fst=as%3Aoff&qid=1562608800&rnid=1974754031&ref=lp_1968093031_nr_p_n_size_two_browse-_10'" value='red'>""")


else:
        print("nothing found similar")
