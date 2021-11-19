#!/bin/bash
filepath=$1
docker exec -i yottadb python3 ${filepath/\/workspace\/YottaPython-gitpod/}
