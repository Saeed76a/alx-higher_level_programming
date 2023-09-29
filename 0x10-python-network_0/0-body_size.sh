#!/bin/bash
# display the length of the conetent
curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2
