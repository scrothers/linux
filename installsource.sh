#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# Test for spectool on the system
/usr/bin/which spectool > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then
	for SPEC in ${DIR}/SPECS/*; do
		echo "[+] Downloading sources for ${SPEC}..."
		spectool -g -R ${SPEC}
	done
else
	echo "Error: Unable to locate 'spectool' which is required to download all sources."
fi
