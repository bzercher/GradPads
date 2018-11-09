Component Specification:

Software components:
	Data storage: We will take advantage of our free unlimited storage as UW students and store csv’s on Google Drive. Our lab uses Google Drive extensively, and both members of our project team have Drive FileStream installed on our computers. Data is stored in the cloud, but FileStream creates a local repository where Python can import data as if it were stored locally on our C: drive. We will set up a Team Drive.

	Data manager: Initially, we will make a jupyter notebook that will import data into dataframes to be visualized with our visualization manager. Using a jupyter notebook will allow us to tinker with the development of map layers quickly and easily.

	Visualization manager: Bokeh or Folium (TBD this weekend as we finish our Technology Review) - Both packages output HTML maps that we can host in a webpage.
Interactions

Interactions:
	We plan for our software interactions to all have taken place before our users set out to accomplish use cases. By generating HTML output, users won’t need to troubleshoot software interactions between our stored data, the data manager, and the visualization manager. Our jupyter notebook will access data stored on Google Drive and generate, say, the bus route maps. Using the Bokeh/Folium package, we will provide this map as an optional, interactive overlay in our HTML output. We can fine-tune these interactions to produce a final HTML output which our users will interact with.

Preliminary plan:
-Finish evaluating Bokeh and Folium
	-Run Bokeh jupyter notebook examples
	-Download and run Folium
	-Look at housing example shown in class to get a handle on Folium output
-Make new Team Drive for data storage
-Begin jupyter notebook writing to import and clean data and interface with visualization tool
