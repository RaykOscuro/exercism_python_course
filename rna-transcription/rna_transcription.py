def to_rna(dna_strand):
    """Transcribes a DNA strand into RNA."""
    dna_to_rna_mappings = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna_strand = "".join(dna_to_rna_mappings.get(nucleotide, "")
                         for nucleotide in dna_strand)
    return rna_strand
