import random,string,requests,os
from pystyle import Colors,Colorate
import time,sys
def ngl():
i='[3] ';h='[2] ';g='[1] ';V=True;H=' ';M='[-] ';L='[✦] ';G='';C='═';J='\x1b[1;31m';Q='\x1b[1;32m';F='\x1b[1;33m';Z='\x1b[1;34m';A='\x1b[1;35m';a='\x1b[1;36m';B='\x1b[0m'
def O():os.system('clear')
def I():
try:return os.get_terminal_size().columns
except:return 80
def c():A=string.ascii_lowercase+string.digits;B=G.join(random.choices(A,k=8));C=G.join(random.choices(A,k=4));D=G.join(random.choices(A,k=4));E=G.join(random.choices(A,k=4));F=G.join(random.choices(A,k=12));H=f"{B}-{C}-{D}-{E}-{F}";return H
def d():
try:
with open('user-agents.txt','r')as A:B=A.readlines();return random.choice(B).strip()
except:return random.choice(['Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'])
def e():return random.choice(['😀','😃','😄','😁','😆','😅','😂','🤣','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨','🧐','🤓','😎','🤩','🥳','😏','😒','😞','😔','😟','😕','🙁','☹️','😣','😖','😫','😩','🥺','😢','😭','😤','😠','😡','🤬','🤯','😳','🥵','🥶','😱','😨','😰','😥','😓','🤗','🤔','🤭','🤫','🤥','😶','😐','😑','😬','🙄','😯','😦','😧','😮','😲','🥱','😴','🤤','😪','😵','🤐','🥴','🤢','🤮','🤧','😷','🤒','🤕','🤑','🤠'])
def S(iteration,total,prefix=G,suffix=G,length=40):
E=length;D=total;C=iteration;G=100*(C/float(D));H=int(EC//D);J='█'H+'░'(E-H)
if G==100:I='100%'
else:I=f"{G:.1f}%"
print(f"\r{A}{prefix} |{Q}{J}{A}| {F}{I}{A} {suffix}{B}",end='\r')
if C==D:print()
def P(text,color=A):C=color;E=I();A=min(E-4,len(text)+4);D=(E-A)//2;print(HD+C+'┌'+'─'(A-2)+'┐'+B);print(HD+C+'│'+text.center(A-2)+'│'+B);print(HD+C+'└'+'─'(A-2)+'┘'+B)
def E(text,color=A):A=I();C=(A-len(text))//2;print(HC+color+text+B)
def D(char=C,color=A):A=I();print(color+charA+B)
def R(text='Loading',duration=1):
D=['⠋','⠙','⠹','⠸','⠼','⠴','⠦','⠧','⠇','⠏'];C=time.time()+duration
while time.time()<C:
for E in D:
if time.time()>=C:break
print(f"\r{A}[{E}]{B} {text}...",end=G);time.sleep(.05)
print(f"\r{A}[✓]{B} {text} completed!")
def T():
A=['⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⣾⣿⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⣿⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠻⠷⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⢀⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⣠⠏⠀⠀⠀⣀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⡆⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠁⠀⠀⣰⢛⣥⣤⣤⣀⠉⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣀⢀⣤⠶⠚⠛⠉⠉⠉⠛⠛⠲⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⣤⣀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⣤⣟⣿⣷⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⡀⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀','⢠⣄⣀⡈⢛⣿⣿⡿⠋⡠⣴⣿⠋⠉⠙⠻⣷⡌⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⣹⣿⣿⡿⢿⣿⣿⡿⠛⠛⠛⠿⣿⣿⣿⣷⣦⣾⠿⢧⡀⠀⡀⠀⠀⠀','⠀⠉⠻⠿⢿⣿⣿⢣⠎⢠⣿⠁⠀⠀⠀⢀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⣿⠝⣳⣿⡿⠃⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣶⣶⡷⣞⠁⠀⠀⠀','⠀⠀⠀⠀⠈⣿⡏⡆⠀⢸⡇⠀⠀⠀⢀⣾⠋⣻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠋⠀⠃⠀⣿⣿⠃⠀⠀⠀⠀⠀⢀⣼⠟⠻⣿⣿⢿⣿⣿⣶⣤⣀⣀⠀⠀','⠀⠀⠀⠀⠀⠘⣿⡅⠀⢸⣷⡀⢀⣴⣿⠟⠛⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⢀⣤⣿⣿⣶⣾⣿⣿⠈⢻⣿⡿⠛⠛⠛⠛⠉','⠀⠀⠀⠀⠀⠀⠘⢧⠀⠘⣿⣿⣿⣿⠃⠀⠀⣼⢿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣦⣤⣤⣶⣿⡟⠁⠀⠀⣿⢿⡟⠀⠸⣿⣷⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠹⠁⠙⣿⣷⣤⡾⡟⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡟⠙⢻⣿⡿⢿⠀⠀⢀⣴⠻⣾⠇⠀⢸⠏⠹⣆⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⡴⠶⢾⣅⣠⣥⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⡀⣸⣿⠤⠈⣶⣖⣹⣿⡾⠃⢀⠰⠋⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣷⣿⣤⣌⡿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣾⡷⠞⢛⠻⣿⠿⢒⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠻⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣷⣷⣮⣭⣭⠿⠖⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠘⠋⠉⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'];C=I();B=max(len(A)for A in A)
if C<B:A=['⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⠃⠀⠀⠀⠀⠈⢿⣷⣦⣤⣄⣀⠀⠀⠀⠀⠀⠀','⠀⠀⢀⣤⣴⣾⣿⠿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⣿⣿⣶⣦⣤⣄⡀','⠀⢀⣴⡾⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠻⠷⣶⣄','⢀⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠷⣦','⣠⠏⠀⠀⠀⣀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⡆','⠁⠀⠀⣰⢛⣥⣤⣤⣀⠉⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣀⢀⣤⠶⠚⠛⠉⠉⠛⠛⠲⢤','⣤⣀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⣤⣟⣿⣷⣿⣿⣿⣿⣿⣿⣷⣦','⢠⣄⣀⡈⢛⣿⣿⡿⠋⡠⣴⣿⠋⠉⠙⠻⣷⡌⢳⡀⠀⠀⠀⠀⠀⠀⠜⣹⣿⣿⡿⢿⣿⣿⡿⠛⠛⠛⠿⣿⣿⣿⣷','⠀⠉⠻⠿⢿⣿⣿⢣⠎⢠⣿⠁⠀⠀⠀⢀⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⣼⡿⣿⠝⣳⣿⡿⠃⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿','⠀⠀⠀⠀⠈⣿⡏⡆⠀⢸⡇⠀⠀⠀⢀⣾⠋⣻⣷⠀⠀⠀⠀⠀⠀⠠⠋⠀⠃⠀⣿⣿⠃⠀⠀⠀⠀⠀⢀⣼⠟⠻⣿⣿⢿⣿','⠀⠀⠀⠀⠀⠘⣿⡅⠀⢸⣷⡀⢀⣴⣿⠟⠛⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⢀⣤⣿⣿⣶⣾⣿⣿⠈⢻⣿','⠀⠀⠀⠀⠀⠀⠘⢧⠀⠘⣿⣿⣿⣿⠃⠀⠀⣼⢿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣦⣤⣤⣶⣿⡟⠁⠀⠀⣿⢿⡟⠀⠸⣿','⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠹⠁⠙⣿⣷⣤⡾⡟⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡟⠙⢻⣿⡿⢿⠀⠀⢀⣴⠻⣾⠇⠀⢸⠏','⠀⠀⠀⠀⠀⠀⠀⠀⠀⣡⡴⠶⢾⣅⣠⣥⣶⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⡀⣸⣿⠤⠈⣶⣖⣹⣿⡾⠃⢀⠰⠋⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣷⣿⣤⣌⡿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣾⡷⠞⢛⠻⣿⠿⢒⣾⡿⠃⠀⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠻⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣷⣷⣮⣭⣭⠿⠖⠛⠉⠀⠀','⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠘⠋⠉⠘⠁⠀⠀⠀⠀⠀⠀⠀'];B=max(len(A)for A in A)
D=(C-B)//2
for E in A:print(HD+Colorate.Horizontal(Colors.red_to_purple,E))
def U():B='✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦ ✦';O();T();D(C,A);E(B,F);P('NGL SPAM TOOL V1.0 - PINK EDITION',A);E(B,F);D(C,A);E('CREATED BY NANAW',F);D(C,A)
def N():D(C,A);E('✦ TOOLS INFORMATION ✦',F);D(C,A);print(A+'This tool allows you to send anonymous messages to NGL users'+B);print(A+'with different spam modes and customizable options.'+B);D(C,A);E('✦ AVAILABLE FEATURES ✦',F);D(C,A);print(A+'• Multiple spam modes with different speeds'+B);print(A+'• Random emoji for each message'+B);print(A+'• Session logging to history file'+B);print(A+'• Device ID rotation for better anonymity'+B);D(C,A);E('✦ DISCLAIMER ✦',F);D(C,A);print(A+'This tool is for educational purposes only.'+B);print(A+"Spam your girlfriend if she doesn't reply to your chat"+B);D(C,A)
def W():D(C,A);E('✦ MAIN MENU ✦',F);D(C,A);print(A+g+B+'Start Spam');print(A+h+B+'View Information');print(A+i+B+'Exit');D(C,A);G=input(A+L+B+'Choose option (1/2/3): ');return G
def X():
o='[✗] ';n='Complete';m='[!] ';l='Invalid input! Please enter a number.';b='%H:%M:%S';a=False;T='Progress:';U();D(C,A);E('✦ SELECT SPAM MODE ✦',F);D(C,A);print(A+g+B+'Normal Spam (1.0s delay)');print(A+h+B+'Fast Spam (0.5s delay)');print(A+i+B+'Brutal Spam (0.1s delay)');print(A+'[4] '+B+'Super Brutal Spam (0.01s delay)');print(A+'[5] '+B+'Ultra Super Brutal Spam (0.0s delay)');print(A+'[6] '+B+'Custom Mode');print(A+'[0] '+B+'Back to Main Menu');D(C,A);N=input(A+L+B+'Choose mode (1/2/3/4/5/6/0): ')
if N=='0':return a
if N=='1':K=1.;O='Normal'
elif N=='2':K=.5;O='Fast'
elif N=='3':K=.1;O='Brutal'
elif N=='4':K=.01;O='Super Brutal'
elif N=='5':K=.0;O='Ultra Super Brutal'
elif N=='6':
O='Custom'
while V:
p=input(A+L+B+'Enter custom delay (in seconds): ')
try:
K=float(p)
if K<0:print(J+M+B+'Delay cannot be negative!');continue
break
except ValueError:print(J+M+B+l)
else:print(J+M+B+'Invalid mode selected!');time.sleep(2);return a
R('Initializing spam mode');D(C,A);E(f"✦ {O.upper()} MODE SELECTED ✦",F);D(C,A);time.sleep(1);X=input(A+L+B+'Target Username: ');Y=input(A+L+B+'Message: ')
while V:
j=input(A+L+B+'Number of messages: ')
if j.strip()==G:print(J+M+B+'Please enter a valid number!');continue
try:
H=int(j)
if H<=0:print(J+M+B+'Please enter a positive number!');continue
break
except ValueError:print(J+M+B+l)
D(C,A);E('✦ MESSAGE PREVIEW ✦',F);D(C,A);E(f"{Y} {e()}",Q);D(C,A);q=input(A+'[?] '+B+'Start sending messages? (y/n): ').lower()
if q!='y':print(A+m+B+'Operation cancelled.');time.sleep(1);return a
R('Preparing to send messages');D(C,A);E('✦ STARTING SPAM ✦',F);D(C,A);print();P=0;W=0;S(0,H,prefix=T,suffix='Starting...')
with open('history.txt','a')as I:
I.write(f"\n\n=== NGL SPAM SESSION - {time.strftime("%Y-%m-%d %H:%M:%S")} ===\n");I.write(f"User: {f}\n");I.write(f"Mode: {O}\n");I.write(f"Target: {X}\n");I.write(f"Message: {Y}\n");I.write(f"Count: {H}\n");I.write(f"Delay: {K}\n\n")
while P<H:
r={'Host':'ngl.link','sec-ch-ua':'"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"','accept':'/*','content-type':'application/x-www-form-urlencoded; charset=UTF-8','x-requested-with':'XMLHttpRequest','sec-ch-ua-mobile':'?0','user-agent':d(),'sec-ch-ua-platform':'"Linux"','origin':'https://ngl.link','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':f"https://ngl.link/{X}",'accept-language':'en-US,en;q=0.9'};Z=f"{Y} {e()}";s={'username':X,'question':Z,'deviceId':c(),'gameSlug':G,'referrer':G}
try:
t=requests.post('https://ngl.link/api/submit',headers=r,data=s)
if t.status_code==200:W=0;P+=1;S(P,H,prefix=T,suffix=n);print();print(Q+'[✓] '+B+f"Sent: {P}/{H} -> {Z}");I.write(f"[{time.strftime(b)}] Sent: {Z}\n")
else:W+=1;S(P,H,prefix=T,suffix='Failed');print();print(J+o+B+'Failed to send');I.write(f"[{time.strftime(b)}] Failed to send\n")
if W==4:print(F+m+B+'Changing device information');c();d();W=0
time.sleep(K)
except Exception as k:S(P,H,prefix=T,suffix='Error');print();print(J+o+B+f"Error: {str(k)}");I.write(f"[{time.strftime(b)}] Error: {str(k)}\n");time.sleep(K)
S(H,H,prefix=T,suffix=n);print();D(C,A);E('✦ SPAM COMPLETED ✦',Q);E(f"✦ {P} MESSAGES SENT ✦",Q);E('✦ LOGGED TO HISTORY ✦',Q);D(C,A);time.sleep(3);return V
def Y():G='[+] ';D(C,A);E('✦ EXITING PROGRAM ✦',F);D(C,A);R('Saving session data');print(A+G+B+'Thank you for using NGL Spam Tool!');print(A+G+B+'Have a great day!');D(C,A);sys.exit(0)
U();N();f=input(A+L+B+'Username: ');D(C,A);E(f"✦ WELCOME, {f.upper()}! ✦",F);D(C,A);R('Loading user profile')
while V:
U();K=W()
if K=='1':R('Starting spam module');X()
elif K=='2':R('Loading information');U();N();input(A+L+B+'Press Enter to continue...')
elif K=='3':Y()
else:print(J+M+B+'Invalid option!');time.sleep(1)
if name=='main':
try:ngl()
except KeyboardInterrupt:print('\n'+R+'[!] Program interrupted by user'+W);sys.exit(0)

ini udah make yang pake termux tapi kurang

