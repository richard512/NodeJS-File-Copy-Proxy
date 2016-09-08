



for var in "$@"
do
	echo "Rendering on iPhone: $var"
	phantomjs --ignore-ssl-errors=yes --proxy=localhost:8080 "iphone.js" "$var"

	echo "Rendering on Desktop $var"
	phantomjs --ignore-ssl-errors=yes --proxy=localhost:8080 "desktop.js" "$var"
	sleep 2
done

cp -r cache/* /var/www/html/

exit
