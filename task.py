import os, subprocess, json
outdir = '/mnt/work/output/gdalinfo'
indir = '/mnt/work/input/data'
written = 0
unwritten = 0
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        #print "Full path:"
	inputpath = os.path.join(root,f)
	#print inputpath
 	#print "Place to put output:"
	outputpath = inputpath.replace(indir,outdir)
	#print outputpath

	fileName, fileExtension = os.path.splitext(outputpath)
	#outputfile = fileName + ".txt"
	outputfile = outputpath + "_gdalinfo.txt"
	#print outputfile


	# try to perform gdalinfo on this file:
	proc = subprocess.Popen(["gdalinfo %s" % inputpath], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = proc.communicate()
        status = proc.returncode

	#print out, err
	#print status

	if status == 0:
		written = written + 1
		print "Writing to %s" % outputfile
		outputdir = os.path.dirname(outputfile)
		try:
			os.makedirs(outputdir)
		except OSError as e:  # If the directory already exists, don't worry about it
			pass
		with open(outputfile, "w") as text_file:
			text_file.write(out)
	else:
		unwritten = unwritten + 1


	
status = { "status": "success", "reason": "Retrieved gdalinfo for %s files.  Gdal did not recognize %s files." % (written,unwritten) }
with open('/mnt/work/status.json', 'w') as outfile:
    json.dump(status, outfile)