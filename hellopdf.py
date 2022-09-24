# Import the required Module
import tabula
# Read a PDF File
#df = tabula.read_pdf("/home/matt/anz-stmt.pdf", pages='all')
# convert PDF into CSV
#df.to_csv('/home/matt/anz-stmt.csv', encoding='utf-8')
# print(df)
# convert PDF into CSV file
tabula.convert_into("/home/matt/anz-stmt.pdf",
                    "/home/matt/anz-stmt.csv", output_format="csv", pages='all')
print('done')
