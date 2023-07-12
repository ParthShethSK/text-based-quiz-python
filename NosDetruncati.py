import time
import sys
from colorama import init, Style, Fore, Back
def Intro():
	str1="Salve"
	str2="This is the"
	str8="NOS DETRUNCATI"
	str3="\"Fata volentem ducunt, nolentem trahunt\""
	str4="it means Fate leads the willing, and drags the unwilling"
	str5="Will you be lead into or dragged away"
	str6="May the fate be with you"
	str7="We believe in"
	init()
	print(Fore.CYAN)
	print(Back.BLACK)
	print('\033[1m'+ str1.center(125,' ')+'\033[0m')
	time.sleep(3)
	print(Fore.CYAN)
	print('\033[1m'+"\n\n"+str2.center(125,' ')+'\033[0m')
	time.sleep(3)
	print(Fore.CYAN)
	print('\033[1m'+'\x1B[3m' +str8.center(125,' ')+ '\x1B[0m'+'\033[0m')
	time.sleep(5)
	print(Fore.GREEN)
	print("\n\nWe are a hacking organization\nWe have been monitoring your activity and the system has" )
	time.sleep(3)
	print("\nidentified you to be a promising candidate\nfor inclusion in our group but")
	time.sleep(3)
	print("\nyou will have to pass this test for it")
	time.sleep(3)
	print("\n\nYou can close this terminal anytime and forget about it\nWe will be more than happy")
	time.sleep(3)
	print("\n\nBut if you continue be prepared for 3 sets of questions\nEach question will have 4 options A B C D")
	time.sleep(4)
	print("\nEach choice has a consequence if correct good for you but if wrong....")
	time.sleep(3)
	print("\nYou will be given 6 chances to correct any mistake\n3 in the first stage, 2 in the second stage, 1 for the last stage")
	time.sleep(6)
	print("\n\nBefore you start one thing you need to know")
	print("\n"+str7.center(125,' '))
	time.sleep(4)
	print('\033[1m'+"\n"+'\x1B[3m' +str3.center(125,' ')+ '\x1B[0m'+'\033[0m')
	time.sleep(5)
	print("\n"+str4.center(125,' '))
	time.sleep(4)
	print("\n"+str5.center(125,' '))
	time.sleep(4)
	print("\n"+str6.center(125,' '))
	time.sleep(5)
def Level1():
	ctr=0
	print(Fore.CYAN)
	print(Back.BLACK)
	str1="SCAENA UNUS"
	questions=["Question 1 : How can you reduce the chance of being hacked?","Question 2 : What is the attack called 'evil twin'?","Question 3 : What is max length of an SSID?","Question 4 : Which wireless mode connects machines directly to one another, without the use of an access point?"]
	options=[["A : Use VPN","B : Have Firewalls","C : Use different encrypted passwords","D : All of the above"],["A : MAC Spoofing","B : ARP Poisoning","C : Rogue Access Point","D : Session Hijacking"],["A : 8 Characters","B : 16 Characters","C : 32 Characters","D : 64 Characters"],["A : Point to Point","B : Infrastructure","C : Ad hoc","D : ESS"]]
	answers=["D","C","C","C"]
	print('\033[1m'+"\n\n\n"+str1.center(125,' ')+'\033[0m')
	print(Fore.GREEN)
	time.sleep(4)
	for i in range(0,4):
		while(ctr!=5):
			print("\n"+questions[i]+"\n"+options[i][0]+"\n"+options[i][1]+"\n"+options[i][2]+"\n"+options[i][3]+"\n")
			ans=input("Enter your choice : ")
			if (ans==answers[i]):
				break;
			else:
				ctr+=1;
				if(ctr==1):
					print("\nFirst Blood! Don't spill more")
					time.sleep(2)
					print("2 lives left for this stage\n")
					time.sleep(3)
				elif(ctr==2):
					print("\nAnother Wrong Answer")
					time.sleep(2)
					print("You can always google, surely we can't see. Last life\n")
					time.sleep(3)
				elif(ctr==3):
					print("Be Careful, no more lives left!")
					time.sleep(2)
					print("Wouldn't want to lose in first round itself\n")
					time.sleep(3)
				else:
					Ending(1)
	print("\nPretty easy stuff right?\n",ctr," lives used\n")
	time.sleep(3)
	return ctr
def Level2(ctr):
	ctr1=0
	print(Fore.CYAN)
	print(Back.BLACK)
	str1="SCAENA DUO"
	questions=["Question 1 : Which of the fall is a passive wireles discovery Tod?","Question 2 : Which tool can be used to perform a DNS zone transfer on Windows?","Question 3 : Which is correct bettercap command?","Question 4 : Which one of the following allows client to update their DNS entry as their IP address change?"]
	options=[["A : Net Stumbler","B : Aircrack","C : kismet","D : Netsniff"],["A : DNSlookup","B : nslookup","C : whois","D : ipconfig"],["A : Bettercap iface ethO","B : Bettercap -iface ethO","C : Bettercap-caplet automate.cap","D : Bettercap caplet automate.cap"],["A : dynamic DNS","B : authoritative name server","C : mail transfer agent","D : none of the above"]]
	answers=["C","B","B","A"]
	print('\033[1m'+"\n\n\n"+str1.center(125,' ')+'\033[0m')
	print(Fore.GREEN)
	time.sleep(4)
	for i in range(0,4):
		while(ctr1!=4):
			print("\n"+questions[i]+"\n"+options[i][0]+"\n"+options[i][1]+"\n"+options[i][2]+"\n"+options[i][3]+"\n")
			ans=input("Enter your choice : ")
			if(ans==answers[i]):
				break;
			else:
				ctr+=1;
				ctr1+=1;
				if(ctr1==1):
					print("\nOne More Wrong Answer")
					time.sleep(2)
					print("One More Life Lost")
					time.sleep(2)
					print("One More Life Left\n")
					time.sleep(3)
				elif(ctr1==2):
					print("\nNo succesful candidate has ever used 5 lives!")
					time.sleep(2)
					print("is Fate with you my friend\n")
					time.sleep(3)
				else:
					Ending(1)
	print("\n",ctr," lives used! Consequences or No Consequences\n")
	time.sleep(3)
	return ctr
def Level3(ctr):
	ctr1=0
	print(Fore.CYAN)
	print(Back.BLACK)
	str1="ULTIMA SCAENA"
	str2="EXTREMUM FATO"
	questions=["Question 1 : Which of the following takes advantage of weakness in the fragment reassembly functionality of TCP/IP?","Question 2 : What provides for both authetication and confidentiality in IPSec?","Question 3 : Which of the followiny is an effective deterrent against TCP session hijacking?","Question 4 : After performing ______ the ethical hacker should never disclose client information to other parties","Question 5 : A _____ is essentially a text file residing on the server that hosts different domain containing entries for dissimilar resource records","Question 6 : Entering Password::blah' or 1=1- into a web form in order to get a password is an example of what type of attack","Question 7 : Replacing NOPs with other code in a buffer-overflow mutation serves what purpose?","Question 8 : Which is also termed as DNS spoofing, is a kind of attack which uses DNS based vulnerabilities for diverting the traffic of the internet?","Last Question : What was the first question (Scroll up by all means, who's watching your screen anyways)"]
	options=[["A : Teardrop","B : SYN flood attack","C : smurf attack","D : Ping of death"],["A : AH","B : IKE","C : DAKLEY","D : ESP"],["A : Install and use an HIPS on the system","B : Install and use Tripwire on the system","C : Enforce good password policy","D : Use unpredictable sequence numbers"],["A : Information Gathering","B : Cracking","C : Pentesting","D : Exploiting"],["A : Zone file","B : Robot file","C : Bot file","D : DNS file"],["A : Buffer overflow","B : Heap-based overflow","C : Stack-based overflow","D : SQL injection"], ["A : Bypassing an IDS","B : Overwriting the return pointer","C : Advancing the return pointer","D : Bypassing a firewall"] , ["A : DNS poisoning","B : DNS re-routing","C : DNS cracking","D : Domain link poisoning"] , ["A : What are safe practices to followed to avoid being hacked?","B : How can you reduce the chance of being hacked?","C : Both A and B","D : None of the above"]]
	answers=["A","D","D","C","A","D","A","A","B"]
	print('\033[1m'+"\n\n\n"+str1.center(125,' ')+'\033[0m')
	print(Fore.GREEN)
	time.sleep(6)
	for i in range(0,ctr+3):
		while(True):
			print("\n"+questions[i]+"\n"+options[i][0]+"\n"+options[i][1]+"\n"+options[i][2]+"\n"+options[i][3]+"\n")
			ans=input("Enter your choice : ")
			if(ans==answers[i]):
				break;
			else:
				ctr1+=1;
				if(ctr1==1):
					print(Fore.CYAN)
					print('\033[1m'+"\n\n"+str2.center(125,' ')+'\033[0m')
					time.sleep(3)
					print(Fore.GREEN)
				else:
					Ending(1)
	while(True):
		print("\n"+questions[8]+"\n"+options[8][0]+"\n"+options[8][1]+"\n"+options[8][2]+"\n"+options[8][3]+"\n")
		ans=input("Enter your choice : ")
		if(ans==answers[8]):
			break;
		else:
			ctr1+=1;
			if(ctr1==1):
				print(Fore.CYAN)
				print('\033[1m'+"\n\n"+str2.center(125,' ')+'\033[0m')
				time.sleep(3)
				print(Fore.GREEN)
			else:
				Ending(1)
def Ending(check):
	str1="Bene Factum"
	str2="Fate is leading you, we will contact you at 0300, once we verify your test results"
	str3="Vide Te Mox"
	str4="Eheu!"
	str5="Fate is dragging you but remember"
	str6="Natura nihil frustra facit"
	time.sleep(6)
	if(check==0):
		print(Fore.CYAN)
		print('\033[1m'+"\n\n"+str1.center(125,' ')+'\033[0m')
		time.sleep(3)
		print(Fore.CYAN)
		print('\033[1m'+str2.center(125,' ')+'\033[0m')
		time.sleep(3)
		print(Fore.CYAN)
		print('\033[1m'+str3.center(125,' ')+'\033[0m')
	else:
		print(Fore.CYAN)
		print('\033[1m'+"\n\n"+str4.center(125,' ')+'\033[0m')
		time.sleep(3)
		print(Fore.CYAN)
		print('\033[1m'+str5.center(125,' ')+'\033[0m')
		time.sleep(3)
		print(Fore.CYAN)
		print('\033[1m'+str6.center(125,' ')+'\033[0m')
	sys.exit()
def main():
	Intro()
	ctr=Level1()
	ctr=Level2(ctr)
	Level3(ctr)
	Ending(0)
main()
