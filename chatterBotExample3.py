from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

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
conversation_section = 0

sectionInfo = {}

# If previous topic was Prof then first becomes true. If ta then second becomes true.
previousTopic = [False, False]

# Reading information about the sections.
# Storing the information (Section# - Prof info - Ta info)
# Will later expand to include exam/assignment info.

def readingInSectionInformation():
	sectionInfoFile = open("sectionInfo.txt", "r")
	
	currentSectionNumber = 0
	
	sectionInfoList = []
	personInfoList = []
	
	infoCounter = 3
	
	for line in sectionInfoFile:
		line = line.strip()
		if len(line) == 3:
			if currentSectionNumber != 0:
				sectionInfo[currentSectionNumber] = sectionInfoList.copy()
				sectionInfoList.clear()
				
			currentSectionNumber = line
		else:
			if infoCounter > 0:
				personInfoList.append(line)
				infoCounter = infoCounter - 1
			else:
				personInfoList.append(line)
				sectionInfoList.append(personInfoList.copy())
				personInfoList.clear()
				infoCounter = 3
	
	if len(sectionInfoList) > 0:
		sectionInfo[currentSectionNumber] = sectionInfoList
	
	sectionInfoFile.close()

def caseAndPuncProcess(statement):
    statement = statement.lower()
    punctuation2 = ['\'s', '\'', ',', '.', '!', '?']
    
    for punct in punctuation2:
        statement = statement.replace(punct, '')
        
    return statement

def nameReplace(statement):

    global conversation_section

    if conversation_section != 0:
        statement.text = statement.text.replace(sectionInfo[conversation_section][0][0], "the professor")
        for listOfInfo in sectionInfo[conversation_section]:
            statement.text = statement.text.replace(listOfInfo[0], "ta")
        statement.text = statement.text.replace(" prof ", " the professor ")
    
    if statement.text.find(" section ") > -1:
        for s in statement.text.split():
            if s.isdigit():
                conversation_section = s
        statement.text = "my section is number"
    
    if conversation_section == 0 and (statement.text.find(" ta ") > -1 or statement.text.find(" professor ") > -1):
    	statement.text = "section information unknown"
    
    #print("Preprocess: " + statement.text)
    
    return statement

def infoReplace(response):
    manipulResponse = caseAndPuncProcess(response.text)
    
    if(" ta " in manipulResponse):
        response.text = response.text.replace("putEmail", sectionInfo[conversation_section][1][1])
        response.text = response.text.replace("putOffice", sectionInfo[conversation_section][1][2])
        response.text = response.text.replace("putHours", sectionInfo[conversation_section][1][3])
        previousTopic[0] = False
        previousTopic[1] = True
    
    if(" professor " in manipulResponse):
        response.text = response.text.replace("putEmail", sectionInfo[conversation_section][0][1])
        response.text = response.text.replace("putOffice", sectionInfo[conversation_section][0][2])
        response.text = response.text.replace("putHours", sectionInfo[conversation_section][0][3])
        previousTopic[1] = False
        previousTopic[0] = True
        
    if previousTopic[0]:
    	response.text = response.text.replace("putEmail", sectionInfo[conversation_section][0][1])
    	response.text = response.text.replace("putOffice", sectionInfo[conversation_section][0][2])
    	response.text = response.text.replace("putHours", sectionInfo[conversation_section][0][3])
            
    if previousTopic[1]:
        response.text = response.text.replace("putEmail", sectionInfo[conversation_section][1][1])
        response.text = response.text.replace("putOffice", sectionInfo[conversation_section][1][2])
        response.text = response.text.replace("putHours", sectionInfo[conversation_section][1][3])
        
    return response
        
readingInSectionInformation()

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
    	'chatterBotExample3.nameReplace',
    ],
    
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.80
        },
        
        {
        	'import_path': 'ChatterBotToPart2.TryingPartTwo'
        }
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
while(True):

	inputString = input("Client: ")
	
	inputString = caseAndPuncProcess(inputString)
	
	if (inputString == "exit"):
	    break
	else:
	    response = bot2.get_response(inputString)
	    response = infoReplace(response)
	    print("Chatbot: " + response.text)

print("Thank you for the conversation.")
