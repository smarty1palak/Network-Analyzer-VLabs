
#!/bin/bash

url=$1
echo "=======================================";
echo "$url"
echo "=======================================";
echo -n "First Hit: Caching: ";
wget --server-response -q -O - $url 2>&1 | grep Caching >/dev/null
if [ $? == 0 ]; then echo HIT; else echo MISS; fi;
echo -n "Second Hit: Caching: ";      
wget --server-response -q -O - $url 2>&1 | grep Caching >/dev/null
if [ $? == 0 ]; then echo HIT; else echo MISS; fi; echo "";