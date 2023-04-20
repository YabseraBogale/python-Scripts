from zipfile import ZipFile as zp

with zp('test.zip','w') as f:
    f.write('testimginput.html')
    f.setpassword(b"ok")