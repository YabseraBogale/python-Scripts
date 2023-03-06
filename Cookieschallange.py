from requests import get

for i in range(25):
	cookie=f'name{i}'
	header={'Cookie':cookie}
	r=get('http://mercury.picoctf.net:', headers=header)
	if 'pico' in r.text:
		print(r.text)
