import emlfilescan as emlscan
import virustotallink as vtl
import blacklist_keyword_check as blacklist
from printv import printv
import re
import requests
from bs4 import BeautifulSoup
import sys

try:
    scantype = int(input('''1. Scan link\n2. Scan domain\n3. Threat report from downloaded email (.eml)\n4. Scan singular message\n5. Threat report from exported whatsapp chat\n6. Scan file\n\nOption: '''))
except:
    sys.exit(1)
if scantype == 1:
    pass
if scantype == 2:
    pass
if scantype == 3:
    emlfile = str(input(".eml file: "))
    email_subject, received_from_addr, received_from_ip, reply_to, emailtext, links_in_email = emlscan.parse_eml(emlfile)
    blacklistedwords, blacklistedwordscnt = blacklist.check_blacklisted_keywords(emailtext + email_subject)

    printv("")
    print("\n[+] SCANNING FOUND LINKS")
    mallinks = []
    suslinks = []
    linksscannedcount = 0
    for link in links_in_email:
        try:
            sus_percent, malcount, suscount = vtl.scanlink(link)
            linksscannedcount += 1
            if malcount > 0:
                mallinks.append(f"\nLink Reported malicious: {malcount} times\n" + link)
            if suscount > 0:
                suslinks.append(f"\nLink Reported suspicious: {suscount} times\n" + link)
        except Exception as e:
            printv(e)
    printv()

    printv(f"\n[+] No. of links scanned: {linksscannedcount}")
    iplist = []
    iplinks = []
    try:
        for line in links_in_email:
            ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line)
            iplist += ip
            if ip:
                iplinks.append(line)
    except Exception as e:
        printv(e)
    # printv(links_in_email)
    # url1 = "http://www.webconfs.com/domain-age.php"
    # for url in links_in_email:
        

    ## ALERT PRINTING ######################################################
    if len(blacklistedwords) > 0:
        printv(f"\nVIRUSTOTAL SCAN RESULTS", color="RED")
        printv(f"\nBlacklisted phrases found {blacklistedwordscnt} times", color="RED")
        printv(f"\nBlacklisted phrases found:\n", color="RED")
        blacklistedwords = [x.strip() for x in blacklistedwords]
        printv(blacklistedwords, color="RED")
    for i in suslinks:
        printv(i, color="RED")
    for i in mallinks:
        printv(i, color="RED")
    if len(mallinks) > 0:
        printv("\n[**] WARNING!! THIS EMAIL CONTAINS MALICIOUS ATTACHMENTS/LINKS.\n", color="RED")
    if len(iplist) > 0:
        printv("\nIP ADDRESSES FOUND IN LINKS (SUSPICIOUS)\n", color="RED")
        for ip in iplinks:
            printv(ip, color="RED")
    
    ## ALERT PRINTING END ######################################################
    
if scantype == 4:
    pass
if scantype == 5:
    pass
if scantype == 6:
    pass