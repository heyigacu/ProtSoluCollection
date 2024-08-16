from Bio import SeqIO
import csv

# Paths to input and output files
input_fasta_path = "input.fasta"
output_csv_path = "Predict/NEED_to_PREPARE/list.csv"

# Open the CSV file for writing
with open(output_csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['id', 'sequence'])  # Write the header row

    # Parse the input FASTA file
    for record in SeqIO.parse(input_fasta_path, "fasta"):
        # Write each sequence to a separate FASTA file
        fasta_filename = f"Predict/NEED_to_PREPARE/fasta/{record.id}.fasta"
        with open(fasta_filename, 'w') as fasta_file:
            SeqIO.write(record, fasta_file, "fasta")
        
        # Write the ID and sequence to the CSV file
        csvwriter.writerow([record.id, str(record.seq)])

print("Processing complete.")
