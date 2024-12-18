import xlsxwriter
from calendar import monthrange, month_name
from datetime import datetime

class HorizontalCalendar:
    def __init__(self, year, output_path, mode):
        self.year = year
        self.output_path = output_path
        self.mode = mode
        self.weekdays = ["L", "M", "X", "J", "V", "S", "D"]
        self.workbook = None
        self.worksheet = None

    def create_month_sheet(self, month, start_row=0):
        days_in_month = monthrange(self.year, month)[1]
        first_weekday = monthrange(self.year, month)[0]

        self.worksheet.write(start_row, 0, month_name[month])

        for col, weekday in enumerate(self.weekdays):
            self.worksheet.write(start_row + 1, col, weekday)

        col = first_weekday
        for day in range(1, days_in_month + 1):
            self.worksheet.write(start_row + 2, col, day)
            col += 1

        self.worksheet.set_column(0, 6, 4)

    def create_calendar(self):
        try:
            self.workbook = xlsxwriter.Workbook(self.output_path)
            if self.mode == "s":
                self.worksheet = self.workbook.add_worksheet("Calendario")
                start_row = 0
                for month in range(1, 13):
                    self.create_month_sheet(month, start_row)
                    start_row += 4  # Espacio entre meses
            else:
                for month in range(1, 13):
                    self.worksheet = self.workbook.add_worksheet(month_name[month])
                    self.create_month_sheet(month)
            self.workbook.close()
            print(f"Calendario guardado en: {self.output_path}")
        except Exception as e:
            print(f"Error al crear el calendario: {e}")
            if self.workbook:
                self.workbook.close()

# Solicitar al usuario el año y el modo
try:
    year_input = input("Introduce el año (ej. 2025): ")
    year = int(year_input) if year_input else datetime.now().year
    mode = input("¿Deseas guardar todos los meses en la misma hoja (s/n)?: ")
    output_path = f"Calendario_{year}.xlsx"

    if 1 <= year <= 9999:
        HorizontalCalendar(year, output_path, mode).create_calendar()
    else:
        print("Año no válido. Debe estar en el rango de 1 a 9999.")
except ValueError:
    print("Entrada no válida. Por favor, introduce un año válido.")