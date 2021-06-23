import bs4, requests, os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\Safari/537.36',}
url = input("Please enter the url you want to download : ")
try:
    htmlfile = requests.get(url, headers=headers)
    print("Downloading...")
    htmlfile.raise_for_status()
    print("Successfully download the html code of the website")
except Exception as err:
    print("Fail to download the html code of the website: %s" % err)

print("We are going to create a folder to save the photos.")
folder_name = input("Please name it : ")
destDir = folder_name
if os.path.exists(destDir) == False:
    os.mkdir(destDir)

objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')

imgTag = objSoup.select('img')
print("Number of images found = ", len(imgTag))
success = 0
failure = 0
if len(imgTag) > 0:
    for i in range(len(imgTag)):
        imgUrl = imgTag[i].get('src')
        print("%s Photo downloading..." % imgUrl)
        finUrl = url + imgUrl
        print("%s downloading..." %finUrl)
        try:
            picture = requests.get(finUrl, headers=headers)
            picture.raise_for_status()
            print("%s Photo downloaded successfully!" % finUrl)
            pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), 'wb')
            success += 1
        except Exception as err:
            print("Fail to download the photo: %s" % err)
            failure += 1
        pictFile = open(os.path.join(destDir, os.path.basename(imgUrl)), 'wb')
        for diskStorage in picture.iter_content(10240):
            pictFile.write(diskStorage)
        pictFile.close()

print("Download Report:")
print("Success =",success)
print("Failure =",failure)
        
        