import xlsxwriter
from calendar import monthrange, month_name

#esta versión hace un calendario horizontal con cada mes en una distintas hojas

class HorizontalCalendar:
    def __init__(self, year, output_path):
        self.year = year
        self.output_path = output_path
        self.weekdays = ["L", "M", "X", "J", "V", "S", "D"]
        self.workbook = None

    def create_month_sheet(self, month):
        days_in_month = monthrange(self.year, month)[1]
        first_weekday = monthrange(self.year, month)[0]
        days = list(range(1, days_in_month + 1))
        weekday_labels = [self.weekdays[(first_weekday + i) % 7] for i in range(days_in_month)]
        worksheet = self.workbook.add_worksheet(month_name[month])

        for col, weekday in enumerate(weekday_labels):
            worksheet.write(0, col, weekday)

        for col, day in enumerate(days):
            worksheet.write(1, col, day)

        worksheet.set_column(0, days_in_month - 1, 4)

    def create_calendar(self):
        try:
            self.workbook = xlsxwriter.Workbook(self.output_path)
            for month in range(1, 13):
                self.create_month_sheet(month)
            self.workbook.close()
            print(f"Calendario guardado en: {self.output_path}")
        except Exception as e:
            print(f"Error al crear el calendario: {e}")
            if self.workbook:
                self.workbook.close()

# Solicitar al usuario el año
try:
    year = int(input("Introduce el año (ej. 2025): "))
    output_path = f"Calendario_{year}.xlsx"

    if 1 <= year <= 9999:
        HorizontalCalendar(year, output_path).create_calendar()
    else:
        print("Año no válido. Debe estar en el rango de 1 a 9999.")
except ValueError:
    print("Entrada no válida. Por favor, introduce un año válido.")

# Solicitar al usuario el año
try:
    year_input = input("Introduce el año (ej. 2025): ")
    year = int(year_input) if year_input else datetime.now().year
    output_path = f"Calendario_{year}.xlsx"

    if 1 <= year <= 9999:
        HorizontalCalendar(year, output_path).create_calendar()
    else:
        print("Año no válido. Debe estar en el rango de 1 a 9999.")
except ValueError:
    print("Entrada no válida. Por favor, introduce un año válido.")
