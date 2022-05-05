#!/bin/bash
echo -e "\$> python3 exec.py 'Hello World!' | cat -e"
python3 exec.py 'Hello World!' | cat -e
echo -e "\n\$> python3 exec.py 'Hello' 'my Friend' | cat -e"
python3 exec.py 'Hello' 'my Friend' | cat -e
echo -e "\n\$> python3 exec.py"
python3 exec.py
echo