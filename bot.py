#!/usr/bin/env python
import irc.bot
import os
import subprocess

def config(key):
    return open('conf/' + key).readline().strip('\n')

class Petal(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, name, server, port):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, int(port))], name, name)
        self.channel = channel

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.message(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        self.message(e, e.arguments[0])

    def message(self, e, msg):
        for mod in os.listdir('mods'):
            result = subprocess.check_output(['mods/' + mod, msg])
            self.connection.privmsg(config('channel'), result.decode().strip())


def main():
    bot = Petal(config('channel'), config('name'), config('server'), config('port'))
    bot.start()

if __name__ == "__main__":
    main()
