from datetime import datetime
import pytz

bogota_timeZone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timeZone)
print(f'Bogotá: {bogota_date.strftime("%d/%m/%y, %H:%M:%S")}')

cdmx_timeZone = pytz.timezone("America/CDMX")
cdmx_date = datetime.now(cdmx_timeZone)
print(f'CDMX: {cdmx_date.strftime("%d/%m/%y, %H:%M:%S")}')