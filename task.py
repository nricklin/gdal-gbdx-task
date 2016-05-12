import os, subprocess, json
outdir = '/mnt/work/output/data'
indir = '/mnt/work/input/data'

input_data = json.load(open('/mnt/work/input/ports.json'))


filetype = input_data['filetype']
cmd = input_data['cmd']


# get all input files of a type
files = glob2.iglob(indir + "/**/*." + filetype.lower())
files.extend( glob2.iglob(indir + "/**/*." + filetype.upper()) )

for abs_filename in files:
	relative_filename = abs_filename.replace(indir,'').strip('/')
	relative_path = '/'.join(relative_filename.split('/')[:-1])
	filename = relative_filename.split('/')[-1:][0]
	print relative_filename
	print relative_path
	print filename


	output_directory = outdir + '/' + relative_path
	output_abs_filename = output_directory + filename

	try:
		os.makedirs(output_directory)

	# Generate command:
	command = cmd.replace('$input',abs_filename)
	command = command.replace('$output',output_abs_filename)

	proc = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()
    status = proc.returncode

    print out


status = { "status": "success", "reason": "Ran stuff." }
with open('/mnt/work/status.json', 'w') as outfile:
    json.dump(status, outfile)