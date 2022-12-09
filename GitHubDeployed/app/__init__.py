from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from thefuzz import fuzz, process

from flask import Flask, render_template, redirect, make_response, request
app = Flask(__name__)

profInfo = ["Anjum Chida", "Anjum.Chida@utdallas.edu", "ECSW 1.002", "12:00pm to 2:00pm Mon/Wed"]
taInfo = ["Akshay Jha", "akshay.jha@utdallas.edu", "ECSS 1.003", "10:00am to 12:00pm Tues"]

#listOfQA = [('can you give me the professor email address','Sure. The professor\'s email is putEmail.'),('can you give the professor email address','Sure. The professor\'s email is putEmail.'),('can you give professor email address','Sure. The professor\'s is putEmail.'),('can you give me the professor email','Sure. The professor\'s is putEmail.'),('can you give the professor email','Sure. The professor\'s is putEmail.'),('can you give the professor name','Sure. The professor is putName.')]
listOfQA = [('can you give me the professor email address','Sure. The professor\'s email is putEmail.'),('can you give the professor email address','Sure. The professor\'s email is putEmail.'),('can you give professor email address','Sure. The professor\'s is putEmail.'),('can you give me the professor email','Sure. The professor\'s is putEmail.'),('can you give the professor email','Sure. The professor\'s is putEmail.'),('can you give the professor name','Sure. The professor is putName.'),('can you give me the professor office','Sure. The professor\'s office is here at putOffice.'),('can you give the professor office','Sure. The professor\'s office is here at putOffice.'),('can you give me professor office','Sure. The professor\'s office is here at putOffice.'),('can you give professor office','Sure. The professor\'s office is here at putOffice.'),('can you give me the professor office hours','Sure. The professor\'s office hours are putHours.'),('can you give the professor office hours','Sure. The professor\'s office hours are putHours.'),('can you give me professor office hours','Sure. The professor\'s office hours are putHours.'),('can you give professor office hours','Sure. The professor\'s office hours are putHours.'),('can you give me the ta name','Sure. The Ta is putName.'),('can you give me the ta email address','Sure. The Ta\'s email is putEmail.'),('can you give the ta email address','Sure. The Ta\'s email is putEmail.'),('can you give ta email address','Sure. The Ta\'s email is putEmail.'),('can you give me the ta email','Sure. The Ta\'s email is putEmail.'),('can you give the ta email','Sure. The Ta\'s email is putEmail.'),('can you give me the ta office','Sure. The Ta\'s office is here at putOffice.'),('can you give the ta office','Sure. The Ta\'s office is here at putOffice.'),('can you give me ta office','Sure. The Ta\'s office is here at putOffice.'),('can you give ta office','Sure. The Ta\'s office is here at putOffice.'),('can you give me the ta office hours','Sure. The Ta\'s office hours are putHours.'),('can you give the ta office hours','Sure. The Ta\'s office hours are putHours.'),('can you give me ta office hours','Sure. The Ta\'s office hours are putHours.'),('can you give ta office hours','Sure. The Ta\'s office hours are putHours.'),('what is the ta email address','The TA\'s email address is putEmail'),('what is the ta name','The TA\'s name is putName'),('what the ta email address','The TA\'s email address is putEmail'),('what is ta email address','The TA\'s email address is putEmail'),('what ta email address','The TA\'s email address is putEmail'),('what is the ta email','The TA\'s email address is putEmail'),('what the ta email','The TA\'s email address is putEmail'),('what is ta email','The TA\'s email address is putEmail'),('what ta email','The TA\'s email address is putEmail'),('where is the ta office','The TA\'s office is putOffice'),('where the ta office','The TA\'s office is putOffice'),('where is ta office','The TA\'s office is putOffice'),('where ta office','The TA\'s office is putOffice'),('what is the ta office hours','The TA\'s office hours are putHours'),('what the ta office hours','The TA\'s office hours are putHours'),('what is ta office hours','The TA\'s office hours are putHours'),('what is the professor email address','The Professor\'s email address is putEmail'),('what is the professor name','The Professor is putName.'),('what the professor email address','The Professor\'s email address is putEmail'),('what is professor email address','The Professor\'s email address is putEmail'),('what professor email address','The Professor\'s email address is putEmail'),('what is the professor email','The Professor\'s email address is putEmail'),('what the professor email','The Professor\'s email address is putEmail'),('what is professor email','The Professor\'s email address is putEmail'),('what professor email','The Professor\'s email address is putEmail'),('what is the professor office hours','The Professor\'s office hours are putHours'),('what is professor office hours','The Professor\'s office hours are putHours'),('what the professor office hours','The Professor\'s office hours are putHours'),('what professor office hours','The Professor\'s office hours are putHours'),('where is the professor office','The Professor\'s office is putOffice'),('where the professor office','The Professor\'s office is putOffice'),('where is professor office','The Professor\'s office is putOffice'),('where professor office','The Professor\'s office is putOffice'),('section information unknown','I need to know your section number first.'),('my section is number','Alrighty. What questions do you have?'),('who is the ta','The TA is putName.'),('who is ta','The TA is putName.'),('who ta','The TA is putName.'),('who the ta','The TA is putName.'),('who is the professor','The professor is putName.'),('who is professor','The professor is putName.'),('who professor','The professor is putName.'),('who the professor','The professor is putName.'),('what about email','Their email is putEmail.'),('what about name','Their name is putName.'),('what about email address','Their email is putEmail.'),('what about office hours','Their office hours are putHours.'),('what about office','Their office is putOffice.'),('what is their email','It is putEmail.'),('what is their name','It is putName.'),('what is their email address','It is putEmail.'),('what is their office hours','Their hours are putHours.'),('what is their office','Their office is putOffice.'),('where is his office','His office is at putOffice.'),('what is his email','It is putEmail.'),('what is his name','It is putName.'),('what is his email address','It is putEmail.'),('what is his office hours','His hours are putHours.'),('what is his office','His office is putOffice.'),('where is his office','His office is at putOffice.'),('what is her email','It is putEmail.'),('what is her email address','It is putEmail.'),('what is her office hours','Her hours are putHours.'),('what is her office','Her office is putOffice.'),('where is her office','Her office is at putOffice.'),('where is her name','Her name is putName.'),('howdy','howdy'),('hello','howdy'),('thank you','You\'re welcome!')]
# If previous topic was Prof then first becomes true. If ta then second becomes true.
previousTopic = [False, False]

def caseAndPuncProcess(statement):
    statement = statement.lower()
    punctuation2 = ['\'s', '\'', ',', '.', '!', '?']
    
    for punct in punctuation2:
        statement = statement.replace(punct, '')
        
    return statement

def nameReplace(statement):

    statement = statement.replace(profInfo[0].lower(), "the professor")
    statement = statement.replace(taInfo[0].lower(), "ta")
    statement = statement.replace(" prof ", " the professor ")
    
    return statement

def infoReplace(response):
    manipulResponse = caseAndPuncProcess(response)
   
    if(" ta " in manipulResponse):
        response = response.replace("putName", taInfo[0])
        response = response.replace("putEmail", taInfo[1])
        response = response.replace("putOffice", taInfo[2])
        response = response.replace("putHours", taInfo[3])
        previousTopic[0] = False
        previousTopic[1] = True
    
    if(" professor " in manipulResponse):
        response = response.replace("putName", profInfo[0])
        response = response.replace("putEmail", profInfo[1])
        response = response.replace("putOffice", profInfo[2])
        response = response.replace("putHours", profInfo[3])
        previousTopic[1] = False
        previousTopic[0] = True
        
    if previousTopic[0]:
        response = response.replace("putName", profInfo[0])
        response = response.replace("putEmail", profInfo[1])
        response = response.replace("putOffice", profInfo[2])
        response = response.replace("putHours", profInfo[3])
            
    if previousTopic[1]:
        response = response.replace("putName", taInfo[0])
        response = response.replace("putEmail", taInfo[1])
        response = response.replace("putOffice", taInfo[2])
        response = response.replace("putHours", taInfo[3])
        
    return response

def bot_responseGet(user_input):
    # this was done on purpose below to see what was wrong (I was hard coding the questions initially
    question = user_input
    # The bulk of the project imagine this inside of the logic adaptor hence an input is being passed
    confidence = 0  # this is set by default to ensure if any error occurs that we can recover from, our answer is none

    # this is to find the intent of a question
    cmplxCheck = "case time complexity worst best average"
    cmpCheck = "Which is faster bigger smaller than"
    defCheck = "definition of "

    # this is our KB
    cmpListn =   ["O(n) < O(n^2)", "O(2n) = O(n)", "O(3n) = O(n)", "O(n) = O(n/2)", "O(1/2 * n) = O(n)", "O(1/2n) = O(n)"]
    cmpListnsq = ["O(n^2) < O(n^3)", "O(n^n) > O(n^2)",  "O(1) < O(n^2)", "O(1) < O(n^3)", "O(1) < O(2^n)", "O(log(n) < O(n^2)"]
    cmpListlg =  ["O(log(n)) < O(n)", "O(log(n) < O(nlog(n))",  "O(log(n) < O(n^3)", "O(log(n) < O(2^n)", "O(log(n) < O(n!)"]
    cmpList =  [ "O(1) < O(n)", "O(1) < O(nlog(n)", "O(1) < O(n!)"]
        # "O(n) < O(nlog(n))", "O(n) < O(n^2)", "O(n) < O(n^3)", "O(n) < O(2^n)", "O(n) < O(n!)",
        # "O(nlog(n)) < O(n^2)", "O(nlog(n)) < O(n^3)", "O(nlog(n)) < O(2^n)", "O(nlog(n) < O(n!)",
        # "O(n^2) < O(n^3)", "O(n^2) < O(2^n)", "O(n^2) < O(n!)",
        # "O(n^3) < O(2^n)", "O(n^3) < O(n!)", "O(2^n) < O(n!)"]
    cmplxList = "Merge Sort has a Best Case time complexity: 𝛀(n*lg(n)). Merge Sort has Average Case time complexity: θ(n*lg(n)). Merge Sort has a Worst Case time complexity: O(n*lg(n)). Merge Sort has Space Complexity: O(n). Quick Sort has a Best Case: 𝛀(n*lg(n)). Quick Sort has a Average Case: θ(n*lg(n)). Quick Sort has a Worst Case: O(n^2). Quick Sort has a Space Complexity: O(n). Selection Sort has a Best Case: 𝛀(n^2). Selection Sort has a Average Case: θ(n^2).	Selection Sort has a Worst Case: O(n^2). Selection Sort has Space Complexity: O(1). Bubble Sort has a Best Case: 𝛀(n). Bubble Sort has Average Case: θ(n^2). Bubble Sort has a Worst Case: O(n^2). Bubble Sort has Space Complexity: O(1). Insertion Sort has a Best Case: 𝛀(n). Insertion Sort has Average Case: θ(n^2). Insertion Sort has a Worst Case: O(n^2). Insertion Sort has Space Complexity: O(n). Heap Sort has a Best Case: 𝛀(n*lg(n)). Heap Sort has Average Case: θ(n*lg(n)). Heap Sort has a Worst Case: O(n*lg(n)). Heap Sort has Space Complexity: O(1). Bucket Sort has a Best Case: 𝛀(n+k). Bucket Sort has Average Case: θ(n+k). Bucket Sort has a Worst Case: O(n^2). Bucket Sort has Space Complexity: O(n). Radix Sort has a Best Case: 𝛀(n*k). Radix Sort has Average Case: θ(n*k). Radix Sort has a Worst Case: O(n*k). Radix Sort has Space Complexity: O(n+k). Count Sort has a Best Case: 𝛀(n+k). Count Sort has Average Case: θ(n+k). Count Sort has a Worst Case: O(n+k). Count Sort has Space Complexity: O(k). Shell Sort has a Best Case: 𝛀(n*lg(n)). Shell Sort has Average Case: θ(n*lg(n)). Shell Sort has a Worst Case: O(n^2). Shell Sort has Space Complexity: O(1). Tim Sort has a Best Case: 𝛀(n). Tim Sort has Average Case: θ(n*lg(n)). Tim Sort has a Worst Case: O(n*lg(n)). Tim Sort has Space Complexity: O(n). Tree Sort has a Best Case: 𝛀(n*lg(n)). Tree Sort has Average Case: θ(n*lg(n)). Tree Sort has a Worst Case: O(n*lg(n)). Tree Sort has Space Complexity: O(n). Cube Sort has a Best Case: 𝛀(n). Cube Sort has Average Case: θ(n*lg(n)). Cube Sort has a Worst Case: O(n^2). Cube Sort has Space Complexity: O(n). Bogo Sort has a Best Case: 𝛀(n). Bogo Sort has Average Case: θ((n-1)*n!). Bogo Sort has a Worst Case: O(∞). Bogo Sort has Space Complexity: O(1). Quick Sort has a Best Case: 𝛀(n*lg(n)). Quick Sort has Average Case: θ(n^2). Quick Sort has a Worst Case: O(n^2). Quick Sort has Space Complexity: O(1). Quantum Bogo Sort has a Best Case: 𝛀(n). Quantum Bogo Sort has Average Case: θ(∞). Quantum Bogo Sort has a Worst Case: O(∞). Quantum Bogo Sort has Space Complexity: O(1). Linear Search has a Best Case: 𝛀(1). Linear Search has Average Case: θ(n/2) or just θ(n). Linear Search has a Worst Case: O(n). Linear Search has Space Complexity: O(1). Binary Search has a Best Case: 𝛀(1). Binary Search has Average Case: θ(lg(n)). Binary Search has a Worst Case: O(lg(n)). Binary Search has Space Complexity: O(1). Jump Search has a Best Case: 𝛀(1). Jump Search has Average Case: θ(n/2). Jump Search has a Worst Case: O(n). Jump Search has Space Complexity: O(1). Interpolation Search has a Best Case: 𝛀(1). This occurs when the middle (our approximation) is the desired key. Interpolation Search has Average Case: θ(lg(n)) It achieves this when the elements are uniformly distributed. Interpolation Search has a Worst Case: O(n) This occurs when the numerical values of hte keys increase exponentially. Interpolation Search has Space Complexity: O(1). Exponential Search has a Best Case: 𝛀(1). Exponential Search has Average Case: θ(lg(n)). Exponential Search has a Worst Case: O(lg(n)). Exponential Search has Space Complexity: O(lg(n)). Sublist Search has a Best Case: 𝛀(n). Sublist Search has Average Case: θ(n). Sublist Search has a Worst Case: O(n*m) where N is the length of a list and M is the length of sublist. Sublist Search has Space Complexity: O(1). Fibonacci Search has a Best Case: 𝛀(1). Fibonacci Search has Average Case: θ(n/2). Fibonacci Search has a Worst Case: O(n). Fibonacci Search has Space Complexity: O(1)."
    cmplxList = cmplxList.lower()
    cmplxList = cmplxList.split(". ")

    defList = "Definition of Time Complexity: the computational complexity to calculate the amount of resources (computational power as well as time) to run an algorithm. Time complexity takes into account how many actions are taken, but is generally focused on the number of accesses and variables uses. For example, bubble sort has to iterate an entire array of size ‘n’ to confirm that only the last variable is in place. There are still ‘n-1’ positions to check, and therefore has to run ‘n’ times over an input array of size ‘n’. Hence, it’s time complexity is O(n^2). Definition of Space Complexity: the computation complexity to calculate the amount of space or storage required to run an algorithm. Space complexity takes into account how many variables or structs are required to keep track of the algorithm to be able to carry it out. For example, bubble sort only requires enough space to hold a temporary variable in order to sort and thus only has a space complexity of O(1) or constant. Big-Oh or Big-O is the measure of the “worst case” computation and follows the format: O(variable), for example bubblesort runs in n^2 worst time, so O(n^2). Many algorithms have a very good “best case” scenario, but as in most algorithms that perform exceedingly well in certain scenarios, the “worst case” is often times more prevalent and therefore what most look out for. For example, in most cases, bubble sort may find a small number on the very end, as it will only ever shift 1 position over (if you are sorting ascending, then it starts on the far right side, and shifts to the left only a single position every iteration). Omega or 𝛀 is the measure of the “best case” or more formally, the “lower bound” computation and follows the format 𝛀(variable). For example bubblesort runs in 𝛀(n) as in the best case, it only has to run through the array a single time. In general we try to achieve Omega consistently. Theta or θ is the measure of the “average case” or average time it takes to compute an algorithm and follows the format θ(variable). Foro example, bubblesort runs in θ(n^2) as it has a tendency to follow the worst case and not the best case. In general we about having a tight bound and ensuring the average case is as low as possible, especially when the average case is close or identical to the best case. Definition of Tightly bound: If the 𝛀() and O() (more formally upper and lower bound) are the same or roughly the same, such that the average case or the θ(algorithm) is both the best and worst case, then it is considered tightly bound. For example, MergeSort’s worst case and best case are both O(n*lg(n)) and therefore so too is the average case. Therefore, MergeSort is considered a tightly bound sort. Definition of upperbound: This is the maximal amount of time it will take to compute an algorithm in run time. Essentially, upperbound is just the “worst case” scenario and is interchangeably used as such, or even denoted with Big-O: O(n) for example. Definition of lowerbound: This is the minimal amount of time it will take to compute an algorithm in run time. Essentially, lowerbound is just the “best case” scenario and is interchangeably used as such, or even denoted with Omega or 𝛀(n) for example. Definition of lg(n): It is important to note that in computer science due to the convenience and how binary works, we typically describe log as lg. This denotation specifies that instead of using logarithm as base 10, we instead use a base 2. It is key to note that lg and log are NOT the same thing, however in many textbooks and depending on professors and classes, they are frequently used interchangeably unless otherwise specified, but in general the intent is in reference to base 2. If you ever are uncertain or have questions, about which to use, please speak to the teacher or TA. Definition of Naive Algorithm: A simple algorithm that may or may not find the optimal solution and is often not the quickest. Definition of Greedy Algorithm: An algorithm that makes the best possible choice in the short term, that quickly finds an answer although it may not be optimal. Definition of Optimal answer: A path or solution that can be calculated and proven to be (one of, if not) the best possible answer or path. Sequential Search: In this, the list or array is traversed sequentially and every element is checked. Interval Search: These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half Definition of Divide and Conquer: An approach in algorithms where you break up problems into smaller more manageable chunks that are then solvable, and then these smaller parts are used to solve the algorithm as a whole."
    defList = defList.lower()
    defList = defList.split(". ")

    # Is this a definition?
    if (fuzz.partial_ratio(defCheck, question) > 60):
        x = process.extract(question, defList, limit=1)
        bot_response = (x[0][0], x[0][1] / 100)
        return bot_response

    # Is this a time complexity question?
    elif (fuzz.partial_ratio(cmplxCheck, question) > 60):
        x = process.extract(question, cmplxList, limit=1)
        y = x[0][0].split(": ")
        bot_response = (y[1], x[0][1] / 100)
        if (len(y[1]) > 10):
            temp = y[1].split(".\t")
            # print(temp[0])
            # print(temp[0])
            # print(y[0])
            y = (temp[0], x[0][1] / 100)
            bot_response = y
            #  print("This is y[0]: " + y[0] + "This is y[1]: " + str(y[1]))
            #  print("This is z: " + z[0] + ". This is confidence of z: " + str(z[1]))

            return bot_response
        # Is this a comparison question?
    elif (fuzz.partial_ratio(cmpCheck, question) > 40):
        # if(fuzz.partial_ratio("slower", question) > 5):
        x = process.extract(question, cmpList, limit=1)
        if (fuzz.partial_ratio("O(n) ", question) > 40):
            x = process.extract(question, cmpListn, limit=1)
            print("in first: " + str(x[0][1]))
        elif (fuzz.partial_ratio("O(n^2) ", question) > 40):
            x = process.extract(question, cmpListnsq, limit=1)
            print("in second: " + str(x[0][1]))

        elif (fuzz.partial_ratio("O(log(n) ", question) > 45):
            x = process.extract(question, cmpListlg, limit = 1)
            print("in third: " + str(x[0][1]))

        else:
            x = process.extract(question, cmpList, limit =1)
            print("in last: " + str(x[0][1]))

        bot_response = (x[0][0], x[0][1] / 100)
        return bot_response

    else: # we don't have anything we can currently answer
        bot_response = process.extract(question, cmpList, limit=1)
        bot_response = ("", 0)
        return bot_response

    bot_response = ("", confidence)
    return bot_response

#punctuation = ['\'s', '\'', ',', '.', '!', '?']

# Get a response for some unexpected input
def getResponse(inputString):
	#readingInSectionInformation()
#	inputString = caseAndPuncProcess(inputString)
	
#	response = bot2.get_response(inputString)
#	response = infoReplace(response)
#	return response.text

    inputString = caseAndPuncProcess(inputString)
    inputString = nameReplace(inputString)

    bestResponse = ""
    maxSimscore = 0.0

    tfidif_vectorizer = TfidfVectorizer()

    for tupleQA in listOfQA:
        comparTuple = (tupleQA[0], inputString)
        tfidf_matrix = tfidif_vectorizer.fit_transform(comparTuple)
        result_cos = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
        if maxSimscore < result_cos[0][1]:
            maxSimscore = result_cos[0][1]
            bestResponse = tupleQA[1]

    #testString = "what is the professor email"
    #example_1 = (testString, inputString)

    #tfidf_vectorizer = TfidfVectorizer()
    #tfidf_matrix = tfidf_vectorizer.fit_transform(example_1)
    #result_cos = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    
    if maxSimscore < 0.4:
        bestResponse = "I am sorry, but I do not understand. Try contacting tlh160001@utdallas.edu"
        maxSimscore = 0.1
    else:
        bestResponse = infoReplace(bestResponse)
        maxSimscore = maxSimscore * 2    

    Part2ResponseTuple = bot_responseGet(inputString)

    confidence = 0.5
    part2Response = ""

    if(Part2ResponseTuple[1] > 0.5):
        part2Response = Part2ResponseTuple[0]
        confidence = Part2ResponseTuple[1]
    else:
        confidence = 0
    #return selected_statement

    if(maxSimscore < confidence):
        bestResponse = part2Response

    return bestResponse
#   return inputString

@app.route("/index.html", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        response = make_response(getResponse(request.headers['chatbox']))
        response.mimetype = "text/plain"
        return response
    return render_template("index.html")

@app.route("/", methods = ['POST', 'GET'])
def hello():
    return redirect("/myapp/index.html")
#    return redirect("/index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/FAQ.html")
def FAQ():
    return render_template("FAQ.html")
