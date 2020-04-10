# The Turing Game: AI

This little bit of Python has a few dependencies / constraints that must be taken into consideration.

### 1. You must install Python 3.7.
Due to the nature of TensorLayer's current support, Pyton 3.7 should be used.
On Windows, install Python 3.7 and ensure that it is being used to execute chat_bot.py.
On Linux, it is recommended to use virtualenvwrapper configured to use Python 3.7 instead of whatever existing Python install there may be.

### 2. (Windows only) Install Windows Visual C++ Redistributable for Visual Studio.
This is a dependency of TensorFlow for Windows.
https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads

### 3. Ensure pip is at least version 20.
`pip install --upgrade pip`

### 4. Install the requirements.
Ensure you are in the proper working directory (SWENG-2020-The-Turing-Game/ai/)

`pip install -U -r requirements.txt`

### 5. Ensure you have the proper mode selected.
By default you'll have a .env file with `MODE = 0` for the command-line interface.
If instead you wish to read and write input.txt and output.txt, change the variable to `MODE = 1` (or any other number).

### 6. execute chat_bot.py.
It should take a few seconds to initialise.
Queries to the CLI can be typed, with the option of a minute-long timer for entering questions.
Queries via input.txt will be continuously read and responses written to output.txt.
In either case, to end the program enter `exit`.
