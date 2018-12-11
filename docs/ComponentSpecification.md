# Component Specification
----
## Software components
---
### Data storage

Data is stored in the repository in the data folder. The largest dataset is 46 MB, which is falls under Github's storage limit. Because there are not large datasets, our python script that generates the map meets any data management needs, so long as the directory structure remains unchanged.

### Visualization

The [folium](https://github.com/python-visualization/folium) package is used to produce our the visualization of our map layers.

##Interactions
---
The current plan for a finalized GradPads product is a webtool hosted online. By generating HTML output, users won’t need to troubleshoot software interactions between our stored data and the visualizations.

In this package distribution, we supply the code for users with a python environment to create the HTML object. This can be accomplished by simply installing the package and running `python core.py` and then opening the created HTML file (as outlined in our README installation instructions). At this stage of development, a graduate student could clone our repository, run this line of code, and carry out the specific use cases laid out in the FunctionalSpecification. 
