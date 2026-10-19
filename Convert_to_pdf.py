import os
import win32com.client


# Ask for file name
file_name = input("Enter your file name: ")


# Base folder
base_folder = r"D:\Bassant"


# Reports folder
reports_folder = os.path.join(
    base_folder,
    file_name,
    file_name + " Reports"
)


print("Reports folder:", reports_folder)


# Check if folder exists
if not os.path.exists(reports_folder):

    print("ERROR: Reports folder does not exist.")
    print("Path:", reports_folder)

    exit()


def convert_to_pdf(pptx_path):

    try:

        # Create PDF path in the same folder
        pdf_path = os.path.splitext(pptx_path)[0] + ".pdf"

        # Open PowerPoint
        presentation = powerpoint.Presentations.Open(
            pptx_path,
            WithWindow=False
        )

        # Save as PDF
        presentation.SaveAs(
            pdf_path,
            32
        )

        # Close presentation
        presentation.Close()

        # Check if PDF was created
        if os.path.exists(pdf_path):

            return True

        return False

    except Exception as e:

        print(f"Error: {e}")

        return False


# Open PowerPoint
powerpoint = win32com.client.Dispatch(
    "PowerPoint.Application"
)

powerpoint.Visible = True


# Loop through all files in the Reports folder
for file in os.listdir(reports_folder):

    # Only process PowerPoint files
    if file.lower().endswith(".pptx"):

        # Full path of PowerPoint file
        pptx_path = os.path.join(
            reports_folder,
            file
        )

        print(f"\nConverting: {file}")

        # Convert PowerPoint to PDF
        success = convert_to_pdf(pptx_path)

        if success:

            # Delete PowerPoint only after successful conversion
            os.remove(pptx_path)

            print(f"Successfully converted: {file}")
            print(f"Deleted PowerPoint: {file}")

        else:

            print(f"FAILED: {file}")
            print("PowerPoint was NOT deleted.")


# Close PowerPoint
powerpoint.Quit()


print("\nConversion process finished.")