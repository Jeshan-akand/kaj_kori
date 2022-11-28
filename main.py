col_off="\033[0m"         #Colour Off



##Blod

bblack="\033[1;30m"     #Black
bred="\033[1;31m"         #Red
bgreen="\033[1;32m"     #Green 
byellow="\033[1;33m"    #Yellow 
bblue="\033[1;34m"        #Blue
bpurple="\033[1;35m"    #purple
bcyan="\033[1;36m"       #Cyan
bwhite="\033[1;37m"      #White


##Normal
black="\033[0;30m"     #Black
red="\033[0;31m"         #Red
green="\033[0;32m"     #Green 
yellow="\033[0;33m"    #Yellow 
blue="\033[0;34m"        #Blue
purple="\033[0;35m"    #purple
cyan="\033[0;36m"       #Cyan
white="\033[0;37m"      #White
os_1=col_off+"["+bgreen+"1"+col_off+"]"
os_2=col_off+"["+bgreen+"2"+col_off+"]"
os_3=col_off+"["+bgreen+"3"+col_off+"]"
os_4=col_off+"["+bgreen+"4"+col_off+"]"
os_5=col_off+"["+bgreen+"5"+col_off+"]"
os_6=col_off+"["+bgreen+"6"+col_off+"]"
os_7=col_off+"["+bgreen+"7"+col_off+"]"
os_8=col_off+"["+bgreen+"8"+col_off+"]"
os_9=col_off+"["+bgreen+"9"+col_off+"]"
os_10=col_off+"["+bgreen+"10"+col_off+"]"
os_suc=col_off+"["+bgreen+"•••"+col_off+"]"
os_fail=col_off+"["+bred+"•••"+col_off+"]"
os_menu=col_off+"["+bgreen+">"+col_off+"]"
os_wrong=col_off+"["+bred+"×"+col_off+"]"
os_input=col_off+"["+bred+"•"+byellow+"•"+bgreen+"•"+col_off+"]"
os_line_clear="                                                                     "
os_tik=col_off+"["+bgreen+" ✓ "+col_off+"]"

os_line="－－－－－－－－－－－－－－－－－"

import requests
from requests.structures import CaseInsensitiveDict
import random,string,secrets,time,json,os

def file_check(path):
	try:
		r=open(path,"r")
		r.read()
	except:
		w=open(path,"w")
		w.write("xxx")

def claim_sleep_time(task_count,task_impression_time,task_click_time,self_time):
	total_time=int(task_impression_time)*2*int(task_count)+int(task_click_time)+self_time
	#print("Total_Time",total_time)
	return total_time


def view_task_claim(a_api,a_aid,visit_cpc):
	api=view_task_api
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/x-www-form-urlencoded"
	headers["User-Agent"] = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A307F Build/RP1A.200820.112)"
	headers["Host"] = host_link
	headers["Connection"] = "Keep-Alive"
	headers["Accept-Encoding"] = "gzip"
	data="android_amount="+visit_cpc+"&android_api="+a_api+"&android_id="+a_aid+"&android_type=Ad_click&"
	try:
		request_claim=requests.post(api,headers=headers,data=data)
		x_text=request_claim.text
		try:
			resp_json=json.loads(x_text)    #json praser 2:success 
			if resp_json["error"]==True:
				return True
			elif resp_json["error"]==False:
				message=resp_json["message"]
				message=message+" "
				message=message.strip(" ")
				return False,message
	             
		except:   #json praser 2: error
			return False,x_text	 
			
	except:
		print(os_line_clear,end="\r")
		print(os_fail+" Waiting For Internet Conection",end="\r")
             	
		
	
	

def visit_task_claim(a_api,a_id,visit_cpc):
    link={
  "1": "https://www.movietickets.com/",
  "2": "https://www.fandango.com/",
  "3": "https://www.amctheatres.com/",
  "4": "https://www.amctheatres.com/",
  "5": "https://www.cheapoair.com/",
  "6": "https://www.orbitz.com/",
  "7": "https://www.vayama.com/",
  "8": "https://search.lowfares.com/",
  "9": "https://www.dealbase.com/",
  "10": "https://www.officesupplynow.com/",
  "11": "https://www.officedepot.com/",
  "12": "http://www.poppin.com/",
  "13": "www.Officedepot.com/",
  "14": "https://www.wayfair.com/",
  "15": "www.Jossandmain.com/",
  "16": "https://www.concordsupplies.com/",
  "17": "https://www.lovinglane.com/",
  "18": "https://www.perigold.com/",
  "19": "https://www.gymboree.com/",
  "20": "https://www.tenthousandvillages.com/",
  "21": "www.Tenthousandvillages.com",
  "22": "https://www.craftonlineusa.com/",
  "23": "https://www.petsmart.com/",
  "24": "https://www.petco.com/",
  "25": "https://www.goatpetproducts.com/",
  "26": "https://www.goatpetproducts.com/",
  "27": "www.Entirelypets.com/",
  "28": "https://www.chewy.com/",
  "29": "https://www.entirelypets.com/",
  "30": "http://store.doverpublications.com/",
  "31": "https://thenewyorkdogshop.com/",
  "32": "https://www.barnesandnoble.com/",
  "33": "https://www.barnesandnoble.com/",
  "34": "https://www.booksamillion.com/",
  "35": "www.Store.doverpublications.com",
  "36": "https://www.booksamillion.com/",
  "37": "https://www.norimediagroup.com/",
  "38": "https://www.sportsunlimitedinc.com/",
  "39": "https://www.modells.com/",
  "40": "https://us.sportsdirect.com/",
  "41": "www.Onlinesports.com/",
  "42": "http://www.pleaselike.com/",
  "43": "http://www.wtfshouldidowithmylife.com/",
  "44": "https://puginarug.com/",
  "45": "https://alwaysjudgeabookbyitscover.com/",
  "46": "http://www.noon.com/",
  "47": "https://www.hectorsalamanca.com/",
  "48": "https://alwaysjudgeabookbyitscover.com/",
  "49": "http://www.noscam.com/",
  "50": "http://www.nothoot.com/",
  "51": "https://www.hectorsalamanca.com/",
  "52": "http://www.rrrgggbbb.com/",
  "53": "http://blue.eastsidelag.com/",
  "54": "https://fallingguy.com/",
  "55": "http://www.tacospin.com/",
  "56": "http://corndog.io/",
  "57": "https://www.zoomquilt.org/",
  "58": "https://www.zoomquilt.org/",
  "59": "https://readymaderesources.com/a-comprehensive-supply-list-for-economic-collapse/",
  "60": "https://jacksonpollock.org/",
  "61": "https://heeeeeeeey.com/",
  "62": "https://jacksonpollock.org/",
  "63": "https://heeey.com/",
  "64": "http://koalastothemax.com/",
  "65": "http://koalastothemax.com/",
  "66": "http://973-eht-namuh-973.com/",
  "67": "http://www.watchcount.com/",
  "68": "http://www.everydayim.com/",
  "69": "http://www.thebestdinosaur.com/",
  "70": "http://www.club100.org/",
  "71": "https://www.flightradar24.com/",
  "72": "https://dogeminer2.com/",
  "73": "https://doublebitpress.com/",
  "74": "http://www.computercollector.com/",
  "75": "https://www.asc.edu/",
  "76": "http://www.classiccmp.org/dunfield/",
  "77": "http://www.computercollector.com/",
  "78": "https://www.asc.edu/",
  "79": "http://www.classiccmp.org/dunfield/",
  "80": "https://ae27ff.meme.tips/register.php",
  "81": "https://hackaday.io/",
  "82": "https://usborne.com/browse-books/features/computer-and-coding-books/",
  "83": "http://websdr.ewi.utwente.nl:8901/",
  "84": "http://sbc.rictor.org/about.html",
  "85": "https://www.modells.com/",
  "86": "https://www.hide.me/",
  "87": "https://knife.com",
  "88": "https://hotvpn.com",
  "89": "https://host.com",
  "90": "https://findtheinvisiblecow.com/",
  "91": "https://www.mapcrunch.com/",
  "92": "https://theuselessweb.com/",
  "93": "http://hackertyper.com/",
  "94": "http://papertoilet.com/",
  "95": "http://newsoffuture.com/",
  "96": "https://pointerpointer.com/",
  "97": "http://beesbeesbees.com/",
  "98": "http://www.staggeringbeauty.com/",
  "99": "https://parade.com/1012420/nicolepajer/best-online-games/",
  "100": "http://www.shadyurl.com/",
  "101": "https://parade.com/984978/kelseypelzer/april-fools-pranks",
  "102": "https://archive.org/",
  "103": "http://dontevenreply.com/",
  "104": "https://stellarium-web.org/",
  "105": "http://www.shutupandtakemymoney.com/",
  "106": "https://parade.com/945826/kelseypelzer/best-stocking-stuffers/",
  "107": "https://parade.com/1300976/marynliles/gifts-for-men-who-have-everything/",
  "108": "https://play2048.co/",
  "109": "https://en.wikipedia.org/wiki/List_of_individual_dogs",
  "110": "https://paradepets.com/dogs/cutest-dog-breeds",
  "111": "https://zoomquilt.org/",
  "112": "http://www.drivemeinsane.com/",
  "113": "https://freerice.com/categories/english-vocabulary",
  "114": "https://apod.nasa.gov/apod/astropix.html",
  "115": "https://musclewiki.com/",
  "116": "https://musclewiki.com/",
  "117": "https://parade.com/1010737/samuelmurrian/best-shows-on-netflix/",
  "118": "https://www.duolingo.com/",
  "119": "https://www.duolingo.com/",
  "120": "https://www.internetlivestats.com/",
  "121": "https://parade.com/1173121/stephanieosmanski/slow-internet-reasons/",
  "122": "http://hubski.com/",
  "123": "https://thisissand.com/",
  "124": "https://lizardpoint.com/",
  "125": "http://radio.garden/search",
  "126": "http://radio.garden/search",
  "127": "https://www.musictheory.net/",
  "128": "https://parade.com/1239349/michelleparkerton/music-quotes/",
  "129": "https://radiooooo.com/",
  "130": "https://sleepyti.me/",
  "131": "https://trypap.com/",
  "132": "https://www.codecademy.com/",
  "133": "https://29a.ch/sandbox/2011/neonflames/#",
  "134": "https://explore.org/livecams/cats/kitten-rescue-cam",
  "135": "https://www.whatshouldireadnext.com/",
  "136": "https://myfridgefood.com/",
  "137": "https://www.onread.com/",
  "138": "https://www.omfgdogs.com/#",
  "139": "http://weavesilk.com/",
  "140": "https://parade.com/1157722/michellehaag/running-quotes/",
  "141": "https://parade.com/1018413/marynliles/things-to-do-when-bored/",
  "142": "https://eyebleach.me/",
  "143": "https://en.wikipedia.org/wiki/List_of_conspiracy_theories",
  "144": "http://sanger.dk/",
  "145": "https://pokemonshowdown.com/",
  "146": "https://www.sporcle.com/",
  "147": "https://www.poptropica.com/",
  "148": "https://koalabeast.com/",
  "149": "http://orteil.dashnet.org/cookieclicker/",
  "150": "https://parade.com/944248/parade/christmas-cookies/",
  "151": "https://habitica.com/static/front",
  "152": "http://www.foddy.net/2010/10/qwop/",
  "153": "http://www.flashbynight.com/",
  "154": "https://xkcd.com/",
  "155": "http://youarelistening.to/",
  "156": "https://www.incredibox.com/",
  "157": "https://asoftmurmur.com/",
  "158": "https://www.rainymood.com/",
  "159": "http://flashbynight.com/drench/",
  "160": "https://quickdraw.withgoogle.com/",
  "161": "https://www.dafont.com/",
  "162": "https://spacejam.com/",
  "163": "https://www.retailmenot.com/",
  "164": "https://www.mint.com/",
  "165": "https://tastedive.com/",
  "166": "https://www.addictivetips.com/",
  "167": "https://archive.org/details/msdos_Oregon_Trail_The_1990",
  "168": "https://www.instructables.com/",
  "169": "https://www.snopes.com/",
  "170": "http://themagicipod.com/",
  "171": "https://www.theonion.com/",
  "172": "https://lifehacker.com/",
  "173": "https://parade.com/1018413/marynliles/things-to-do-when-bored/",
  "174": "https://parade.com/1133959/parade/best-soup-recipes/",
  "175": "https://mix.com/",
  "176": "https://www.wizardingworld.com/",
  "177": "https://parade.com/955587/kelseypelzer/harry-potter-quotes/",
  "178": "https://codepen.io/akm2/full/rHIsa",
  "179": "https://www.lego.com/en-us/kids",
  "180": "https://parade.com/679441/samuelmurrian/we-ranked-all-five-jurassic-park-movies-including-jurassic-world-fallen-kingdom/",
  "181": "https://parade.com/393857/lharris-2/20-of-the-most-epic-star-wars-quotes-of-all-time/",
  "182": "https://www.ocearch.org/tracker/?list",
  "183": "https://www.ocearch.org/tracker/?list",
  "184": "https://parade.com/1043064/marynliles/texting-games/",
  "185": "https://parade.com/1364913/klconniewang/stars-not-leaving-hallmark-channel/",
  "186": "https://parade.com/celebrities/sam-heughan-sassenach-whisky-waypoints",
  "187": "https://parade.com/992609/roisinkelly/meghan-markle-net-worth/",
  "188": "https://parade.com/1364075/jessicasager/elon-musk-net-worth/",
  "189": "https://parade.com/news/drew-barrymore-madonna-halloween-costume-instagram-photos-2022",
  "190": "https://parade.com/1275071/meganoneill/best-fall-books/"

 }
	


    rand=random.randrange(1,86)
    link_x=link[str(rand)]
    ads_link=link_x+"?gclid=EAIaIQobC9jcu0-gJYavD_BwE"+secrets.token_hex(10)


    url = view_task_api
    
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["User-Agent"] = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A307F Build/RP1A.200820.112)"
    headers["Host"] = host_link
    headers["Connection"] = "Keep-Alive"
    headers["Accept-Encoding"] = "gzip"
    
    data = "android_amount="+str(visit_cpc)+"&android_api="+a_api+"&android_id="+a_id+"&android_type="+ads_link+""
    try:   #net connection check 1 :success
        
        resp = requests.post(url, headers=headers, data=data)
        x=resp.text
        
        try:
            resp_json=json.loads(x)    #json praser 2:success 
            if resp_json["error"]==True:
	            return True
            elif resp_json["error"]==False:
	             message=resp_json["message"]
	             message=message+" "
	             message=message.strip(" ")
	             return False,message
	             
	             
        except:   #json praser 2: error
             return False,x	 
        	   
    except:   #net connection check 1 :error 
             	print(os_line_clear,end="\r")
             	print(os_fail+" Waiting For Internet Conection",end="\r")
             	
             	
             	
             	

def visit_data(self_time):
	counter=0
	
	while True:
		print(os_line_clear,end="\r")
		print(os_suc+" Checking Task Database",end="\r")
		
		counter+=1
		url=visit_data_api
		
		headers = CaseInsensitiveDict()
		headers["Content-Type"] = "application/x-www-form-urlencoded"
		headers["User-Agent"] = "Dalvik/2.1.0 (Linux; U; Android 12; SM-A307F Build/RP1A.200820.112)"
		headers["Host"] = host_link
		headers["Connection"] = "Keep-Alive"
		headers["Accept-Encoding"] = "gzip"
		
		data="android_api=1234"
		
		try:
		
			resp = requests.post(url, headers=headers, data=data,timeout=5)
			x=resp.text
			resp_json=json.loads(x)
			
			visit_coin,task_ststus,ads_counter,ads_click_time,ads_impression_time=resp_json["android_video_amount"],resp_json["active_s"],resp_json["android_admin_video_imp"],resp_json["spin_13"],resp_json["android_unity"]
			claim_sleep_x=claim_sleep_time(ads_counter,ads_impression_time,ads_click_time,self_time)
			
			if task_ststus=="0":
				task_ststus_x="True"
			else:
				task_ststus_x="False"
			
			update_cheak_task_data(task_ststus_x,str(visit_coin),str(claim_sleep_x))   #update cheak
			#print("tttttttt")
			
			if task_ststus=="0":
				return visit_coin,claim_sleep_x
				break 
			elif task_ststus=="1":
				print(os_line_clear,end="\r")
				print(os_fail+" Task is OFF Now 😑 ",end="\r")
				time.sleep(5)
				print(os_line_clear,end="\r")
				pass
	
		except:
			time.sleep(0.5)
			print(os_line_clear,end="\r")
			print(os_fail+" No Internet Conection !",end="\r")
			time.sleep(3)
			

def remote_config():
	import requests,json
	counter=0
	
	
	while True:
		print(os_line_clear,end="\r")
		print(os_input+" Checking Server Updates ",end="\r")
		time.sleep(0.5)
		counter+=1
		all_account=[]
		try:
		
			request=requests.get(pastebin_api_link,timeout=10)
			
			request_x=request.text
			
			try:
				remote_data=json.loads(request.text)
				tool_status=remote_data["Tool_on"]
				claim_delay=remote_data["Delay"]
				my_account=remote_data["M_A"]
				guest_account=remote_data["G_A"]
				
			
			except:
				
				print(os_line_clear,end="\r")
				print(os_fail+" Something went Wrong in Database..",end="\r")
				time.sleep(5)
				message="🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨\n"+os_line+"\nProblems in Database Checkout Please.....\n\n"+os_line+"\n\n⚙ JSON     ➜\n\n"+request_x+"\n\n"+os_line+"\n#Problems"
				
				send_msg_on_telegram(message)
				sleep("Try Again After ",60)
				break
			
				
			
				
			
			for account in my_account:
			   account_data={
			   
			   "api":account["api"],
			   "aid":account["aid"],
			   "status":"personal"
			   
			   }
			   all_account.append(account_data)
		
			for account in guest_account:
				account_data_guest={
				"api":account["api"],
				"aid":account["aid"],
				"status":"guest"
				}
			    	
				all_account.append(account_data_guest)
				
		
		
			with open("status.img","w")as F:
				json.dump(all_account,F,indent=2)
			
					
			with open("status.img","r") as R:
				all_account=json.load(R)
				
			
			print(os_line_clear,end="\r")
			print(os_tik+" Update Successful",end="\r")
			time.sleep(.5)
			update_cheak_remote_config(str(tool_status),str(claim_delay),str(remote_data))
			#print("v        kkkkkkkkkk")
			if tool_status==True:
				return all_account,claim_delay
				break  
		
	
			elif tool_status==False:
				print(os_line_clear,end="\r")
				print(os_fail+" Script is OFF ",end="\r")
				time.sleep(5)
				pass
	
		except:
			print(os_line_clear,end="\r")
			print(os_fail+" No Internet Conection",end="\r")
			time.sleep(1)


def update_cheak_remote_config(tool_status,delay,json_text):
	file_check("remote.img")
	cheak=open("remote.img","r")
	old_data=cheak.readline()
	new_data=str(tool_status)+str(delay)
	if old_data!=new_data:
		update=update_time()
		time,date=update[0],update[1]
		print(os_line_clear,end="\r")
		if tool_status=="True":
			message="⋙══ ✅ Script Updated ✅ ══ ⋘\n"+os_line+" \n\n🟢 Script On        ➜  "+tool_status+"\n⏳ Claim Delay   ➜  "+str(delay)+" Seconds \n⏰ Update Time ➜  "+time+" ~ "+date+"\n\n"+os_line+"\n\n⚙ JSON     ➜\n\n"+json_text+"\n\n"+os_line+"\n#Script_update"
		else:
			message="⋙══ ✅ Script Updated ✅ ══ ⋘\n"+os_line+" \n\n🔴 Script On        ➜  "+tool_status+"\n⏳ Claim Delay   ➜  "+str(delay)+" Seconds \n⏰ Update Time ➜  "+time+" ~ "+date+"\n\n"+os_line+"\n\n⚙ JSON     ➜\n\n"+json_text+"\n\n"+os_line+"\n#Script_update"
		
			
		send_msg_on_telegram(message)
		
		print(os_line_clear,end="\r")
		print(os_suc+bcyan+" Updated Script :\n\t\t   "+os_1+bcyan+" Script On   : "+tool_status+"\n\t\t   "+os_2+bcyan+" Claim Delay : "+str(delay)+" Seconds \n\t\t   "+os_3+bcyan+" Update Time : "+time+" ~ "+date+" ",end="\n\n")
		
		update=open("remote.img","w")
		update.write(new_data)
		
		
def update_cheak_task_data(task_status,visit_cpc,visit_delay):
	file_check("task.img")
	cheak=open("task.img","r")
	old_data=cheak.readline()
	new_data=str(task_status)+str(visit_cpc)+str(visit_delay)
	if old_data!=new_data:
		update_time_date=update_time()
		time,date=update_time_date[0],update_time_date[1]
		if task_status=="True":
			message="⋙══ ✅ Task Updated ✅ ══ ⋘--\n"+os_line+" \n\n🟢 Task On         ➜  "+str(task_status)+"\n💰 Claim Point   ➜  "+str(visit_cpc)+" points\n⏳ Claim Sleep   ➜  "+str(visit_delay)+" seconds\n⏰ Update Time ➜  "+time+" ~ "+date+"\n\n"+os_line+"\n\n#Task_update"
		else:
			message="⋙══ ✅ Task Updated ✅ ══ ⋘--\n"+os_line+" \n\n🔴 Task On         ➜  "+str(task_status)+"\n💰 Claim Point   ➜  "+str(visit_cpc)+" points\n⏳ Claim Sleep   ➜  "+str(visit_delay)+" seconds\n⏰ Update Time ➜  "+time+" ~ "+date+"\n\n"+os_line+"\n\n#Task_update"
		
		send_msg_on_telegram(message)
		print(os_line_clear,end="\r")
		print(os_suc+bcyan+" Updated Task :\n\t\t   "+os_1+bcyan+" Task On     : "+task_status+"\n\t\t   "+os_2+bcyan+" Claim Point : "+str(visit_cpc)+" points \n\t\t   "+os_3+bcyan+" Claim Sleep : "+str(visit_delay)+" seconds \n\t\t   "+os_4+bcyan+" Update Time : "+time+" ~ "+date+" ",end="\n\n")
		
		update=open("task.img","w")
		update.write(new_data)		

def sleep(text,time):
	import time as ghoom
	time=time
	while time>0:
		print(os_suc+text+bgreen+str(time-1)+col_off+" seconds",end="\r")
		
		time-=1
		ghoom.sleep(1)
		print(os_line_clear,end="\r")
        				
def update_time():
    from datetime import datetime, timedelta
    import time
    import pytz

    IST = pytz.timezone('Asia/Dhaka')   
    today_date = datetime.now(IST).strftime("%d-%m-%Y") #Current Date
    curr_time = datetime.now(IST).strftime("%H:%M:%S")   #Current time
    if datetime.now(IST).strftime("%H")<"12":
    	curr_time=curr_time+" AM"
    else:
    	curr_hour=int(datetime.now(IST).strftime("%H"))-12
    	curr_min=datetime.now(IST).strftime("%M")
    	curr_sec=datetime.now(IST).strftime("%S")
    	curr_time=str(curr_hour)+":"+curr_min+":"+curr_sec
    	curr_time=curr_time+" PM"
    return curr_time,today_date		


def send_msg_on_telegram(msg):
    	while True:
    		print(os_line_clear,end="\r")
    		print(os_suc+" Conecting With Telegram",end="\r")
    		telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
    		try:
    			
    			tel_resp = requests.get(telegram_api_url,timeout=7)
    			if tel_resp.status_code == 200:
    				print(os_line_clear,end="\r")
    				print (os_tik+" Notification has been sent on Telegram",end="\r")
    				time.sleep(0.4)
    				break
    			else:
    				print(os_line_clear,end="\r")
    				print(os_fail+" Could not send Message",end="\r")
    				time.sleep(0.5)
    				break
    		except:
    			print(os_line_clear,end="\r")
    			print(os_fail+" No Internet Conection ",end="\r")
    			
    			time.sleep(1)
    	
    			
def github_update(version):
	import os
	print(os_line_clear,end="\r")
	try:
		print(os_input+" Checking Script Updates ",end="\r")
		requestx=requests.get("https://raw.githubusercontent.com/Jeshan-akand/kaj_kori/main/version.json").text
		request_json=json.loads(requestx)
		latest_update=int(request_json["version"])
		if version < latest_update:
			print(os_line_clear,end="\r")
			print(os_menu+" Update Found !...Please Wait Script Updating...",end="\r")
			time.sleep(1)
			#os.system("pkg install git && git clone https://github.com/Jeshan-akand/kaj_kori")
			os.system("rm -rf $HOME/kaj_kori && pkg update -y && pkg upgrade -u && pkg install python -y && pkg install git -y && cd $HOME && git clone https://github.com/Jeshan-akand/kaj_kori && python bot.py")
		else:
				print(os_line_clear,end="\r")
				print(os_tik+" Script Already Up-To-Date ",end="\r")
				time.sleep(0.4)
	except:
			print(os_line_clear,end="\r")
			print(os_fail+" No Internet Conection ",end="\r")
			time.sleep(1)
    	
				


def banner():
    os_tag="["+bgreen+"•••"+col_off+"]"
    
    
    os.system("clear")
    
    logo=bgreen+"""
      /$$$$$ /$$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$   /$$
     |__  $$| $$_____/ /$$__  $$| $$  | $$ /$$__  $$| $$$ | $$
        | $$| $$      | $$  \__/| $$  | $$| $$  \ $$| $$$$| $$
        | $$| $$$$$   |  $$$$$$ | $$$$$$$$| $$$$$$$$| $$ $$ $$
   /$$  | $$| $$__/    \____  $$| $$__  $$| $$__  $$| $$  $$$$
  | $$  | $$| $$       /$$  \ $$| $$  | $$| $$  | $$| $$\  $$$
  |  $$$$$$/| $$$$$$$$|  $$$$$$/| $$  | $$| $$  | $$| $$ \  $$
   \______/ |________/ \______/ |__/  |__/|__/  |__/|__/  \__/
                                                            
                                                            
     """+col_off
    sry_xx_ver="\n"+os_input+bcyan+" Script Version     :"" 4.0.X"
    sry_f_nam="\n"+os_input+bcyan+" Script Name        :"" Home Earn Task Auto Claim"
    sry_f_bran="\n"+os_input+bcyan+" Script Owner       :"" Jeshan Akand"
    line=bgreen+"\n==============================================================="+col_off
    print(logo,sry_f_bran,sry_f_nam,sry_xx_ver)
    print(line)
    print()
    
    
    
    
def main():
		#amount=int(input(os_input+" Enter Claim Amount : "+bgreen))
		
		#print("\n")    #calim amount
		banner()
		counter_guest=0
		sleep(" Script Run After ",5)
		
		for j in range(999999999999999999999999999999):   #claim loop
	#		github_update(1)
			remote_data=remote_config()    #remote data Function 
			account_list,self_sleep_time=remote_data[0],remote_data[1]   #remote data variables 
			visit_data_status=visit_data(self_sleep_time)  # visit data Function & Variable			
			visit_coin,claim_sleep=visit_data_status[0],visit_data_status[1]
			for account in account_list:  # calim account list
				api,aid,status=account["api"],account["aid"],account["status"]  #prase json account list
				if status=="guest":   #cheak if guest or not  for hide my account clam
					print(os_line_clear,end="\r")
					print(os_suc+" Trying To Claim Task",end="\r")
				vist_status=view_task_claim(api,aid,visit_coin)   #claim visit @@@@@
				
				
				if status=="guest":   #cheak if guest or not for print success or error 
					time_update=update_time()
					curr_time,curr_date=time_update[0],time_update[1]
					counter_guest+=1 #print counter for guest
					try:	   #for Internet Connection Errors...
							
							if vist_status==True and status=="guest": #cheak if Claim success 
								
								#balance,message=response[0],response[1]
								
								print(os_line_clear,end="\r")
								print("["+bgreen+str(counter_guest)+col_off+"] Claim Successful : "+str(visit_coin)+" Points Added"+"   "+curr_time+" ~ "+curr_date)   #print success message 
							
							else:
								message=vist_status[1]
								print(os_line_clear,end="\r")
								print("["+bred+str(counter_guest)+col_off+"] Claim failed : "+message+"   "+curr_time+" ~ "+curr_date)  #print error message
								
					except:
						print(os_line_clear,end="\r")
						print("["+bred+str(counter_guest)+col_off+"] Claim failed : No internet connection ..")
						while True:
							try:
								requests.get("https://google.com",timeout=7)
								break
							except:
										print(os_fail+" No Internet Conection",end="\r")
										

																								

			sleep(" Please wait 🙃 Next Claim After ",claim_sleep)
#		time loop
#		remote data
#        task data
#        visit claim
#        main
tele_auth_token = "5347927222:AAEOYRIQkGkHwKOQIY8Jl3wmxWa6SQsNg1k" # Authentication token provided by Telegram bottel_
tel_group_id = "xome_earn" 


pastebin_api_link="https://pastebin.com/raw/Fph58pze"

host_link="clipow.com"
app_name="home_earn"



api_x="https://"+host_link+"/"+app_name+""
visit_data_api=""+api_x+"/android/admin_get_url.php"
view_task_api = ""+api_x+"/android/bonus_point.php"
visit_task_api=""+api_x+"android/web_point.php"
#print(api_x,visit_data_api,view_task_api)


main()