# DNA Sequence Similarity Analysis Using BLAST

## 1. Project Overview

This project investigates DNA sequence similarity using the NCBI Basic Local Alignment Search Tool (BLAST).

A chloroplast DNA sequence from *Arabidopsis thaliana* was obtained from the NCBI Nucleotide database and analysed using BLASTN to identify similar sequences in the nucleotide database.

## 2. Biological Background

The **rbcL gene** encodes the large subunit of Ribulose-1,5-bisphosphate carboxylase/oxygenase (RuBisCO).

RuBisCO is an important enzyme involved in photosynthetic carbon fixation, where atmospheric carbon dioxide is incorporated into organic molecules.

The gene is located in the chloroplast genome.

## 3. Objectives

- Retrieve a real DNA sequence from NCBI.
- Understand the FASTA sequence format.
- Perform nucleotide sequence similarity searching using BLASTN.
- Interpret sequence identity, query coverage, E-value and alignment score.
- Understand how sequence alignment helps identify related DNA sequences.

## 4. Data Source

- Database: NCBI Nucleotide
- Organism: *Arabidopsis thaliana*
- Gene: rbcL
- Accession number: U91966.1
- Query length: 2,187 base pairs

NCBI record: https://www.ncbi.nlm.nih.gov/nuccore/U91966.1

## 5. Methodology

1. Retrieved the rbcL nucleotide sequence from NCBI.
2. Downloaded the sequence in FASTA format.
3. Submitted the sequence to NCBI BLASTN.
4. Selected the Nucleotide collection (nr/nt) database.
5. Examined the resulting sequence matches.
6. Inspected the pairwise alignment of a matching chloroplast sequence.
7. Recorded the alignment statistics and interpreted the findings.

## 6. Results

The query sequence produced highly similar matches in the nucleotide database.

One selected match was:

- Subject accession: OY747152.1
- Organism: *Arabidopsis thaliana*
- Query coverage: 100%
- Percentage identity: 99.82%
- E-value: 0.0
- Alignment score: 4,017 bits
- Identical positions: 2,183/2,187
- Gaps: 0

The alignment covered the complete query sequence.

## 7. Interpretation

The results demonstrate a high degree of sequence similarity between the query and the selected chloroplast sequence.

The alignment contained 2,183 identical positions out of 2,187 aligned positions, corresponding to approximately 99.82% sequence identity.

Four nucleotide positions differed, and no gaps were observed.

The high sequence identity and full query coverage indicate a highly significant sequence match.

## 8. Tools and Resources

- NCBI Nucleotide Database
- NCBI BLASTN
- Visual Studio Code
- GitHub

## 9. Project Files

- `rbcL.fasta` – Original DNA query sequence.
- `blast_results.txt` – Downloaded BLAST results.
- `README.md` – Project documentation.

## 10. Skills Developed

- Retrieving biological sequences from public databases.
- Understanding FASTA format.
- Performing nucleotide BLAST searches.
- Interpreting sequence alignment statistics.
- Understanding DNA sequence similarity.
- Scientific data documentation.

## 11. Conclusion

This project demonstrated how BLASTN can be used to compare nucleotide sequences and identify highly similar DNA regions.

It provided practical experience in accessing biological databases, conducting sequence similarity searches and interpreting molecular biology data.

---

**Author:** Evans Kioko
**GitHub:** [@Evanno000](https://github.com/Evanno000)
**Field:** Bioinformatics and Molecular Biology
