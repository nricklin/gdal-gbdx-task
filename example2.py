from gbdxtools import Interface
gbdx = Interface()

task = gbdx.Task('ricklin-gdal-test')
task.inputs.data = ' s3://gbd-customer-data/7b216bd9-6523-4ca9-aa3b-1d8a5994f054/sethtest/'
#task.inputs.filetype = 'tif'
task.inputs.execution_strategy = 'runonce'

command = """
gdalbuildvrt $indir/out.vrt  $indir/*.tif;
gdal_translate  $indir/out.vrt  $outdir/out.tif
"""


task.inputs.command = command


workflow = gbdx.Workflow([task, task2])
workflow.savedata(task.outputs.data, location='seth_test_output')
workflow.execute()