import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\Safari/537.36',}
url = input("Please enter the url you want to download : ")
try:
    htmlfile = requests.get(url, headers=headers)
    print("Downloading...")
    htmlfile.raise_for_status()
    print("Successfully download the html code of the website")
except Exception as err:
    print("Fail to download the html code of the website: %s" % err)

file_name = input("Please name the file name : ")
fn = file_name + '.txt'
total_size = 0
with open(fn, 'wb') as file_Obj:
    for diskStorage in htmlfile.iter_content(10240):
        size = file_Obj.write(diskStorage)
        total_size += size
        print("File size downloaded : %d bytes" %total_size)
    print("With file name: %s (file size: %d bytes) saved HTML file successful!" % (fn ,total_size) )