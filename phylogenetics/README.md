# Phylogenetics
## Final project

Page dedicated to the final project from the phylogenetics part of the course. 

## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Authors](#authors)

## General Information

The goal of the final project was to explore phylogeny of the tribe Apieae belonging to the botanical family Apiaceae.

## Description of the files
* data - directory where IDs and sequences of nuclear and chloroplast markers as well as linked data are located
* alignments - directory where sequence alignments with the ClustalW, Mafft and Muscle algorithms are located
* alignments_trimmed - directory where the trimmed sequence alignments by automated1, nogaps and strict algorithms are located
* best_models - directory where best nucleotide substitution models for nuclear and chloroplast marker data are located
* partition_finder - directory where best data partition and nucleotide substitution model for linked data are located
* raxml - directory where ML analysis results (including rooted tree) are located
* mrbayes - directory where BI analysis results (including rooted tree) are located
* beast - directory where BEAST analysis results are located
* images - directory where the images placed in the report are located
* scripts - directory where the scripts used for analysis are located


## Usage

To run a script written in Python, go to the <i>./scripts</i> directory and in the terminal type the command:

```python 
python <file_name.py> 
```

where file_name.py is the name of the script.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Authors
Julia Smolik
