##Background
---
As a world-class research university, the UW draws graduate students from widespread geographical locations. With a competitive, fast-moving housing market in Seattle, graduate students often struggle to find affordable and convenient housing. Furthermore, in a striking paper recently published in Nature: Biotechnology, graduate student mental health is in a crisis. Evans et al. report that “graduate students are more than six times as likely to experience depression and anxiety as compared to the general population.”1 It is easy to imagine a scenario where a graduate student’s mental health deteriorates as academic stress is exacerbated by the stress of an undesirable housing situation. It is important that graduate students have resources to find housing that fits their needs and desires.

Rather than providing address-level granularity for housing prices, we will focus on other metrics to inform incoming graduate students of their housing choice. Craigslist, Zillow, and Hotpads all provide price data; however, correlating the prices of apartments to transit times and other useful information can be difficult. We can provide new perspective to the housing search by providing commute data, greenspace data, and crime data on one interactive map tool.

##User Profile
---
Our targeted user is any graduate student looking for housing. We will make this tool with incoming graduate students who have not had the opportunity to visit Seattle in mind, in that they are unlikely to be familiar with neighborhood separations. The goal is that our targeted user will not have to interact with a python environment; instead, they will just need an internet connection to use our interactive graphic which is exported in an HTML format to a browser.

##Data Sources
---
Seattle has a wealth of open source data ranging from traffic data to crime data which are applicable to housing questions. Zillow also supplies rental price data for a variety of rental types. Sound Transit supplies map open transit data free of charge.

##Use Cases
---
###User wants to find the neighborhood with the cheapest rates for studio apartments

The user will navigate to our webtool. The user will then select the housing type overlay through a dropdown menu where housing types are listed. Studios through 3 bedroom houses will be listed; selecting “Studios” will bring up a map layer with color coding corresponding to a legend with housing price information.

###User has an address and wants to see the proximity to different bus routes

The user will type in the address and the map will relocate to a zoomed in view of the address (at the point of publication, the address search tool is not available). By clicking a bus route overlay, the bus route shapes will populate the map. The user can then see which routes pass close to the selected address and which stops are near their address. Hovering over the bus route layer will show basic information on the route (the route number and destination provided by Sound Transit).

1. Evans, TM; et. al. Nat. Biotechnol. 2018, 36, 282-284.
