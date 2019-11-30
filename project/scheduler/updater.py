from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from sold.models import Sold
from django.core.mail import EmailMessage
import xlwt
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_email, 'interval', hours=24)
    scheduler.start()
    


def send_email ():
        msg = EmailMessage('Subject of the Email', 'Body of the email', 'enigma7t7@gmail.com', ['reza_avd@yahoo.com'])
        msg.content_subtype = "html"  
        msg.attach_file(write_excel())
        sent_email()
        msg.send()

def sent_email ():
    sent = Sold.objects.filter(بررسی_شده=False)
    for item in sent:
        item.بررسی_شده = True
        item.save()



def write_excel():
    filename = foo()
    excel_file = xlwt.Workbook(encoding='utf-8')
    sheet = excel_file.add_sheet('Sold')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['کاربر', 'نام محصول', 'مدل', 'سایز', 'تعداد', 'قیمت']

    for col_num in range(len(columns)):
        sheet.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Sold.objects.filter(بررسی_شده=False).values_list('user', 'name', 'model', 'size', 'number', 'price')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            sheet.write(row_num, col_num, row[col_num], font_style)
    excel_file.save(filename) 
    return filename

def foo():
   dirname = datetime.now().strftime('%Y.%m.%d.%H.%M.%S') #2010.08.09.12.08.45 
   os.mkdir(os.path.join('daily_email', dirname))
   first = "daily_email/"
   name = "/daily_purchase.xls"
   result =first + dirname + name
   return result  
