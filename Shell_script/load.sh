##!/bin/bash
###This script is the quick check to detect whether the performance issue is due to CPU, Memory, Input/Output (I/O), and network error 
##This script should work on both CentOS and macOS


# ###heck if the load average is greater than 70% of the CPU cores
load_avg=$(w | head -n 1 | awk '{print $8}' |cut -f1 -d",")
num_cores=$(nproc)
max_load=$(echo "0.7 * $num_cores" | bc)
#echo $max_load
if [ $(echo "$load_avg > $max_load" | bc) -eq 1 ]; then
#if [ $max_load -ge 1 ]; then
echo "load is greater than 1 : $max_load"
else
echo "Load is less than 1: $max_load"	
fi	
