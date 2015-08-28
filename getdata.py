import json
import pycurl
from StringIO import StringIO
countRepositorys = 0
countmax = 10000

countMakefile = 0
countSConstruct = 0
countWafProject = 0
countRake = 0
countDoIT = 0
countCMake = 0
countAll = 0
# Erkennungsmerkmale
Makefile = 'title="Makefile"'
SConstruct = 'title="SConstruct"'
WafProject = 'title="wscript"'
Rake = 'title="Rakefile"'
DoIT = 'title="dodo.py"'
CMake = 'title="CMakeLists.txt"'
print(pycurl.version)
for month in xrange(1,13):
	if(month<10):
		month = str(0)+str(month)
	else:
		month = str(month)
	for d in xrange(1,32):
		if(countAll<countmax):
			if(d<10):
				d = str(0)+str(d)
			else:
				d = str(d)
			for x in xrange(1,11):
				link = 'https://api.github.com/search/repositories?q=stars%3A>1%20created:2013-'+month+'-'+d+'&s=forked&per_page=100&page='+str(x)
				buffer = StringIO()
				c = pycurl.Curl()
				c.setopt(c.URL, link.encode('ascii'))
				c.setopt(c.WRITEFUNCTION, buffer.write)
				c.perform()
				c.close()

				body = buffer.getvalue()
				parsed_json = json.loads(body)
				try:
					for post in parsed_json['items']:
						if(countAll<countmax):
							countRepositorys += 1
							#print(post['html_url'])
							buffer = StringIO()
							rep = pycurl.Curl()
							rep.setopt(rep.URL, post['html_url'].encode('ascii'))
							rep.setopt(rep.WRITEFUNCTION, buffer.write)
							rep.perform()
							rep.close()
							contents = buffer.getvalue()
							if(contents.find(Makefile)>0):
								print("Makefile genutzt: "+post['html_url'])
								countMakefile +=1
								countAll +=1
							elif(contents.find(SConstruct)>0):
								print("SConstruct genutzt: "+post['html_url'])
								countSConstruct +=1
								countAll +=1
							elif(contents.find(WafProject)>0):
								print("WafProject genutzt: "+post['html_url'])
								countWafProject +=1
								countAll +=1
							elif(contents.find(Rake)>0):
								print("Rake genutzt: "+post['html_url'])
								countRake +=1
								countAll +=1
							elif(contents.find(DoIT)>0):
								print("DoIT genutzt: "+post['html_url'])
								countDoIT +=1
								countAll +=1
							elif(contents.find(CMake)>0):
								print("CMake genutzt: "+post['html_url'])
								countCMake +=1
								countAll +=1
				except Exception:
					print("Error: "+link)
print("--------------------")
print("Makefile: "+str(countMakefile))
print("SConstruct: "+str(countSConstruct))
print("WafProject: "+str(countWafProject))
print("Rake: "+str(countRake))
print("DoIT: "+str(countDoIT))
print("CMake: "+str(countCMake))
print("Gesamt: "+str(countAll))
print("Anzahl der Repositories: "+str(countRepositorys))
print("--------------------")





