#cpu average


#!/bin/bash
total_idle=0
count=0
for i in {01..57}; do
  if [ -f /var/log/sa/sa${i} ]; then
    # Extract average %idle for the day
    idle=$(sar -u -f /var/log/sa/sa${i} | grep "Average" | awk '{print $NF}')
    if [ ! -z "$idle" ]; then
      total_idle=$(echo "$total_idle + $idle" | bc)
      count=$((count + 1))
    fi
  fi
done
if [ $count -gt 0 ]; then
  avg_idle=$(echo "scale=2; $total_idle / $count" | bc)
  avg_cpu=$(echo "scale=2; 100 - $avg_idle" | bc)
  echo "Average CPU Utilization over $count days: $avg_cpu%"
else
  echo "No data available for the specified period."
fi

























# ram average script


#!/bin/bash
total_memused=0
count=0
for i in {01..57}; do
  if [ -f /var/log/sa/sa${i} ]; then
    # Extract average %memused for the day
    memused=$(sar -r -f /var/log/sa/sa${i} | grep "Average" | awk '{print $4}')
    if [ ! -z "$memused" ]; then
      total_memused=$(echo "$total_memused + $memused" | bc)
      count=$((count + 1))
    fi
  fi
done
if [ $count -gt 0 ]; then
  avg_memused=$(echo "scale=2; $total_memused / $count" | bc)
  echo "Average RAM Utilization over $count days: $avg_memused%"
else
  echo "No data available for the specified period."
fi