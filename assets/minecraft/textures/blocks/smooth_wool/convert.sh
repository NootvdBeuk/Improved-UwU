contains() {
	string="$1"
	substring="$2"
	if test "${string#*$substring}" != "$string"
	then
		return 0
	else
		return 1
	fi
}

for i in wool_*.png
do
	# only apply on images not yet converted
	contains $i "colored" || mv $i $(echo $i | sed 's:wool_:wool_colored_:g')
done
