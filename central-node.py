import time
import sys
import subprocess
import os
import random

if len(sys.argv) < 3:
    print('Enter the number of processes to run!')

processes = int(sys.argv[1])
# Make actor directory
os.makedirs('actor', exist_ok=True)
with open('actor/current_actor.pt', 'w') as actor_file:
    actor_file.write('1')

# Make buffer directories and run processes
for p in range(processes):
    os.makedirs('buffer_' + str(p), exist_ok=True) 
    subprocess.run(['singularity', 'run', '--bind', 'buffer_' + str(p) + ':/buffer', '--bind', 'actor:/actor', 'test.sif'])


for i in range(100):
    with open('actor/current_actor.pt', 'w') as actor_file:
        actor_file.write(str(random.random()))
    time.sleep(1)
