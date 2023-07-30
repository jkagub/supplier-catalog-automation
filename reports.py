#!/usr/bin/env python3

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file_path, title, paragraph):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    report_title = reportlab.platypus.Paragraph(title, styles["h1"])

    # Split the paragraph into separate lines
    lines = paragraph.split("name: ")

    # Create a list to store the data in the required format
    table_data = []

    # Iterate through each line in the paragraph, skipping the first empty entry
    for line in lines[1:]:
        data = line.strip().split("weight: ")
        if len(data) == 2:
            name, weight = data
            # Append the name and weight as separate rows to the table data list
            table_data.append([f"name: {name.strip()}", f"weight: {weight.strip()}"])
        else:
            # Handle lines with incorrect format or empty lines
            # You can add custom logic here, such as skipping the line or logging a warning.
            pass

    # Create the table with the updated table_data
    report_table = Table(table_data)

    report_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    report_elements = [report_title, report_table]
    doc.build(report_elements)