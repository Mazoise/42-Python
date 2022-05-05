#!/bin/bash
echo -e "\$> python filterwords.py \"Hello, my friend\" 3"
python filterwords.py "Hello, my friend" 3
echo -e "\n\$> python filterwords.py \"A robot must protect its own existence as long as such protection does not conflict with the First or Second Law\" 6"
python filterwords.py "A robot must protect its own existence as long as such protection does not conflict with the First or Second Law" 6
echo -e "\n\$> python filterwords.py  Hello World"
python filterwords.py  Hello World
echo -e "\n\$> python filterwords.py 300 3"
python filterwords.py 300 3
echo