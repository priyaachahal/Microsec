if [ $# != 2 ]
then
echo "Usage $0 inputfile 60"
exit
fi
for blockip in `cat "$1"`
     do
        echo "`iptables -A INPUT -s " $blockip " -j DROP`"
done
sleep 3600
for blockip in `cat "$1"`
     do
        echo "`iptables -D INPUT -s " $blockip " -j DROP`"
done
exit 0