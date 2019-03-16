for i in {1..10}
do
	let a="50*i+100"
	locust --host=http://mm-nitk.vlabs.ac.in --no-web -c $a -r 100 --run-time 1m --csv=ex$i   
done