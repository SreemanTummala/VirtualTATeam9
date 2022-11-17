from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot2 = ChatBot('Test Bot')

newtrainer = ListTrainer(bot2)

greetingTrainer = ChatterBotCorpusTrainer(bot2)

greetingTrainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

# Train the chat bot with a few responses

newtrainer.train([
    'can you give me the professor email address',
    'Sure. The professor\'s email is putEmail.'
])

newtrainer.train([
    'can you give the professor email address',
    'Sure. The professor\'s email is putEmail.'
])

newtrainer.train([
    'can you give professor email address',
    'Sure. The professor\'s is putEmail.'
])

newtrainer.train([
    'can you give me the professor email',
    'Sure. The professor\'s is putEmail.'
])

newtrainer.train([
    'can you give the professor email',
    'Sure. The professor\'s is putEmail.'
])

newtrainer.train([
    'can you give the professor name',
    'Sure. The professor is putName.'
])

newtrainer.train([
    'can you give me the professor office',
    'Sure. The professor\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give the professor office',
    'Sure. The professor\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give me professor office',
    'Sure. The professor\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give professor office',
    'Sure. The professor\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give me the professor office hours',
    'Sure. The professor\'s office hours are putHours.'
])

newtrainer.train([
    'can you give the professor office hours',
    'Sure. The professor\'s office hours are putHours.'
])

newtrainer.train([
    'can you give me professor office hours',
    'Sure. The professor\'s office hours are putHours.'
])

newtrainer.train([
    'can you give professor office hours',
    'Sure. The professor\'s office hours are putHours.'
])

newtrainer.train([
    'can you give me the ta name',
    'Sure. The Ta is putName.'
])

newtrainer.train([
    'can you give me the ta email address',
    'Sure. The Ta\'s email is putEmail.'
])

newtrainer.train([
    'can you give the ta email address',
    'Sure. The Ta\'s email is putEmail.'
])

newtrainer.train([
    'can you give ta email address',
    'Sure. The Ta\'s email is putEmail.'
])

newtrainer.train([
    'can you give me the ta email',
    'Sure. The Ta\'s email is putEmail.'
])

newtrainer.train([
    'can you give the ta email',
    'Sure. The Ta\'s email is putEmail.'
])

newtrainer.train([
    'can you give me the ta office',
    'Sure. The Ta\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give the ta office',
    'Sure. The Ta\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give me ta office',
    'Sure. The Ta\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give ta office',
    'Sure. The Ta\'s office is here at putOffice.'
])

newtrainer.train([
    'can you give me the ta office hours',
    'Sure. The Ta\'s office hours are putHours.'
])

newtrainer.train([
    'can you give the ta office hours',
    'Sure. The Ta\'s office hours are putHours.'
])

newtrainer.train([
    'can you give me ta office hours',
    'Sure. The Ta\'s office hours are putHours.'
])

newtrainer.train([
    'can you give ta office hours',
    'Sure. The Ta\'s office hours are putHours.'
])

newtrainer.train([
    'what is the ta email address',
    'The TA\'s email address is putEmail'
])

newtrainer.train([
    'what is the ta name',
    'The TA\'s email address is putName'
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
    'what is the professor name',
    'The Professor is putName.'
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
    'who is the ta',
    'The TA is putName.'
])

newtrainer.train([
    'who is ta',
    'The TA is putName.'
])

newtrainer.train([
    'who ta',
    'The TA is putName.'
])

newtrainer.train([
    'who the ta',
    'The TA is putName.'
])

newtrainer.train([
    'who is the professor',
    'The professor is putName.'
])

newtrainer.train([
    'who is professor',
    'The professor is putName.'
])

newtrainer.train([
    'who professor',
    'The professor is putName.'
])

newtrainer.train([
    'who the professor',
    'The professor is putName.'
])


newtrainer.train([
    'what about email',
    'Their email is putEmail.'
])

newtrainer.train([
    'what about name',
    'Their name is putName.'
])

newtrainer.train([
    'what about email address',
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

newtrainer.train([
    'what is their email',
    'It is putEmail.'
])

newtrainer.train([
    'what is their name',
    'It is putName.'
])

newtrainer.train([
    'what is their email address',
    'It is putEmail.'
])

newtrainer.train([
    'what is their office hours',
    'Their hours are putHours.'
])

newtrainer.train([
    'what is their office',
    'Their office is putOffice.'
])

newtrainer.train([
    'where is his office',
    'His office is at putOffice.'
])

newtrainer.train([
    'what is his email',
    'It is putEmail.'
])

newtrainer.train([
    'what is his name',
    'It is putName.'
])

newtrainer.train([
    'what is his email address',
    'It is putEmail.'
])

newtrainer.train([
    'what is his office hours',
    'His hours are putHours.'
])

newtrainer.train([
    'what is his office',
    'His office is putOffice.'
])

newtrainer.train([
    'where is his office',
    'His office is at putOffice.'
])

newtrainer.train([
    'what is her email',
    'It is putEmail.'
])

newtrainer.train([
    'what is her email address',
    'It is putEmail.'
])

newtrainer.train([
    'what is her office hours',
    'Her hours are putHours.'
])

newtrainer.train([
    'what is her office',
    'Her office is putOffice.'
])

newtrainer.train([
    'where is her office',
    'Her office is at putOffice.'
])

newtrainer.train([
    'where is her name',
    'Her name is putName.'
])

newtrainer.train([
    'howdy',
    'howdy'
])

newtrainer.train([
    'hello',
    'howdy'
])

newtrainer.train([
    'thank you',
    'You\'re welcome!'
])

