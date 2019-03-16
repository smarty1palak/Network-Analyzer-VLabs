while read url
do
	for i in {1..10}
	do
		let a="50*i+100"
		locust --host=http://$url --no-web -c $a -r 100 --run-time 1m --csv=ex$url$i   
	done
	echo "$url" 
done < $1