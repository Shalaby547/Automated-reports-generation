from openpyxl import load_workbook
from pptx import Presentation
from pptx.util import Pt, Cm
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.util import Inches
import os
from pptx.dml.color import RGBColor

class Colors:

    GREEN_BG = RGBColor(198, 239, 206)
    GREEN_WORD = RGBColor(46, 125, 50)

    RED_BG = RGBColor(255, 199, 206)
    RED_WORD = RGBColor(156, 0, 6)

    YELLOW_BG = RGBColor(255, 235, 156)
    YELLOW_WORD = RGBColor(156, 101, 0)

    EXCELLENT_WORD = RGBColor(46, 125, 50)    # #2E7D32
    VERY_GOOD_WORD  = RGBColor(76, 175, 80)    # #4CAF50
    GOOD_WORD  = RGBColor(110, 180, 126)  # #81C784

width_map = {
    "Very Good": Cm(3),
    "Good": Cm(2.0),
    "Not Submitted": Cm(4),
    "Needs Improvement": Cm(4.5),
}
templates = {
    (1, False): "Template1Q.pptx",
    (2, False): "Template2Q.pptx",
    (3, False): "Template3Q.pptx",
    (4, False): "Template4Q.pptx",

    (1, True): "Template1QME.pptx",
    (2, True): "Template2QME.pptx",
    (3, True): "Template3QME.pptx",
    (4, True): "Template4QME.pptx"
}


File= input("Enter file name : ")
Quiz_count= int(input("Enter Quiaz Nomber: "))
has_monthly_exam = input("Monthly exam true or false: ").lower() == "true"
month = input("enter month :")
session_nomber= int(input("How many sessions?"))

def performance_monthly_location_determination(session_nomber):
 
 if session_nomber==4:
    
      Montly_location=19
      performance_location=20

 elif session_nomber==8:
      Montly_location=35
      performance_location=36

 return Montly_location,performance_location

monthly_location,performance_location= performance_monthly_location_determination(session_nomber)

File_name= str(File)
File_report= File_name + " Reports"
template_name = templates[(Quiz_count, has_monthly_exam)]

excel_path = fr"D:\Bassant\{File_name}\{File_name}.xlsx"
template_path = fr"D:\Bassant\Templates\{template_name}"
output_folder = fr"D:\Bassant\{File_name}\{File_report}"

# =====================
# Open Excel
# =====================

wb = load_workbook(excel_path, data_only=True)
ws = wb.active

print("Excel opened successfully.\n")

# =====================
# Read categories once
# =====================

categories = []

for row in range(3, 35):
    categories.append(ws.cell(row, 2).value)

print("Categories loaded.\n")

# =====================
# Students dictionary
# =====================

students = {}

# =====================
# Read students
# =====================

for col in range(3, ws.max_column + 1):

    student_name = ws.cell(2, col).value

    if student_name is None:
        continue

    print("Student:", student_name)

    attendance = []
    homework = []
    quizzes = []

    quiz_counter = 0
    monthly_exam = ""

    for row in range(3, 35):

        category = categories[row - 3]

        value = ws.cell(row, col).value

        if value is None:
            continue

        value = str(value).strip()

        # Attendance
        if category == "Attendance":
            attendance.append(value)

        # Homework
        elif category == "Homework":
            homework.append(value)

        # Quiz1 and Quiz2
        elif "Quiz" in str(category):
             quizzes.append(value)
             

        # Monthly Exam 
    monthly_exam = ws.cell(monthly_location, col).value
    overall_performance = ws.cell(performance_location, col).value

    print("Attendance:", attendance)
    print("Homework :", homework)
    print(" quizzes degrees :", quizzes)
    print("Exam     :", monthly_exam)

    students[student_name] = {
        "attendance": attendance,
        "homework": homework,
        "quizzes":quizzes,
        "monthly_exam": monthly_exam,
        "overall_performance": overall_performance
    }

    print("-----------------------")

# ==========================
# Create PowerPoints
# ==========================

for student, data in students.items():

    print("Creating report for:", student)

    prs = Presentation(template_path)

    replacements = {
        "Studentname": student,
        "ME": str(data["monthly_exam"])+"%",
        "GRADE": str(data["overall_performance"]),
        "period": month
        #"ME": f'{data["monthly_exam"]:.0%}',
    }
    # Quizzes placeholders
    for i, quiz in enumerate(data["quizzes"], start=1):
        replacements[f"Q{i}"] = quiz

    # Attendance placeholders
    for i in range(8):

        if i < len(data["attendance"]):
            replacements[f"AT{i+1}"] = str(data["attendance"][i])
        else:
            replacements[f"AT{i+1}"] = ""

    # Homework placeholders
    for i in range(8):

        if i < len(data["homework"]):
            replacements[f"HW{i+1}"] = str(data["homework"][i])
        else:
            replacements[f"HW{i+1}"] = ""

    

    # ======================
    # Replace in slides
    # ======================

        # ======================
    # Replace in slides
    # ======================

    table_count = 0

    for slide in prs.slides:

        for shape in slide.shapes:

            # -------------------------
            # Text Boxes
            # -------------------------
            if shape.has_text_frame:
            

                text = shape.text

                for old, new in replacements.items():
                    text = text.replace(old, new)

                shape.text = text
                
                # تنسيق اسم الطالب فقط
                if student in shape.text:

                    paragraph = shape.text_frame.paragraphs[0]
                    paragraph.alignment = PP_ALIGN.CENTER

                    if paragraph.runs:

                        run = paragraph.runs[0]

                        run.font.size = Pt(32)
                        run.font.bold = True

                        # اللون الوردي الموجود في الصورة
                        run.font.color.rgb = RGBColor(212, 76, 152)
  #صفات الخط في التقييم النهائي 

                if month in shape.text:

                    for paragraph in shape.text_frame.paragraphs:

                        paragraph.alignment = PP_ALIGN.CENTER

                        for run in paragraph.runs:

                            run.font.size = Pt(16)
                            run.font.bold = True
                            run.font.color.rgb = RGBColor(255, 255, 255)        
                
                
                if shape.text == "Overall Performance":
                    p = shape.text_frame.paragraphs[0]
                    p.text = "Overall Performance"
                    p.alignment = PP_ALIGN.CENTER

                    font = p.runs[0].font
                    font.bold = True
                    font.size = Pt(20)

                if shape.text == str(data["overall_performance"]):

                    p = shape.text_frame.paragraphs[0]
                    p.alignment = PP_ALIGN.CENTER

                    font = p.runs[0].font
                    font.bold = True
                    font.size = Pt(20)

    # ==========================

                # -------------------------
            # Tables
            # -------------------------
            if shape.has_table:

                table = shape.table

                first_cell = table.cell(0, 0).text

                if "Quiz" in first_cell:
                    shape.top += Cm(1)

                table = shape.table

                for r, row in enumerate(table.rows):

                    for c, cell in enumerate(row.cells):

                        text = cell.text

                        for old, new in replacements.items():
                            text = text.replace(old, new)

                        cell.text = text

                        # هنا بالظبط
                        if text in width_map:
                            table.columns[c].width = width_map[text]

                        paragraph = cell.text_frame.paragraphs[0]
                        paragraph.alignment = PP_ALIGN.CENTER

                        if paragraph.runs:

                           run = paragraph.runs[0]

                           run.font.size = Pt(14)
                           run.font.bold = True

                           value = text.strip()

                        if value in ("Absent", "Not Submitted"):
                                run.font.color.rgb = Colors.RED_WORD

                        elif value == "Needs Improvement":
                                run.font.color.rgb = Colors.YELLOW_WORD

                        elif value == "Good":
                                run.font.color.rgb = Colors.GOOD_WORD

                        elif value == "Very Good":
                                run.font.color.rgb = Colors.VERY_GOOD_WORD

                        elif value in ("Excellent", "Present"):
                                run.font.color.rgb = Colors.EXCELLENT_WORD

                        elif value == "Awesome":
                                run.font.color.rgb = Colors.AWESOME_WORD
                    


    save_path = os.path.join(
        output_folder,
        f"{student}.pptx"
    )
    print(data["overall_performance"])
    print("Saving:", save_path)

    prs.save(save_path)

print("\nAll reports created successfully.")