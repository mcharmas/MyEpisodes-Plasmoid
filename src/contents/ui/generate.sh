path="../code/generated/"
for f in $(ls *.ui); do
	class=${f%.*}
	pyuic4 -o $path$class.py $f
done
