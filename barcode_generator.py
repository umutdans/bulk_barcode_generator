import csv
import os
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcodes_from_csv(csv_file_path, output_dir):
    # Create a unique directory inside the output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    barcode_dir = os.path.join(output_dir, f"barcodes_{timestamp}")
    os.makedirs(barcode_dir, exist_ok=True)

    # Read data from CSV file
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for data in row:
                # Generate barcode
                barcode = Code128(data, writer=ImageWriter())
                # Save barcode as image
                barcode.save(os.path.join(barcode_dir, data))

if __name__ == "__main__":
    # Hide the root window
    Tk().withdraw()
    # Open file dialog to select CSV file
    csv_file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        # Set output directory to the same directory as the script
        output_dir = os.path.dirname(os.path.abspath(__file__))
        generate_barcodes_from_csv(csv_file_path, output_dir)