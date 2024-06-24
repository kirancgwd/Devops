#!bin/bash
############
#
#By Kiran C
#
#Shell script to check the server details
############

echo "Below is the avilable storage"
df -h
echo
echo "Below is the available memory"
free -m
echo
echo "Number of available processor"
nproc
