# GradPads

## Helping Graduate Students find affordable, enjoyable housing.

This visualization tool utilizes folium to map housing data in Seattle. With
graduate students in mind, GradPads aggregates more than just price data to give
users a more complete view of a neighborhood.

### Organization of the project

The project has the following structure:

```
  GradPads/
    |- data/
      |- Crime_Data.csv
      |- Neighborhood_MedianRentalPrice_1Bedroom.csv
      |- Neighborhood_MedianRentalPrice_Studio.csv
      |- Neighborhood_MedianRentalPrice_Studio.csv
      |- Neighborhood_ZriPerSqft_AllHomes.csv
      |- Transit_Routes_for_King_County_Metro__transitroute_line.geojson
      |- Transit_Stops_for_King_County_Metro__transitroute_line.geojson
      |- Zip_MedianRentalPrice_1Bedroom.csv
      |- Zip_MedianRentalPrice_Studio.csv
      |- Zip_ZriPerSqft
      |- greenspace2.geojson
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

This project uses Seattle open source data for crime, greenspace, and transit info.
It also uses open source data for geojson zip code objects.

This project also uses Zillow research data for housing prices.

### Use Case

Our intended user is a graduate student who is moving to Seattle with limited
information about how
