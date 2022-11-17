from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request, make_response, redirect
import json

# hard coding prof/ta names and emails
"""
professorName = "professor bob"
professorEmail = "pab120003@utdallas.edu"
professorOffice = "ECSW 1.002"
professorOfficeHours = "12:00pm to 2:00pm Mon/Wed"

taName = "tom smith"
taEmail = "tlh160001@utdallas.edu"
taOffice = "ECSS 1.003"
taOfficeHours = "10:00am to 12:00pm Tues"
"""
"""
How to store read section information?

1. List of Lists of Lists. (Bad)
2. Dictionary with Key = Section # and Value = List of Lists
	2a. Where first list = Prof info of format (Name, Email, Office, Hours)
	2b. Subsuquent lists = Ta info of format (Name, Email, Office, Hours)

"""
# What section current convo is thought to be:
#conversation_section = 232

profInfo = ["Anjum Chida", "Anjum.Chida@utdallas.edu", "ECSW 1.002", "12:00pm to 2:00pm Mon/Wed"]
taInfo = ["Akshay Jha", "akshay.jha@utdallas.edu", "ECSS 1.003", "10:00am to 12:00pm Tues"]
# If previous topic was Prof then first becomes true. If ta then second becomes true.
previousTopic = [False, False]

# Reading information about the sections.
# Storing the information (Section# - Prof info - Ta info)
# Will later expand to include exam/assignment info.

#def readingInSectionInformation():
#	sectionInfoFile = open("sectionInfo.txt", "r")
#	
#	currentSectionNumber = 0
#	
#	sectionInfoList = []
#	personInfoList = []
#	
#	infoCounter = 3
#	
#	for line in sectionInfoFile:
#		line = line.strip()
#		if len(line) == 3:
#			if currentSectionNumber != 0:
#				sectionInfo[currentSectionNumber] = sectionInfoList.copy()
#				sectionInfoList.clear()
#				
#			currentSectionNumber = line
#		else:
#			if infoCounter > 0:
#				personInfoList.append(line)
#				infoCounter = infoCounter - 1
#			else:
#				personInfoList.append(line)
#				sectionInfoList.append(personInfoList.copy())
#				personInfoList.clear()
#				infoCounter = 3
#	
#	if len(sectionInfoList) > 0:
#		sectionInfo[currentSectionNumber] = sectionInfoList
#	
#	sectionInfoFile.close()

def caseAndPuncProcess(statement):
    statement = statement.lower()
    punctuation2 = ['\'s', '\'', ',', '.', '!', '?']
    
    for punct in punctuation2:
        statement = statement.replace(punct, '')
        
    return statement

def nameReplace(statement):

    #global conversation_section

    #if conversation_section != 0:
    statement.text = statement.text.replace(profInfo[0].lower(), "the professor")
    statement.text = statement.text.replace(taInfo[0].lower(), "ta")
    statement.text = statement.text.replace(" prof ", " the professor ")
    
    #if statement.text.find(" section ") > -1:
    #    #print("Finding Section Oh!")
    #    for s in statement.text.split():
    #        if s.isdigit():
    #            conversation_section = s
    #            #print("Found section!")
    #            #print(s)
    #            break
    #    statement.text = "my section is number"
    
    #if conversation_section == 0 and (statement.text.find(" ta ") > -1 or statement.text.find(" professor ") > -1):
    #	statement.text = "section information unknown"
    
    #print("Preprocess: " + statement.text)
    
    return statement

def infoReplace(response):
    manipulResponse = caseAndPuncProcess(response.text)
    
    if(" ta " in manipulResponse):
        response.text = response.text.replace("putName", taInfo[0])
        response.text = response.text.replace("putEmail", taInfo[1])
        response.text = response.text.replace("putOffice", taInfo[2])
        response.text = response.text.replace("putHours", taInfo[3])
        previousTopic[0] = False
        previousTopic[1] = True
    
    if(" professor " in manipulResponse):
        response.text = response.text.replace("putName", profInfo[0])
        response.text = response.text.replace("putEmail", profInfo[1])
        response.text = response.text.replace("putOffice", profInfo[2])
        response.text = response.text.replace("putHours", profInfo[3])
        previousTopic[1] = False
        previousTopic[0] = True
        
    if previousTopic[0]:
        response.text = response.text.replace("putName", profInfo[0])
        response.text = response.text.replace("putEmail", profInfo[1])
        response.text = response.text.replace("putOffice", profInfo[2])
        response.text = response.text.replace("putHours", profInfo[3])
            
    if previousTopic[1]:
        response.text = response.text.replace("putName", taInfo[0])
        response.text = response.text.replace("putEmail", taInfo[1])
        response.text = response.text.replace("putOffice", taInfo[2])
        response.text = response.text.replace("putHours", taInfo[3])
        
    return response
        
# Create a new instance of a ChatBot
bot2 = ChatBot(
    'Test Bot',
    read_only = True,
    #storage_adapter='chatterbot.storage.SQLStorageAdapter'
    
    #professorInfo = ["professor bob", "pab120003@utdallas.edu", "ECSW 1.002", "12:00pm to 2:00pm Mon/Wed"],
    
    #taInfo = ["tom smith", "tlh160001@utdallas.edu", "ECSS 1.003", "10:00am to 12:00pm Tues"],
    
    preprocessors=[
    	'chatterbot.preprocessors.clean_whitespace',
    	'chatterbot.preprocessors.convert_to_ascii',
    	'chatterBotServerLobo.nameReplace',
    ],
    
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. Try contacting tlh160001@utdallas.edu',
            'maximum_similarity_threshold': 0.90
        },
        
        #{
        #	'import_path': 'ChatterBotToPart2.TryingPartTwo'
        #}
    ]
)

punctuation = ['\'s', '\'', ',', '.', '!', '?']

"""
Professor/TA email
Professor/TA Office
Professor/TA Office hours
Section Exam time, Date, Format
When is X due.
"""
# Get a response for some unexpected input
def getResponse(inputString):
	#readingInSectionInformation()
	inputString = caseAndPuncProcess(inputString)
	
	response = bot2.get_response(inputString)
	response = infoReplace(response)
	return response.text

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
   return redirect("/index.html")
   
@app.route('/index.html', methods = ['POST', 'GET'])
def index():
   if request.method == 'POST':
      print(request.headers['chatbox'])
      response = make_response(getResponse(request.headers['chatbox']))
      response.mimetype = "text/plain"
      return response
   return render_template('index.html')
   
@app.route('/FAQ.html')
def faq():
   return render_template('FAQ.html')
   
@app.route('/contact.html')
def contact():
   return render_template('contact.html')
   
@app.route('/about.html')
def about():
   return render_template('about.html')

if __name__ == '__main__':
   print("help")
   app.run(host = '127.0.0.1', port = 5500, debug = True)
else:
   print("fail")

