from irc import bot

config_file = open('config', 'r')
config = dict([line.strip('\n').split() for line in config_file.readlines()])
config_file.close()
print(config)
