import csv
import os
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcodes_from_csv(csv_file_path, output_dir):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    barcode_dir = os.path.join(output_dir, f"barcodes_{timestamp}")
    os.makedirs(barcode_dir, exist_ok=True)

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for data in row:
                barcode = Code128(data, writer=ImageWriter())
                barcode.save(os.path.join(barcode_dir, data))

if __name__ == "__main__":
    Tk().withdraw()
    csv_file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        output_dir = os.path.dirname(os.path.abspath(__file__))
        generate_barcodes_from_csv(csv_file_path, output_dir)
