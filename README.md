# Getmetric Python library

## Install

Library can be installed using pip. To install do

```sh
pip install getmetric
```

## Examples

### Sending measurement
Example shows how to pass value 10 to Getmetric measurement:

```python
import getmetric

gm = getmetric.Getmetric(async_dump=True, send_period_sec=10)

gm.push_measure("YOUR_MEASUREMENT_CODE_HERE", 10)

gm.stop()
```

### Sending per/second measurement
Example shows how to measure operations per seconds using measurement value

```python
import getmetric
import time

gm = getmetric.Getmetric(async_dump=True, send_period_sec=10)
    
for x in range(100):
    gm.push_per_second_measure("YOUR_MEASUREMENT_CODE_HERE", 1)
    time.sleep(0.10)

gm.stop()
```

This is very useful when you need to calculate how much iteration per second you have withing
specific process, for example queries per second, API calls per second, etc.

NOTE: Measurement code can be taken from https://getmetric.net/metrics -> select and edit measurement, click Usage/Examples tab, check API key for measurement


### TODO: Operation

### TODO: Log
