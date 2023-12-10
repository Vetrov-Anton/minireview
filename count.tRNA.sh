#!/bin/bash
cut -f1,14 | grep '^tRNA' | cut -b10-13 | sort | uniq -c | tr -d ' '| tr '-' '/' | sort -k 1nr
