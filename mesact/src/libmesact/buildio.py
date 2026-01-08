import os
from datetime import datetime

from libmesact import io

def build_io(parent):
	file_path = os.path.join(parent.config_path, 'io.hal')
	parent.info_pte.appendPlainText(f'Building {file_path}')
	contents = []
	contents = ['# This file was created with the Mesa Configuration Tool on ']
	contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n')

	contents.append('\n# Inputs\n')

	

	#main_boards = ['5i25', '5i25T', '6i25', '7i92', '7i92T']
	#print(f'hm2_{parent.board_0_hal_name}.0.')
	#print(f'{parent.board_cb.currentText()}')
	#print(f'{parent.daughter_cb_1.currentText()}')
	#print(f'{parent.daughter_cb_2.currentText()}')

	#c0_board_tw
	# intput tab index is 7 and output tab index is 8
	# main_tw boards tab index is 3, 4 and 5
	#
	#db1 = parent.board_1_hal_name
	#db2 = parent.board_2_hal_name

	# key is hal name, value is hm2
	main_board_hm2 = {
	'7i76e': 'hm2_7i76e.0.7i76.0.0.',
	'7i95': 'hm2_7i95.0.',
	'7i96': 'hm2_7i96.0.',
	'7i96s': 'hm2_7i96s.0.',
	'7i97': 'hm2_7i97.0.',}
	daughter_ports = {'7i76': ['2', '0'], '7i77': ['3', '0']}
	mb = parent.board_0_hal_name
	input_names = {
	'7i76': 'input-',
	'7i76e': 'input-',
	'7i77': 'input-',
	'7i95': 'iinmux.00.input-',
	'7i96': 'gpio.0',
	'7i96s': 'inm.00.input-',
	'7i97': 'inmux.00.input-'}

	for i in range(3): # determine if the main_tw board tab is visible
		if getattr(parent, f'main_tw').isTabVisible(i + 3): # board tab
			if getattr(parent, f'c{i}_board_tw').isTabVisible(7): # inputs tab
				invert = '_not' if mb == '7i96' else '-not'
				if i == 0: # it's a mother board create hm2
					hm2 = main_board_hm2[mb]
				if i > 0: # it's a daughter board create hm2
					daughter = f'{getattr(parent, f"board_{i}_hal_name")}'
					port = daughter_ports[daughter][i-1]
					hm2 = f'hm2_{mb}.0.{daughter}.0.{port}.'
				for j in range(32):
					input_pb = getattr(parent, f'c{i}_input_{j}')
					if input_pb.isEnabled() and input_pb.text() != 'Select':
						hal = f'{hm2}{input_names[daughter]}{j:02d}'
						invert_cb = getattr(parent, f'c{i}_input_invert_{j}')
						slow_cb = getattr(parent, f'c{i}_input_debounce_{j}')
						if invert_cb.isChecked():
							hal += invert

						print(f'hal {hal}')
						#c0_input_invert_0
						#c0_input_debounce_0


						pass
						#print(f'{io.inputs[input_pb.text()]}')
						#print(f'{j}', end=' ')
				#print(' Inputs Processed')


			if getattr(parent, f'c{i}_board_tw').isTabVisible(8): # outputs tab
				#print(f'Processing Outputs for board {i}')
				#print('Outputs', end=' ')
				for k in range(16):

					output_pb = getattr(parent, f'c{i}_output_{k}')
					if output_pb.isEnabled() and output_pb.text() != 'Select':
						pass
						#print(f'{io.outputs[output_pb.text()]}')
						#print(f'{k}', end=' ')
				#print(' Outputs Processed')

	return

	#c0_input_0
	#c0_input_invert_0
	#c0_input_debounce_0

	#for i in range(3):
	#	if getattr(parent, f'c{i}_board_tw').isTabVisible(7):
	#		print(f'Processing Inputs for board {i}')

	#c0_output_0
	#c0_output_invert_0
	#c0_output_type_0


	try:
		with open(file_path, 'w') as f:
			f.writelines(contents)
	except OSError:
		parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')
