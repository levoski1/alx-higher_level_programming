#!/bin/bash
# ends a request to that URL displays the size of the response body
curl -sI "$1" | grep -s content-length | cut -d " " -f 2
