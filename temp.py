# copy 

import shutil,os

src ='\\\\LNGSHAD-001\\WebsitesShared\\LA-App_Cert2_release_r1020_daily_build'
dst = 'C:\\inetpub\\wwwroot\\nl_cert2'
# print(os.walk(dst,topdown=False))

for root,dirs,files in os.walk(dst, topdown=True):
    for name in files:
        print(name)
    for name in dirs:
        print(name)