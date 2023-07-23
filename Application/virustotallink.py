import vt
import time
import hashlib
from printv import printv

API_KEY_VIRUSTOTAL = "05a005915e6bd5d067fa6d4c6c985746a5c2b7d371b840500c2b0630f11c7b1c"

# def scanfile(filepath):
#     client = vt.Client(API_KEY_VIRUSTOTAL)
#     with open(filepath, "rb") as file2scan:
#         bytes = file2scan.read()
#         readablehash = hashlib.sha256(bytes).hexdigest()
#     file = client.get_object(".\\files\\" + str(readablehash))## check if scanned before
#     print(file.last_analysis)
#     with open(filepath, "rb") as file2scan:
#         analysis = client.scan_file(file2scan, wait_for_completion=False)
#         time.sleep(10)
#     print(analysis.status)
#     return

def scanlink(url):
    printv(f"\n{url}")
    try:
        client = vt.Client(API_KEY_VIRUSTOTAL)
        printv("Client object created")
        urlid = vt.url_id(url)
        printv("Urlid created")
        url = client.get_object("/urls/{}".format(urlid))
        printv("RETRIEVED URL SCAN OBJECT")
        printv(f"\n\n[*] LINK REPORT \n\n")
        printv(f"\nNo. of times url submitted: {url.times_submitted}")
        printv(f"\nUrl last analysis stats: \n{url.last_analysis_stats}")
        sus_percent = (int(url.last_analysis_stats['malicious']) +
                            int(url.last_analysis_stats['undetected'])+
                            int(url.last_analysis_stats['suspicious'])) / (int(url.last_analysis_stats['malicious']) + 
                            int(url.last_analysis_stats['undetected']) +
                            int(url.last_analysis_stats['suspicious']) +
                            int(url.last_analysis_stats['harmless'])
                            )
        printv(f"\nReported as Malicious: {url.last_analysis_stats['malicious']}\n")                      
        printv(f'''\nMal percent: {sus_percent}\n''')
        printv("\n\nLINK REPORT END\n\n")
    except Exception as e:
        printv(e)
        printv("\n\nFAILED TO SCAN LINK. PROCEED WITH CAUTION\n\n")
        client.close()
        return
    client.close()
    return sus_percent, url.last_analysis_stats['malicious'], url.last_analysis_stats['suspicious']

def domaininfo(domain):
    client = vt.Client(API_KEY_VIRUSTOTAL)

    client.close()
    return

#scanlink("https://www.chess.com/")
# domaininfo("donotreply@isc2.brightspace.com") # use domaininfo function for email scanning