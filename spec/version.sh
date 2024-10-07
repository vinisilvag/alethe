#!/usr/bin/env sh
# Print a version string.

v=`git describe --tag --dirty=-changed --always 2> /dev/null`
if [ -n "$v" ]; then
    printf "%s" "$v"
else
	echo "not known"
fi

