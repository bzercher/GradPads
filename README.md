# GradPads

----

## Helping Graduate Students find affordable, enjoyable, and safe housing.

This visualization tool utilizes folium to map housing data in Seattle. With graduate students in mind, GradPads aggregates more than just price data to give users a more complete view of a neighborhood.

----

### Organization of the project

The project has the following structure:

```
  GradPads/
    |- data/
      |- Crime_Data.csv
      |- SPD_Beats_WGS84.json
      |- Transit_Routes_for_King_County_Metro__transitroute_line.geojson
      |- Zip_MedianRentalPrice_1Bedroom.csv
      |- Zip_MedianRentalPrice_Studio.csv
      |- greenspace2.geojson
      |- spd-beats.geojson
      |- wa_washington_zip_codes_geo.min.json
    | -docs/
      |- ComponentSpecification.md
      |- FunctionalSpecification.md
    |- examples
      |- MakingLayerExample.ipynb
    |- GradPads
      |- core.py
      |- data_manipulation.py
      |- tests/
        |- test_data_manipulation.py
    |- setup.py
    |- README.md
```

### Project data

This project utilizes Seattle open source data for crime, greenspace, and transit info. It also uses open source data for geojson zip code objects.

For housing prices, GradPads uses [Zillow Research data](https://www.zillow.com/research/data/) for monthly rental averages.

Future work on this package will incorporate other cities with open-data initiatives into our map building.

### Use Case

Our intended use case for this project is an incoming UW student who is moving to Seattle without being able to see the neighborhoods. In these situations, potential renters will venture to Craigslist or a similar site to enter in budget constraints. The user may be shown 5 different apartments in different neighborhoods that fall in their price range; however, without further information, the user may struggle to differentiate these properties.

By using GradPads, these apartments can be compared by proximity to transit, parks, and crime information. Average monthly rental prices are also included to give a general overview of neighborhood pricing, to aid in continued searching. 
