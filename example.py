from gbdxtools import Interface
gbdx = Interface()

task = gbdx.Task('ricklin-gdal-test')
task.inputs.data = 's3://gbd-customer-data/7b216bd9-6523-4ca9-aa3b-1d8a5994f054/test_acomp_output/'
task.inputs.filetype = 'tif'

command = """
gdal_calc.py -A $input --A_band=2 -B $input --B_band=3 --outfile=$output \
--calc='(A.astype(float)-B)/(A.astype(float)+B)' --type=Float32
"""

task.inputs.command = command

workflow = gbdx.Workflow([task])
workflow.savedata(task.outputs.data, location='gdal-test-task-output3')
workflow.execute()