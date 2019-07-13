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
if data.lower()=='bottle' :
        print("""<meta name="viewport" content="width=device-width, initial-scale=1">""")

        print("""<input type=button onClick="location.href=' https://www.flipkart.com/kitchen-cookware-serveware/water-bottles/pr?sid=upp%2Cf2k%2C0zz&q=bottle&otracker=categorytree&p%5B%5D=facets.color%255B%255D%3DBlue&p%5B%5D=facets.color%255B%255D%3Dblue&p%5B%5D=facets.serviceability%5B%5D%3Dtrue'" value='blue'>""")

        print("""<input type=button onClick="location.href='https://www.flipkart.com/kitchen-cookware-serveware/water-bottles/pr?sid=upp%2Cf2k%2C0zz&q=bottle&otracker=categorytree&p%5B%5D=facets.color%255B%255D%3DRed&p%5B%5D=facets.color%255B%255D%3Dred&p%5B%5D=facets.serviceability%5B%5D%3Dtrue'" value='red'>""")

        print("""<input type=button onClick="location.href='https://www.flipkart.com/kitchen-cookware-serveware/water-bottles/pr?sid=upp%2Cf2k%2C0zz&q=bottle&otracker=categorytree&p%5B%5D=facets.color%255B%255D%3DSteel%252FChrome&p%5B%5D=facets.color%255B%255D%3DSilver&p%5B%5D=facets.serviceability%5B%5D%3Dtrue'" value='silver'>""")

        print("""<input type=button onClick="location.href='https://www.flipkart.com/kitchen-cookware-serveware/water-bottles/pr?sid=upp%2Cf2k%2C0zz&q=bottle&otracker=categorytree&p%5B%5D=facets.color%255B%255D%3DSteel%252FChrome&p%5B%5D=facets.color%255B%255D%3DSilver&p%5B%5D=facets.serviceability%5B%5D%3Dtrue'" value='brown'>""")

        print("""<input type=button onClick="location.href='https://www.flipkart.com/kitchen-cookware-serveware/water-bottles/pr?sid=upp%2Cf2k%2C0zz&q=bottle&otracker=categorytree&p%5B%5D=facets.color%255B%255D%3DBlack&p%5B%5D=facets.color%255B%255D%3DGrey&p%5B%5D=facets.serviceability%5B%5D%3Dtrue'" value='black'>""")

        print("""<input type=button onClick="location.href='https://www.flipkart.com/kitchen-cookware-serveware/water-bottles/pr?sid=upp%2Cf2k%2C0zz&q=bottle&otracker=categorytree&p%5B%5D=facets.color%255B%255D%3DPink&p%5B%5D=facets.color%255B%255D%3Dpurple&p%5B%5D=facets.color%255B%255D%3DOrange&p%5B%5D=facets.serviceability%5B%5D%3Dtrue'" value='pink'>""")

else:
        print("nothing found similar")
