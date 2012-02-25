data_path = '/data/alstottj/Culture/'
job_directory = '/home/alstottj/Code/Mika/jobfiles/'
analysis_code_file = '/home/alstottj/Code/Mika/calculate_events.py'
python_location = '/usr/local/Python/2.7.2/bin/python'

swarm_file_name = job_directory+'swarm'
swarm_file = open(swarm_file_name, 'w')

import os
dirlist = os.listdir(data_path)

for i in dirlist:
    if i[-4:]=='.raw':
        print i
        base = i[:-4]
        folder = data_path+base+'/'
        fname = folder+base+'.h5'
        job_file_name = job_directory+base+'.py'
        job_file = open(job_file_name, 'w')
        job_file.write("folder = %r\n" % folder)
        job_file.write("fname = %r\n" % fname)
        job_file.write("execfile(%r)\n" % analysis_code_file)
        job_file.close()

        swarm_file.write("%s %s\n" % (python_location, job_file_name))

swarm_file.close()
from os import system
print("Submitting analyses with swarm file "+swarm_file_name)
system('swarm -f '+swarm_file_name+' -g 72 -m a')
