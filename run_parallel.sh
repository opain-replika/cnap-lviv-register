#!/bin/bash
# run_parallel.sh - launch 9 parallel instances with configurable CENTER and TIME_HOUR

# Define possible values (arrays)
CENTERS=("вул. Виговського, 32 Терпідрозділ ЦНАП" "вул. Чупринки, 85 Терпідрозділ ЦНАП" "вул. Левицького, 67 Терпідрозділ ЦНАП")
TIME_HOURS=("12:30" "13:30" "14:30" "12:30" "13:30" "14:30" "12:30" "13:30" "14:30")

# Ensure the script is executable
chmod +x "$0"

# Launch 9 parallel processes
for i in $(seq 0 8); do
  # Cycle through the arrays to pick values
  CENTER=${CENTERS[$i % ${#CENTERS[@]}]}
  TIME_HOUR=${TIME_HOURS[$i % ${#TIME_HOURS[@]}]}

  # Export variables for the child process
  export CENTER
  export TIME_HOUR

  echo "Starting instance $i with CENTER='$CENTER' TIME_HOUR='$TIME_HOUR'"
  # Run python script in background, passing environment variables
  CENTER="$CENTER" TIME_HOUR="$TIME_HOUR" python main.py > "log_$i.txt" 2>&1 &
done

# Wait for all background jobs to finish
wait
echo "All 9 instances have finished execution."