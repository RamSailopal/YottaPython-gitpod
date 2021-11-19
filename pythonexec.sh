#!/bin/bash
filepath=$1
echo $filepath
echo ${filepath/\/workspace\/YottaPython-gitpod/}
docker exec -i yottadb "python3 ${filepath/\/workspace\/YottaPython-gitpod/}"
