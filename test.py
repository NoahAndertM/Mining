import re

chat = open("chatLogLr.txt")
chatText = chat.read() # Inhalt einlesen
chat.close()

# Check ich nicht wirklich
mediaPattern = r"(<Medien ausgeschlossen>)" # Because it serves no purpose
regexMedia = re.compile(mediaPattern, flags=re.M)

dateAndTimepattern = r"(\d+\/\d+\/\d+)(,)(\s)(\d+:\d+)(\s)(\w+)(\s)(-)(\s\w+)*(:)"
regexDate = re.compile(dateAndTimepattern, flags=re.M)


print(chatText)
