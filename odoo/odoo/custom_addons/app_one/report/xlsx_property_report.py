from ast import literal_eval

# noinspection PyUnresolvedReferences

from odoo import http
from odoo.http import request
import io
import xlsxwriter

class XlsxPropertyReport(http.Controller):
    @http.route('/property/excel/report/<string:property_ids>', type='http', auth='none')
    def download_excel_xlsx(self,property_ids):

        property_ids= request.env['property'].sudo().browse(literal_eval(property_ids))
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Properties')

        header_format = workbook.add_format({'bold': True, 'align': 'center', 'border':1,'bg_color':'#D3D3D3'})
        string_formate= workbook.add_format({'border':1,'align': 'center'})
        price_formate= workbook.add_format({'border':1,'align': 'center','num_format': '#,##0.00'})


        headers=['Name','Expected Date','Expected Price','Area','Description']
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, header_format)

        row_num = 1
        for property in property_ids:
            worksheet.write(row_num, 0, property.name,string_formate)
            worksheet.write(row_num, 1, property.expected_date,price_formate)
            worksheet.write(row_num, 2, property.expected_price,price_formate)
            worksheet.write(row_num, 3, property.area,price_formate)
            worksheet.write(row_num, 4, property.description,string_formate)
            row_num += 1

        workbook.close()
        output.seek(0)
        file_name='Properties.xlsx'

        return request.make_response(
            output.getvalue(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename=%s' % file_name)
            ]
        )