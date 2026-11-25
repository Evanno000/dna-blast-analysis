
# DNA BLAST Analysis of the Arabidopsis thaliana QUA1 Transcript

## Project Overview

This project investigates sequence similarity of the QUA1 (QUA1 / AT3G25140) transcript from Arabidopsis thaliana using nucleotide BLAST (BLASTn).

The project combines biological database retrieval, nucleotide sequence handling, BLAST similarity analysis, data processing using Python, and graphical visualization.

The aim is to identify nucleotide sequence matches in the NCBI nucleotide database and explore the relationship between sequence identity and query coverage.

## Biological Background

QUA1 (QUARTET 1) is associated with plant cell wall biology and homogalacturonan-related processes.

The selected transcript was obtained from the National Center for Biotechnology Information (NCBI).

- Organism: Arabidopsis thaliana
- Gene: QUA1
- Gene locus: AT3G25140
- Transcript accession: NM_113418.5
- Sequence length: 2,290 nucleotides

## Objectives

1. Retrieve a nucleotide sequence from a biological database.
2. Perform nucleotide BLAST analysis.
3. Examine sequence identity and alignment coverage.
4. Process BLAST results using Python.
5. Export a structured dataset of BLAST hits.
6. Visualize sequence similarity results.

## Data Sources

### Query sequence

NCBI accession: NM_113418.5

NCBI Nucleotide:
https://www.ncbi.nlm.nih.gov/nuccore/NM_113418.5

The transcript sequence was downloaded in FASTA format.

### BLAST database

NCBI nucleotide database (nt).

BLAST tool:
https://blast.ncbi.nlm.nih.gov/Blast.cgi

Search settings:

- Program: BLASTn
- Search mode: Megablast / highly similar sequences
- Database: Nucleotide (nt)
- Organism filter: Arabidopsis thaliana
- Query: NM_113418.5

## Methodology

### 1. Sequence retrieval

The QUA1 transcript sequence was retrieved from NCBI and stored in FASTA format.

### 2. BLASTn search

The transcript was submitted to NCBI BLASTn to identify nucleotide sequence matches.

### 3. Data processing

The BLAST hit table was downloaded and processed using Python.

The analysis used:

- Biopython for FASTA sequence handling
- Pandas for tabular data processing
- Matplotlib for visualization

### 4. Query coverage estimation

Query coverage was estimated using the query alignment coordinates:

Estimated query coverage (%) = (query coordinate span / query length) × 100

This is a coordinate-span estimate and may differ from NCBI's reported coverage in alignments involving gaps or multiple alignment segments.

### 5. Visualization

The top 10 non-self BLAST hits were selected based on bit score.

Two plots were generated:

- Percent identity
- Estimated query coverage

The query's self-match was excluded from these plots to make comparisons among other database hits more informative.

## Results

The BLAST search returned 295 hits.

The query sequence itself appeared as the top match, with:

- Percent identity: 100%
- Alignment length: 2,290 nucleotides
- Query coverage: 100%
- E-value: 0.0 as displayed by NCBI
- Bit score: 4,229

The second hit, AY099574.1, showed:

- Percent identity: 100%
- Alignment length: 1,918 nucleotides
- Estimated query coverage: approximately 83.76%
- Bit score: 3,542

The third hit, BX823546.1, showed:

- Percent identity: 99.84%
- Alignment length: 1,873 nucleotides
- Estimated query coverage: approximately 81.79%
- Bit score: 3,443

Several additional hits showed high sequence identity but lower query coverage.

## Interpretation

The BLAST results demonstrate strong nucleotide sequence similarity between the selected QUA1 transcript and multiple sequences in the nucleotide database.

The second hit had 100% identity over approximately 83.76% of the query, demonstrating that identity and coverage describe different aspects of sequence similarity.

A high identity percentage does not necessarily mean that the entire query sequence is represented in the alignment.

The results support sequence similarity but do not independently establish the biological function of every matching sequence.

The self-match is expected because the query sequence was included in the nucleotide database.

An E-value displayed as 0.0 by BLAST represents a value below the display precision, rather than a mathematically literal zero.

## Limitations

- The BLAST search was restricted to Arabidopsis thaliana.
- Database contents may change over time.
- Estimated query coverage was calculated from query-coordinate span.
- Sequence similarity alone does not establish biological function.
- The query's own database match is expected and was excluded from the visualization.
- The analysis represents a particular database search and is not an exhaustive functional investigation.

## Technologies Used

- Python
- Biopython
- Pandas
- Matplotlib
- NCBI BLAST
- NCBI Nucleotide database
- FASTA
- CSV
- TSV

## Project Structure

dna-blast-analysis/
├── data/
│   ├── query_sequence.fasta
│   └── qua1_transcript.fasta
├── results/
│   ├── sequence_summary.txt
│   ├── qua1_blast_results.tsv
│   ├── blast_summary.csv
│   ├── blast_identity_plot.png
│   └── blast_identity_coverage.png
├── blast_analysis.py
├── requirements.txt
└── README.md

## Reproducibility

Clone the repository and install the dependencies:

pip install -r requirements.txt

Run the analysis:

python blast_analysis.py

The script generates a CSV summary and graphical visualization in the results directory.

The original BLAST results table is retained to allow reprocessing without repeating the database search.

## Author

Evans Kioko

Computational Biology | Bioinformatics | Biochemistry
