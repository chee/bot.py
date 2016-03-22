#!/usr/bin/env python
import sys
message = ' '.join(sys.argv[1:])
if message.startswith('.bots'):
    print('Hello!')
