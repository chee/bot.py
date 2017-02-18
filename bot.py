#!/usr/bin/env python3

import irc.bot
import os
import subprocess

def config(key):
    return open('conf/' + key).readline().strip('\n')

class Petal(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, name, server, port):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, int(port))], name, name)
        self.channel = channel

    def on_welcome(self, connection, _):
        connection.join(self.channel)

    def on_privmsg(self, _, event):
        self.message(event, event.arguments[0])

    def on_pubmsg(self, _, event):
        self.message(event, event.arguments[0])

    def message(self, event, msg):
        user = event.source.split('!')[0]
        ignore = config('ignore').split(' ')
        if (user in ignore):
            return
        for mod in os.listdir('mods'):
            try:
                result = subprocess.check_output(['mods/' + mod, msg])
                self.connection.privmsg(config('channel'), result.decode().strip())
            except subprocess.CalledProcessError:
                print('subprocess failed')
            except PermissionError:
                print('couldnt execute ' + mod)

def main():
    bot = Petal(config('channel'), config('name'), config('server'), config('port'))
    bot.start()

if __name__ == "__main__":
    main()
