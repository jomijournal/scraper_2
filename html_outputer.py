#utf8

class HtmlOutputer(object):
	def __init__(self):
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = open('output.html', 'w+')

		fout.write('<html>')
		fout.write('<body>')
		fout.write('<table>')
        
        #python default: ascii
		for data in self.datas:

			fout.write('<tr>')
			# fout.write('<td>%s</td>'% data['url'])
			if 'name' in data:
				fout.write('<td>%s</td>'% data['name'])#.encode('utf-8'))
			if 'email' in data:
				fout.write('<td>%s</td>'% data['email'])#.encode('utf-8'))
			fout.write('</tr>')

		fout.write('</table>')
		fout.write('</body>')	
		fout.write('</html>')
		fout.close
