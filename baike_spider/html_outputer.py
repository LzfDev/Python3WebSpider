# coding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset=\"UTF-8\">")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")

        fout.write("<tr>")
        fout.write("<td>%s</td>" % "url:")
        fout.write("<td>%s</td>" % "title:")
        fout.write("<td>%s</td>" % "para:")
        try:
        #ascii
            for data in self.datas:
                fout.write("<tr>")
                fout.write("<td>%s</td>" % data['url'])
                fout.write("<td>%s</td>" % data['title'])
                fout.write("<td>%s</td>" % data['para'])

        except Exception as e:
            print("write failed.")
            raise e

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()