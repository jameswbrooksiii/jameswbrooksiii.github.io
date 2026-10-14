import sys, time, os, pwinput, random

def medScroll(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def fastScroll(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)

def slowScroll(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

def reallySlowScroll(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1)

def elipses():
    reallySlowScroll(f"""...""")

def chatElipses(x):
    for i in range(x):
        reallySlowScroll(f"""...""")
        time.sleep(1)
        sys.stdout.write('\b\b\b   ')
        sys.stdout.flush()
        sys.stdout.write('\b\b\b')
        sys.stdout.flush()
        time.sleep(1)

def countUp():
    slowScroll(f""" """)
    for i in range(50):
        #sys.stdout.write(str(random.randrange(1,10)))
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(f""",""")
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(f""",""")
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(f""",""")
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(str(random.randrange(0,10)))
        sys.stdout.flush()
        sys.stdout.write(f"""cr""")
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
        sys.stdout.flush()
        #time.sleep(0.1)
    sys.stdout.write('               ')
    sys.stdout.flush()
    sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
    sys.stdout.flush()

logo1 = f"""\n----------------------------------------------------
|         ____  _____ ____    _    ____ ___        |
|  __/\__/ ___|| ____| __ )  / \  / ___/ _ \       |"""
logo2 = f"""
|  \    /\___ \|  _| |  _ \ / _ \| |  | | | |      |
|  /_  _\ ___) | |___| |_) / ___ \ |__| |_| |      |
|  __\/__|____/|_____|____/_/   \_\____\___/  _    |"""
logo3 = f"""
| |  \/  (_)_ __ (_)_ __   __ _  | |  | |_ __| |   |
| | |\/| | | '_ \| | '_ \ / _` | | |  | __/ _` |   |
| | |  | | | | | | | | | | (_| | | |__| || (_| |_  |"""
logo4 = f"""
| |_|  |_|_|_| |_|_|_| |_|\__, | |_____\__\__,_(_) |
|                         |___/                    |
----------------------------------------------------
"""

copyrights = f"""\nCopyright (c) The Company. All rights reserved.
SEBACO Mining Ltd. is a registered subsidiary of The Company.
Revision 88 / Serial Number 840726
ATTENTION: This version is out of date. Please contact a system administrator.

Please login.

User_ID: """

mission1 = f"""\n\nJob Type:"""
mission2 = f"""    Cargo Freight"""
destination1 = f"""\nDestination:"""
destination2 = f""" Barnaul Jump-1 Cluster, Ypsilon-14, Sebaco Asteroid Mining Facility"""

salary1 = f"""\n\nLOTT_GUST Standard Monthly Salary:"""
salary2 = f""" 2,500cr"""
duration1 = f"""\nJob Duration:"""
duration2 = f"""                      3 Months"""
total1 = f"""\nTotal Payment:"""
total2 = f"""                     7,500cr"""

status1 = f"""\n\nJob Status:"""
status2 = f""" FAILED"""

payment = f"""\n\nPAYMENT WITHHELD. Company damages sustained. Press Enter to view damages.\n"""

damagesHeader = f"""\n\n--------------------------------------------------
| ITEM                         |  ESTIMATED_COST |
--------------------------------------------------"""
drone = f"""\n| Salvage Drone                |"""
droneCost = f"""        10,000cr |"""
android = f"""\n| Terminated Corporate Android |"""
androidCost = f""" RESTRICTED_DATA |"""
personnel = f"""\n| Other Personnel              |"""
personnelCost = f"""      Negligible |"""
facilities = f"""\n| Ypsilon-14 Facilities        |"""
facilitiesCost = f"""  ~200,000,000cr |"""
equipment = f"""\n| Lost Mining Equipment        |"""
equipmentCost = f"""  ~200,000,000cr |"""
research = f"""\n| Lost Research                |"""
researchCost = f""" RESTRICTED_DATA |"""
profits = f"""\n| Lost Potential Profits       |"""
profitsCost = f"""         [ERROR] |"""
damagesFooter = f"""\n--------------------------------------------------"""
estimated = f"""\n\n  TOTAL_ESTIMATED_DAMAGES       """
estimatedCost = f"""1,000,000,000cr"""

accept = f"""\n\nPress Enter to accept and establish connection with The Board.\n"""

question11 = f"""Hello, LOTT_GUST."""
question12 = f""" Briefly describe what happened on Ypsilon-14.\n"""
question21 = f"""Reports from your debriefing indicate that the supposed "hostile entity" on the station was "invisible"."""
question22 = f""" Elaborate on this."""
question23 = f""" Do you have any proof?\n"""
question3 = f"""Did anyone authorize you to initiate the self-destruct sequence?\n"""
question4 = f"""Were you aware that Ashraf was an Android?\n"""
thanks1 = f"""Thank you, LOTT_GUST."""
thanks2 = f""" You may now leave the room."""
thanks3 = f""" You'll be hearing from us again very soon."""
end = f"""\n\nCONNECTION LOST: Communications complete.
Please do NOT terminate this program or power off the terminal. A system administrator will be here shortly to securely log you out.\n"""


os.system("cls")
input()
os.system("cls")
medScroll(f"""Please wait """)
chatElipses(2)
elipses()
time.sleep(1)
medScroll(f""" ready""")
time.sleep(1)
fastScroll(f"""\nCollecting packets
    Accessing database ... done
    Downloading packages ... done
    Installing build dependencies ... done
    Getting requirements to build terminal environment ... done
    Preparing metadata ... done
Building environment for terminal
    Building environment for collected packages ... done
    Successfully stored in directory
Successfully built terminal environment""")
medScroll(f"""\nBooting """)
time.sleep(1)
elipses()
medScroll(f""" done""")
time.sleep(1)
os.system("cls")
sys.stdout.write(logo1)
time.sleep(1)
sys.stdout.write(logo2)
time.sleep(1)
sys.stdout.write(logo3)
time.sleep(1)
sys.stdout.write(logo4)
fastScroll(copyrights)
input()
pwinput.pwinput()
fastScroll(f"""\n""")
chatElipses(1)
medScroll(f"""Login successful.""")
time.sleep(1)
medScroll(f""" Welcome,""")
time.sleep(1)
medScroll(f""" LOTT_GUST!""")
time.sleep(1)
medScroll(f""" Press Enter to view your payment.\n""")
input()
os.system("cls")
medScroll(f"""Calculating payment""")
time.sleep(1)
elipses()
time.sleep(1)
medScroll(mission1)
time.sleep(1)
medScroll(mission2)
time.sleep(1)
medScroll(destination1)
time.sleep(1)
medScroll(destination2)
time.sleep(1)
medScroll(salary1)
time.sleep(1)
medScroll(salary2)
time.sleep(1)
medScroll(duration1)
time.sleep(1)
medScroll(duration2)
time.sleep(1)
medScroll(total1)
time.sleep(1)
medScroll(total2)
time.sleep(1)
medScroll(status1)
time.sleep(1)
slowScroll(status2)
time.sleep(1)
medScroll(payment)
input()
os.system("cls")
medScroll(f"""Estimating damages""")
time.sleep(1)
elipses()
time.sleep(1)
fastScroll(damagesHeader)
time.sleep(3)
medScroll(drone)
time.sleep(3)
medScroll(droneCost)
time.sleep(3)
medScroll(android)
time.sleep(3)
medScroll(androidCost)
time.sleep(3)
medScroll(personnel)
time.sleep(3)
medScroll(personnelCost)
time.sleep(3)
medScroll(facilities)
time.sleep(3)
medScroll(facilitiesCost)
time.sleep(3)
medScroll(equipment)
time.sleep(3)
medScroll(equipmentCost)
time.sleep(3)
medScroll(research)
time.sleep(3)
medScroll(researchCost)
time.sleep(3)
medScroll(profits)
time.sleep(3)
slowScroll(profitsCost)
time.sleep(3)
fastScroll(damagesFooter)
time.sleep(3)
slowScroll(estimated)
time.sleep(3)
countUp()
time.sleep(3)
slowScroll(estimatedCost)
time.sleep(3)
medScroll(accept)
input()
os.system("cls")
medScroll(f"""Establishing connection with The Board""")
time.sleep(1)
elipses()
time.sleep(1)
medScroll(f"""\nConnection successful""")
time.sleep(1)
fastScroll(f"""\n\n> """)
chatElipses(3)
medScroll(question11)
time.sleep(1)
medScroll(question12)
input()
fastScroll(f"""\n\n> """)
chatElipses(3)
medScroll(question21)
time.sleep(1)
medScroll(question22)
time.sleep(1)
medScroll(question23)
input()
fastScroll(f"""\n\n> """)
chatElipses(3)
medScroll(question3)
input()
fastScroll(f"""\n\n> """)
chatElipses(3)
medScroll(question4)
input()
fastScroll(f"""\n\n> """)
chatElipses(3)
medScroll(thanks1)
time.sleep(1)
medScroll(thanks2)
time.sleep(1)
medScroll(thanks3)
time.sleep(3)
medScroll(end)
input()
input()
time.sleep(5)
