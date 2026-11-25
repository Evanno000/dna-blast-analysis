
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO


# ==========================================
# PATH CONFIGURATION
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parent

QUERY_FILE = PROJECT_DIR / "data" / "qua1_transcript.fasta"
BLAST_FILE = PROJECT_DIR / "results" / "qua1_blast_results.tsv"
CSV_OUTPUT = PROJECT_DIR / "results" / "blast_summary.csv"
GRAPH_OUTPUT = PROJECT_DIR / "results" / "blast_identity_coverage.png"


# ==========================================
# BLAST ANALYSIS
# ==========================================

def main():

    print("=" * 50)
    print("       QUA1 BLAST RESULTS ANALYSIS")
    print("=" * 50)

    try:

        # Load query sequence
        query_record = SeqIO.read(QUERY_FILE, "fasta")
        query_length = len(query_record.seq)

        query_accession = query_record.id

        print(f"Query: {query_accession}")
        print(f"Query length: {query_length} nt")

        # BLAST table columns
        columns = [
            "query_accession",
            "subject_accession",
            "percent_identity",
            "alignment_length",
            "mismatches",
            "gap_opens",
            "query_start",
            "query_end",
            "subject_start",
            "subject_end",
            "evalue",
            "bit_score",
        ]

        # Read BLAST results
        df = pd.read_csv(
            BLAST_FILE,
            sep="\t",
            comment="#",
            header=None,
            names=columns
        )

        # Convert numerical columns
        numeric_columns = [
            "percent_identity",
            "alignment_length",
            "mismatches",
            "gap_opens",
            "query_start",
            "query_end",
            "subject_start",
            "subject_end",
            "evalue",
            "bit_score",
        ]

        for column in numeric_columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

        df = df.dropna(subset=numeric_columns)

        # Estimate query coverage from query coordinates
        query_span = (
            (df["query_end"] - df["query_start"]).abs() + 1
        )

        df["query_coverage"] = (
            query_span / query_length * 100
        ).clip(upper=100)

        # Sort hits by bit score
        df = df.sort_values(
            by="bit_score",
            ascending=False
        )

        # Export all analysed hits
        df.to_csv(CSV_OUTPUT, index=False)

        # Exclude the query's self-match from the visualization
        non_self_hits = df[
            df["subject_accession"] != query_accession
        ].copy()

        # Select top 10 non-self hits
        top_hits = non_self_hits.head(10).copy()

        print(f"Total hits analysed: {len(df)}")
        print("\nTOP 10 NON-SELF BLAST HITS")
        print("-" * 50)

        display_columns = [
            "subject_accession",
            "percent_identity",
            "query_coverage",
            "evalue",
            "bit_score",
        ]

        print(
            top_hits[display_columns].to_string(
                index=False,
                float_format=lambda x: f"{x:.2f}"
            )
        )

        # ==========================================
        # VISUALIZATION
        # ==========================================

        labels = top_hits["subject_accession"].tolist()

        identities = top_hits["percent_identity"].tolist()

        coverages = top_hits["query_coverage"].tolist()

        fig, axes = plt.subplots(
            1,
            2,
            figsize=(14, 7)
        )

        # Identity plot
        axes[0].barh(
            labels,
            identities
        )

        axes[0].set_title(
            "Percent Identity of Top 10 BLAST Hits"
        )

        axes[0].set_xlabel("Percent Identity (%)")

        axes[0].set_xlim(0, 105)

        axes[0].invert_yaxis()

        # Coverage plot
        axes[1].barh(
            labels,
            coverages
        )

        axes[1].set_title(
            "Estimated Query Coverage of Top 10 Hits"
        )

        axes[1].set_xlabel("Query Coverage (%)")

        axes[1].set_xlim(0, 105)

        axes[1].invert_yaxis()

        # Figure title
        fig.suptitle(
            "BLASTn Analysis of Arabidopsis thaliana QUA1 Transcript",
            fontsize=14
        )

        fig.tight_layout()

        # Save figure
        fig.savefig(
            GRAPH_OUTPUT,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close(fig)

        # ==========================================
        # COMPLETION
        # ==========================================

        print("\n" + "=" * 50)

        print(f"CSV saved: {CSV_OUTPUT}")

        print(f"Graph saved: {GRAPH_OUTPUT}")

        print("=" * 50)

    except FileNotFoundError as error:

        print("\nERROR: Required file not found.")
        print(error)

    except Exception as error:

        print("\nERROR DURING ANALYSIS:")
        print(error)


if __name__ == "__main__":
    main()
