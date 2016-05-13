Test possibilities:

# gdal-gbdx-task
A docker GBDX task for doing arbitrary gdal operations on data within DigitalGlobe's GBDX platform


Intended to use with gbdxtools like this:


```python
from gbdxtools import Interface
gbdx = Interface()

def gdalstuff( inputlocation="$input", outputlocation="$output" ):
    with open(inputloaction):
      # do gdal stuff
      
    with open(outputlocation):
      # write gdal stuff

gdaltask = gbdx.Task('gdal-task-name')
gdaltask.inputs.filetypes = 'tif'
gdaltask.inputs.cmd = jsonpickle(gdalstuff)

pythontask = gbdx.PythonTask(sourceBundle = 's3://path/to/src',function = gdalstuff, requirements=['python-gdal==1.0.0','adsafds'], pre-install-cmd="apt-get install gdal")
pythontask.inputs.input1 = firsttask.outputs.output1


workflow = gbdx.Workflow([gdaltask])
workflow.savedata(gdaltask.outputs.data, location='my_output_folder')
```
