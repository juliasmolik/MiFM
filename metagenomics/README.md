# Metagenomics
## Final project

Page dedicated to the final project from the metagenomics part of the course. 

## Table of Contents
* [General Info](#general-information)
* [Usage](#usage)
* [License](#license)
* [Authors](#authors)

## General Information

In 2017 - 2019, a study was conducted to analyze the taxonomic composition and biodiversity of autotrophic euglenins in more than a dozen small water reservoirs located in different regions of Poland.

Water samples from selected reservoirs were collected four times during the growing season in 2017, 2018 and 2019. The collected material was deposited on filters, from which total DNA was then isolated. Amplification of the V2 region of 18S rDNA was then carried out using euglenin-specific primers. The resulting amplicons were subjected to high-throughput sequencing and fastq format files with reads assigned to individual samples were obtained.

The aim of this study is to examine and describe the quality of the data, and then analyze the taxonomic composition using various statistics, graphs, and α-diversity and β-diversity analyses.

The performance of the analyses was divided into two stages. The first involved manipulating the data so as to obtain filtered and trimmed reads, which were then classified taxonomically. QIIME software was used for this purpose. Analysis of the obtained data was then performed using a script written in R. An alpha- and beta-diversity analysis was performed, as well as a taxonomic composition analysis. The obtained results were presented by various graphs.

## Description of the files
* Smolik_zadanie1.pdf - final report
* data - directory where the sequencing data (reads) are located
* fastqc - directory, which contains quality reports made with the FastQC program
* images - directory where the images placed in the report are located
* scripts - directory where the scripts used for analysis are located
* barplot.qzv - barplot file examining taxonomic composition, made with the QIIME program
* metadata.tsv - tsv file containing metadata from analyzed samples
* multiqc_report.html - quality report of samples made with MultiQC program
* rename_samples.tsv - tsv file containing new sample names
* samples.csv - csv file with metadata for all samples
* seqs_import.csv - csv file with instructions for importing sequences into QIIME software
* roooted_tree.qza - file with the phylogenetic tree of the analyzed ASVs
* table_output.qza - summary table of filtering results
* taxonomy.qza - file with the result of the taxonomic classification


## Usage

To run a script written in Python, go to the <i>./scripts</i> directory and in the terminal type the command:

```python 
python <file_name.py> 
```

where file_name.py is the name of the script.

The script in R is written in RMarkdown. All commands are run inside the script.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Authors
Julia Smolik
