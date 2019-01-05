if [ $# != 2 ]
then
echo "Usage $0 websiteaddress searchword"
exit
fi
wget -r " $1 " -O - 2>/dev/null | egrep -o "https://|http://" | grep " $2 " > file.txt
exit