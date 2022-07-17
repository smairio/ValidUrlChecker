This script will check if the URL status code = 200 and will append the valid result to a text file (valid.txt)
containing the title of the requested url.
Link format : https://site.com
              http://site.com
usage :python ValidUrlChecker.py file.txt
file.txt content:https://google.com
                 https://youtube.com
                 https://bing.com
                 https://notvalidsitetest.com
in shell:
python ValidUrlChecker.py file.txt
https://google.com: Google
https://youtube.com: YouTube
https://bing.com: Bing
ignoring failed URL


valid.txt: https://google.com: 200 |Google
           https://youtube.com: 200 |YouTube
           https://bing.com: 200 |Bing
# ValidUrlChecker

