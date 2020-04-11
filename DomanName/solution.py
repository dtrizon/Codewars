def domain_name(url):
	tempurl = url.split('://')
	if (len(tempurl) == 2):
		if (len(tempurl[1].split('www.')) == 2):
			return tempurl[1].split('www.')[1].split('.')[0]
		else:
			return tempurl[1].split('.')[0]
	else:
		if len(url.split('www.')) == 2:
			return url.split('www.')[1].split('.')[0]
		else:
			return url.split('.')[0]