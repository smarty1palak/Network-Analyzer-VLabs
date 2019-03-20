while read url
do
	for i in {1..10}
	do
		let a="50*i"
		locust --host=http://$url --no-web -c $a -r 100 --run-time 1m --csv=ex$url$i  
		echo "ex${url}${i}_requests.csv"
		cat "ex${url}${i}_requests.csv"| awk -v FS=',' '{print $4}'| head -3 | tail -n 1
		if [ "$(cat "ex${url}${i}_requests.csv"| awk -v FS=',' '{print $4}'| head -3 | tail -n 1)" -gt 40 ]
		then
			echo "maximum number of clients reached: $a"
			echo >> analysis.txt
			echo "${url} : ${a} " >> analysis.txt
			pwd
			break
		fi
	done
	echo "$url" 
done < $1