#!/usr/bin/env python3

"""Hello World multi languages.

Depending of the language configured on the environment the program shows the 
corresponding message.

Usage:

have the LANG env environment correctly configured, example:

    export LANG=pt_BR

Execution:

    python3 hello.py
    or
    python ./hello.py
 
"""

__version__ = "0.0.1"
__author__ = "Marcos Paulo"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!" 
    

print(msg)
