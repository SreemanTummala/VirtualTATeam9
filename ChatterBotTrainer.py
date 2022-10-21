from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot2 = ChatBot('Test Bot')

newtrainer = ListTrainer(bot2)
'''
greetingTrainer = ChatterBotCorpusTrainer(bot2)

greetingTrainer.train(
    "chatterbot.corpus.english.greetings"
)
'''
# Train the chat bot with a few responses

newtrainer.train([
    'what is the ta email address',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what the ta email address',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what is ta email address',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what ta email address',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what is the ta email',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what the ta email',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what is ta email',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what ta email',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'where is the ta office',
    'The TA\'s office is putOffice'
])

newtrainer.train([
    'where the ta office',
    'The TA\'s office is putOffice'
])

newtrainer.train([
    'where is ta office',
    'The TA\'s office is putOffice'
])

newtrainer.train([
    'where ta office',
    'The TA\'s office is putOffice'
])

newtrainer.train([
    'what is the ta office hours',
    'The TA\'s office hours are putHours'
])

newtrainer.train([
    'what the ta office hours',
    'The TA\'s office hours are putHours'
])

newtrainer.train([
    'what is ta office hours',
    'The TA\'s office hours are putHours'
])

newtrainer.train([
    'what is the professor email address',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what the professor email address',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what is professor email address',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what professor email address',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what is the professor email',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what the professor email',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what is professor email',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what professor email',
    'The Professor\'s email address is putEmail'
])

newtrainer.train([
    'what is the professor office hours',
    'The Professor\'s office hours are putHours'
])

newtrainer.train([
    'what is professor office hours',
    'The Professor\'s office hours are putHours'
])

newtrainer.train([
    'what the professor office hours',
    'The Professor\'s office hours are putHours'
])

newtrainer.train([
    'what professor office hours',
    'The Professor\'s office hours are putHours'
])

newtrainer.train([
    'where is the professor office',
    'The Professor\'s office is putOffice'
])

newtrainer.train([
    'where the professor office',
    'The Professor\'s office is putOffice'
])

newtrainer.train([
    'where is professor office',
    'The Professor\'s office is putOffice'
])

newtrainer.train([
    'where professor office',
    'The Professor\'s office is putOffice'
])

newtrainer.train([
    'section information unknown',
    'I need to know your section number first.'
])

newtrainer.train([
    'my section is number',
    'Alrighty. What questions do you have?'
])

newtrainer.train([
    'what about email',
    'Their email is putEmail.'
])

newtrainer.train([
    'what about office hours',
    'Their office hours are putHours.'
])

newtrainer.train([
    'what about office',
    'Their office is putOffice.'
])
