# Introducing geoextent

geoextent is an easy to use library for extracting the geospatial extent from data files with multiple data formats.

Take a look at the [source code on GitHub](https://github.com/o2r-project/geoextent.git), [library on PyPI](https://pypi.org/project/geoextent/) and the [documentation website](https://o2r.info/geoextent/).

Here is a small example how to use `geoextent`.
```
geoextent -b -t -input= 'cities_NL.csv'
```
The output will show the bbox, time interval and crs extracted from file data, as follow: 

```
{'format': 'text/csv',
 'crs': '4326',
 'tbox': ['30.09.2018', '30.09.2018'],
 'bbox': [4.3175, 51.434444, 6.574722, 53.217222]}
```

[OpenStreetMap](https://www.openstreetmap.org/export#map=8/52.347/5.446) showing the area of extracted bbox. 

![](https://i.imgur.com/E5BR9ta.png)


You can get quick usage help instructions on the command line, too:

```
geoextent --help
```
Output:
```
geoextent is a Python library for extracting geospatial and temporal extents of a file or a directory of multiple geospatial data formats.

usage: geoextent [-h] [-formats] [-b] [-t] [-input= '[filepath|input file]']

optional arguments:
  -h, --help            show help message and exit
  -formats              show supported formats
  -b, --bounding-box    extract spatial extent (bounding box)
  -t, --time-box        extract temporal extent
  -input= INPUT= [INPUT= ...]
                        input file or path

By default, both bounding box and temporal extent are extracted.

Examples:

geoextent path/to/geofile.ext
geoextent -b path/to/directory_with_geospatial_data
geoextent -t path/to/file_with_temporal_extent
geoextent -b -t path/to/geospatial_files


Supported formats:
- GeoJSON (.geojson)
- Tabular data (.csv)
- Shapefile (.shp)
- GeoTIFF (.geotiff, .tif)
```

## Motivation

Geospatial properties of data can serve as a useful integrator of diverse data sets and can improve discovery of datasets.
However, spatial and temporal metadata is rarely used in common data repositories, such as [Zenodo](https://zenodo.org/).
Users may ask _what data is available for my area of interest over a specific time interval?_
This question formed the initial idea for creating a library that can serve as the basis for integration geospatial metadata in data repositories.
Because a core function is the extraction of the geospatial extent, we named it **`geoextent`**.
The data extracted using the library can be added to record metadata, which will allow users, specifically researchers, to find relevant data with less time and effort.

## Origins

The library's source code is based on two groups projects ([Cerca Trova](https://github.com/KathHv/geosoftware2_ct) and [Die Gruppe 1](https://github.com/carobro/Geosoftware2)) of the study project [Enhancing discovery of geospatial datasets in data repositories](https://geosoft2.github.io/2018.html).
We decided to develop the library with Python as we plan to integrate it with o2r's metadata extraction and processing tool [`o2r-meta`](https://github.com/o2r-project/o2r-meta).

## Process of creating the codebase

Luckily we did not have to start from scratch but could make `geoextent` a reimplementation of existing prototypes.
We roughly followed these steps:

- Evaluate the existing code of the [study project groups](https://geosoft2.github.io/2018.html)
  - Review the code implementation
  - Identify parts of the code that are re-usable
- Integrate chosen parts
- Develop of core features
- Set up [tests on Travis CI](https://travis-ci.org/github/o2r-project/geoextent/)
- Publication of library [on PyPI](https://pypi.org/project/geoextent/)
- Writing library documentation using [Sphinx](https://www.sphinx-doc.org/en/master/) and render it as part of the Travis CI process
- Adding introduction Notebook for easy testing with [MyBinder](TODO)

## Current features

- Extract bounding box. 
    ```
    geoextent -b -input= 'wf_100m_klas.tif'
    ```
    Output:
    ```
    {'format': 'image/tiff',
     'crs': '4326',
     'bbox': [5.91530075647532,
      50.3102519741084,
      9.46839871248415,
      52.5307755328733]}
    ```
- Extract time interval
     ```
    geoextent -t -input= 'muenster_ring_zeit.geojson'
    ```
    Output:
    ```
    {'format': 'application/geojson',
     'crs': 4326,
     'tbox': ['2018-11-14', '2018-11-14']}

    ```
- Show coordinate reference system (CRS) used
- Supported formats:
    - GeoJSON (.geojson)
    - Tabular data (.csv)
    - Shapefile (.shp)
    - GeoTIFF (.geotiff, .tif)

For more examples, see [documentation](https://o2r.info/geoextent/).

## Next steps

As an immediate next steps, we want to integrate the extraction of extents into `or2-meta` so that users creating an ERC will have to do less manual metadata creation.
We also hope that `geoextent` is useful to others and have plenty ideas about extending the library.
For example, being a Python project, we would like to explore integrating `geoextent` into Zenodo.
Most importantly, we will add support for multiple files and directories, but also further data formats - see [project issues on GitHub](https://github.com/o2r-project/geoextent/issues).
_We welcome your ideas, feature requests, comments, and of course contributions!_
