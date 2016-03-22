#!/usr/bin/env python3
import sys
message = ' '.join(sys.argv[1:])
if message.startswith('.bots'):
    print('Hello!')
