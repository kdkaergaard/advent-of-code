#!/usr/bin/env sh

awk '{total += int($1/3)-2} END {print total}' ../modules.txt
