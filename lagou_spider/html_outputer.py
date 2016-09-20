#coding:utf-8
class HtmlOutputer(object):
    
    def __init__(self):
        self.datas=[]
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border=1>")
    
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['positionName'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['city'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['companyShortName'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['industryField'].encode('utf-8'))
            fout.write("<td>%s</td>"%data['salary'].encode('utf-8'))
            fout.write("<td><img src='http://www.lgstatic.com/thumbnail_120x120/%s' /></td>"%data['companyLogo'].encode('utf-8'))

            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
    



