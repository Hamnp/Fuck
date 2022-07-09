
# import libraries
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs


# function to clear screen
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# create sessions(if any) and check for any banned accounts
# TODO: Remove code input(just to check if an account is banned)
print('𝗖𝗛- @𝗞𝗨𝗥𝗗 𝗕𝗢𝗧𝗦 ', ' 𝗕𝗬 - @𝗛𝗔𝗠𝗔_𝗠𝗔𝗤𝗦𝗢𝗢𝗗 ༈༉')
print('\n' + info + lg + ' Pshknin Bo Accountakan akam...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} Pshknin {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}', 16746680, 'd038e172eb99839b69c39c3c25cd98cf')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('OK')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}sza drawa!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+' account szadrawa srawa la[Remove permanently using manager.py]'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Sessions created!')
clr()
# func to log scraping details(link of the grp to scrape
# and current index) in order to resume later
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} dast krd ba drwst krdni hallgrai user u id {w}status.dat{lg}')


def exit_window():
    input(f'\n{cy} Dast Bni ba enter bo daxstn...')
    clr()
    
    sys.exit()

# read user details
try:
    # rquest to resume adding
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} andamakani groupa zyad bkam {w}{status[0]}{lg}? [y/n]: {r}')
        if 'y' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt':
                os.system('del status.dat')
            else:
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} linke groupe taibat / yan user bnusa bom: {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} linke groupe taibat / yan user bnusa bom: {r}')
    index = 0
# load all the accounts(phonenumbers)
accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} akawantakant: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} halbzhira chand account challak bn: {r}'))
print(f'{info}{cy} zhmara bnwsa{lg}')
print(f'{cy}[0]{lg} groupe user')
print(f'{cy}[1]{lg} groupe link')
choice = int(input(f'{INPUT}{cy} jor halbzhira: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} linke groupakat bnwsa: {r}'))
else:
    target = str(input(f'{INPUT}{cy} linke groupakat bnwsa: {r}'))
print(f'{grey}_'*50)
#status_choice = str(input(f'{INPUT}{cy} Do you wanna add active members?[y/n]: {r}'))
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('vars.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} Kat channd bxaianit la zyad krdni andam{w}[{lg}0 bo har andamik{w}]: {r}'))
#print(f'{info}{lg} Joining group from {w}{number_of_accs} accounts...')
#print(f'{grey}-'*50)
print(f'{success}{lg} -- andam zyad krdn la {w}{len(to_use)}{lg}  --')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 60
    c = TelegramClient(f'sessions/{acc[0]}', 16746680 , 'd038e172eb99839b69c39c3c25cd98cf')
    print(f'{plus}{grey} user: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
    c.start(acc[0])
    acc_name = c.get_me().first_name
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- joine groupe uargri krd')
            except UserAlreadyParticipantError:
                pass
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- joine groupe andam zyad krdni krd')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined ')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- Joined ')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} User: {cy}{acc_name}{lg} -- Sarkawtw nabw')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Retrieving entities...')
    #c.get_dialogs()
    try:
        members = []
        members = c.get_participants(scraped_grp_entity, limit = 5500)
    except Exception as e:
        print(f'{error}{r} natwanm andam war brgm')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg} andam nya bo zyad krdn!')
        continue
    print(f'{info}{lg} Start: {w}{index}')
    #adding_status = 0
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} bbura natanm jari...') 

            break
        try:
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
            #print(f'{info}{grey} User: {cy}{acc_name}{lg} -- Sleep 1 second')
            adding_status += 1
            print(f'{info}{grey} User: {cy}{acc_name}{lg} -- kat {w}{sleep_time} {lg}second(s)')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} User: {cy}{acc_name}{lg} -- {r}User zyad krdni nachallak krdwa')
            continue
        except PeerFloodError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r}.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} natwanit andam zyad katn bo group')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r} sza dra la group')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} User: {cy}{acc_name}{lg} -- {r} pewistem ba adminya')
            break
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} User: {cy}{acc_name}{lg} -- {r} User peshtr tomar krawa')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} Halla Ruida')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- Adding Terminated ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
#global adding_status, approx_members_count
if adding_status != 0:
    print(f"\n{info}{lg} zyad krdn kotay hat")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()