import pandas as pd
from fpdf import FPDF

# Function to read data from a CSV file
def read_data(file_path):
    data = pd.read_csv(file_path)
    
    # Print the columns and first few rows to inspect
    print("Columns in the file:", data.columns.tolist())  # Print column names as a list
    print("First few rows of the data:")
    print(data.head())  # Print first few rows of the data to inspect the values
    
    # Clean up column names (remove leading/trailing spaces)
    data.columns = data.columns.str.strip()
    
    # Check if 'Marks' exists in the columns after cleanup
    if 'Marks' not in data.columns:
        print("Marks column is still missing!")
        # If the column is missing, we check for any spaces or issues
        print("Available columns:", data.columns.tolist())  # Print actual columns again

    return data

# Function to analyze the data
def analyze_data(data):
    # Ensure that 'Marks' column is present
    if 'Marks' not in data.columns:
        raise KeyError("'Marks' column is missing in the data!")

    analysis = {
        "average_marks": data['Marks'].mean(),
        "max_marks": data['Marks'].max(),
        "min_marks": data['Marks'].min(),
    }
    return analysis

# Function to generate a PDF report
def generate_pdf_report(analysis, data, output_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add a page
    pdf.add_page()
    
    # Set font
    pdf.set_font('Arial', 'B', 16)
    
    # Title of the report
    pdf.cell(200, 10, txt="Student Marks Analysis Report", ln=True, align='C')
    
    # Line break
    pdf.ln(10)
    
    # Add summary of the analysis
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt=f"Average Marks: {analysis['average_marks']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Maximum Marks: {analysis['max_marks']}", ln=True)
    pdf.cell(200, 10, txt=f"Minimum Marks: {analysis['min_marks']}", ln=True)
    
    # Line break
    pdf.ln(10)
    
    # Add a table with the original data
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80, 10, 'Name', border=1, align='C')
    pdf.cell(40, 10, 'Marks', border=1, align='C')
    pdf.ln()
    
    pdf.set_font('Arial', '', 12)
    for _, row in data.iterrows():
        pdf.cell(80, 10, row['Name'], border=1, align='C')
        pdf.cell(40, 10, str(row['Marks']), border=1, align='C')
        pdf.ln()
    
    # Output the PDF to a file
    pdf.output(output_filename)

# Main function to drive the script
def main():
    # Update file path to point to your specific file location
    file_path = r'C:\Users\admin\Documents\SYBScIT\data.csv'  # Use raw string to avoid issues with backslashes
    output_filename = 'student_marks_analysis_report.pdf'
    
    # Step 1: Read the data
    data = read_data(file_path)
    
    # Step 2: Analyze the data
    analysis = analyze_data(data)
    
    # Step 3: Generate the PDF report
    generate_pdf_report(analysis, data, output_filename)
    
    print(f"PDF report '{output_filename}' has been generated successfully!")

# Run the main function
if __name__ == "__main__":
    main()
