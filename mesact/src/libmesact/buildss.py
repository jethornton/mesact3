import os, traceback
from datetime import datetime



def build(parent):
	file_path = os.path.join(parent.config_path, 'sserial.hal')
	parent.info_pte.appendPlainText(f'Building {file_path}')
	if parent.ss_card_cb.currentData():
		contents = []
		contents = ['# This file was created with the Mesa Configuration Tool on ']
		contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
		contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n')







	try:
		with open(file_path, 'w') as f:
			f.writelines(contents)
	except OSError:
		parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')

