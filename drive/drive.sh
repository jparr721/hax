#!/bin/bash

echo "Showing physical disk statistics"

echo -e "\nName                 sdx             Mounted"
for dir in /sys/block/* ; do
	echo "`cat $dir/device/model` -- $dir"
done
