#!/bin/bash

DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd .. && pwd )

# Test for spectool on the system
/usr/bin/which spectool > /dev/null 2> /dev/null
if [ $? -eq 0 ]; then
	for SPEC in ${DIR}/SPECS/*; do
		echo "[+] Downloading sources for ${SPEC}..."
		spectool -g -R ${SPEC}
		if [ $? -ne 0 ]; then
			echo "Error: Unable to download source for ${SPEC}..."
			exit 1
		fi
	done
else
	echo "Error: Unable to locate 'spectool' which is required to download all sources."
	exit 1
fi
