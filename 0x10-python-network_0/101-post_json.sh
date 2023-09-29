#!/bin/bash
#
curl -s $1 -X POST -d '@$2' -H "Content-Type: application/json"
