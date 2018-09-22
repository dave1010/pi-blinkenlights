#!/bin/sh
while true; do echo Spawning; `dirname "$0"`/listen.py; sleep 1; done
