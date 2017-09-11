# Sentilo sensors: Noise detection

## About

This tiny project has been made to study how data from sensors in the Sentilo platform can be retrieved, as well as visualizing it using R.

Data obtention has been based of [300000kms' project](https://github.com/300000kms/sentilo) and looking at [sentilo](https://github.com/sentilo/sentilo) source code, since the API does not seem to work properly in [Barcelona's](http://connecta.bcn.cat/) case.


## Structure
* __sentilo.py__ is used to retrieve the data and save it in a CSV file.
* __data\_vis.R__ takes that data and plots it.


## Example

You can see an example in the following picture.
The data was taken at 15 minutes interval from 8.30h to 20h from the sensors located at Passeig de Gràcia.
![](/examples/noise.png)

This allows seeing how the increase of people there is slower than when they are leaving, peaking between 5 and 6. People where appointed to go at 17.14h.

## LICENSE
```
Copyright 2017 Laura C.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
