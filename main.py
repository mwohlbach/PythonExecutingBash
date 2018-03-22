import subprocess

output = subprocess.check_output(['bash','-c', 'git add .'])

print(str(output))