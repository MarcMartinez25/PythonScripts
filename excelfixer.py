import xlrd
import xlsxwriter

# For file_name be sure to type it in the following format
#     'filename.xlsx'

# The splitter is what you want to separate the text by
#     Ex: ','  ';' 
#    Also be sure to wrap the splitter like so: 'splitter'

# For the new_file_name be sure to type it in the following format
#    'newfilename.xlsx'
def workbook_readwrite(file_name, splitter, new_file_name):
    wb = xlrd.open_workbook(filename)
    sh1 = wb.sheet_by_index(0)
    contact = sh1.cell(rowx=0,colx=0).value
    li = contact.split(splitter)
    
    workbook = xlsxwriter.Workbook(new_file_name)
    worksheet = workbook.add_worksheet()
    
    for items in li:
    worksheet.write(r,0,items)
    r += 1
    
    workbook.close()

workbook_readwrite()