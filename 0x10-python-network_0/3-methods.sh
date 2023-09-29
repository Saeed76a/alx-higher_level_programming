#!/bin/bash
# 
curl -sI $@ | grep Allow | cut -d ' ' -f2-
