import os, subprocess, requests, shutil
from datetime import datetime
from functools import partial

from PyQt6.QtWidgets import QLineEdit, QComboBox, QDoubleSpinBox, QCheckBox
from PyQt6.QtWidgets import QFileDialog, QLabel, QPushButton

from libmesact import dialogs

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

def check_emc():
	cp = subprocess.run(['pgrep', '-l', 'linuxcnc'], text=True, capture_output=True)
	if 'linuxcnc' in cp.stdout:
		return True
	else:
		return False

def new_config(parent):
	# set main tab visibility
	parent.main_tw.setTabVisible(3, False)
	parent.main_tw.setTabVisible(4, False)
	parent.main_tw.setTabVisible(5, False)
	parent.main_tw.setTabVisible(6, False)

	# clear all entries
	for child in parent.findChildren(QPushButton):
		if child.menu() is not None:
			child.setText('Select')
	for child in parent.findChildren(QComboBox):
		child.setCurrentIndex(0)
	for child in parent.findChildren(QLineEdit):
		child.clear()
	for child in parent.findChildren(QComboBox):
		child.setCurrentIndex(0)
	for child in parent.findChildren(QDoubleSpinBox):
		child.setValue(0)
	for child in parent.findChildren(QCheckBox):
		child.setChecked(False)
	parent.servo_period_sb.setValue(1000000)
	parent.intro_graphic_le.setText('emc2.gif')
	parent.main_tw.setCurrentIndex(0)

def startup_file(parent):
	dialog = QFileDialog(parent)
	dialog.setWindowTitle("Select a NC Code File")
	dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
	dialog.setDirectory(f'{os.path.expanduser("~/linuxcnc/nc_files")}')
	dialog.setNameFilter('NC Code Files (*.ngc *.NGC)')
	dialog.setOption(QFileDialog.Option.DontUseNativeDialog)
	if dialog.exec():
		source_path = dialog.selectedFiles()[0]
		parent.startup_file_le.setText(os.path.basename(source_path))

def select_flex_ui(parent):
	if not parent.machine_name:
		msg = ('In order to copy the Qt Designer\n'
		'file the Machine Name can not be blank.\n'
		'Enter the Machine Name so the\n'
		'configuration path can be created\n'
		'and the selected UI file can be\n'
		'copied to the configuration directory.')
		dialogs.msg_error_ok(parent, msg, 'Error')
		return

	dialog = QFileDialog(parent)
	dialog.setWindowTitle("Select a Designer ui File")
	dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
	dialog.setDirectory(f'{os.path.expanduser("~")}')
	dialog.setNameFilter('QT Designer File (*.ui)')
	dialog.setOption(QFileDialog.Option.DontUseNativeDialog)
	if dialog.exec():
		source_path = dialog.selectedFiles()[0]
		#print("Selected file:", file_name)
		#parent.flex_gui_path_lb.setText(os.path.dirname(source_path))
		parent.flex_gui_lb.setText(os.path.basename(source_path))
		# copy the file to the configuration directory if not there
		ui_name = os.path.basename(source_path)
		target_path = os.path.join(parent.config_path, ui_name)

		if not os.path.isfile(target_path):
			shutil.copy2(source_path, parent.config_path)

'''
match True:
	case (variable > 10):
		print("Variable is greater than 10")
	case (variable < 10):
		print("Variable is less than 10")
	case _:
		print("Variable is exactly 10 or condition is not met")
'''

def select_flex_qss(parent):
	if not parent.machine_name:
		msg = ('In order to copy the QSS file\n'
		'the Machine Name can not be blank.\n'
		'Enter the Machine Name so the\n'
		'configuration path can be created\n'
		'and the selected QSS file can be\n'
		'copied to the configuration directory.')
		dialogs.msg_error_ok(parent, msg, 'Error')
		return

	dialog = QFileDialog(parent)
	dialog.setWindowTitle("Select a QT qss File")
	dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
	dialog.setDirectory(f'{os.path.expanduser("~")}')
	dialog.setNameFilter('QT Stylesheet File (*.qss)')
	dialog.setOption(QFileDialog.Option.DontUseNativeDialog)
	if dialog.exec(): # a file was chosen
		source_path = dialog.selectedFiles()[0]
		qss_name = os.path.basename(source_path)
		target_path = os.path.join(parent.config_path, qss_name)
		if not os.path.isdir(parent.config_path):
			os.mkdir(parent.config_path)
		if not os.path.isfile(target_path):
			shutil.copy2(source_path, parent.config_path)
		parent.custom_qss_le.setText(qss_name)

		# if config path and the file is not there copy the file


		return




		'''
		# copy the file to the configuration directory if not there
		if not os.path.isfile(target_path):
			if parent.config_path:
				if os.path.isdir(parent.config_path:):
					msg = ('Do you want to copy the stylesheet\n'
					f'{base_name} to the configuration directory\n'
					f'{parent.config_path}')
					response = dialogs.msg_question_yes_no(parent, msg, 'Copy File?')
					if response:
						shutil.copy2(source_path, parent.config_path)
				else: # config path does not exist
					print('no config name')
			elif not parent.config_path: # no machine name
				print('nope')
		'''

def theme_changed(parent):
	if parent.sender().currentData():
		parent.custom_qss_le.setText('')
		parent.open_qss_pb.setEnabled(False)
	else:
		parent.open_qss_pb.setEnabled(True)

def select_dir(parent): # FIXME not used anywhere it seems
	options = QFileDialog.Option.DontUseNativeDialog
	dir_path = False
	file_dialog = QFileDialog()
	file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
	file_dialog.setOptions(QFileDialog.Option.DontUseNativeDialog)
	file_dialog.setWindowTitle('Open File')
	dir_path, file_type = file_dialog.getOpenFileName(None,
	caption=caption, directory=parent.nc_code_dir,
	filter=parent.ext_filter, options=options)
	if dir_path:
		return dir_path
	else:
		return False

def open_manual(parent):
	if parent.installed:
		doc = os.path.join(parent.docs_path, 'mesact.pdf.gz')
	else:
		doc = os.path.join(parent.docs_path, 'mesact.pdf')
	subprocess.call(('xdg-open', doc))

def machine_name_changed(parent, text):
	if text:
		parent.machine_name = text.replace(' ','_').lower()
		parent.config_path = os.path.expanduser('~/linuxcnc/configs') + '/' + parent.machine_name
		parent.config_path_lb.setText(parent.config_path)
		parent.ini_path = os.path.join(parent.config_path, f'{parent.machine_name}.ini')
	else:
		parent.config_path_lb.setText('')
		parent.config_path = False
		parent.ini_path = False

def input_changed(parent):
	# 7i95, 7i96s and 7i96s have slow
	if parent.board_0_hal_name in ['7c80', '7i95', '7i96s', '7i97']:
		input_number = parent.sender().objectName().split('_')[-1]
		#print(f'input_number {input_number}')
		checked = parent.sender().isChecked()
		#print(f'checked {checked}')
		if parent.sender().objectName().startswith('c0_input_invert_'):
			getattr(parent, f'c0_input_debounce_{input_number}' ).setEnabled(not checked)
		elif parent.sender().objectName().startswith('c0_input_debounce_'):
			getattr(parent, f'c0_input_invert_{input_number}' ).setEnabled(not checked)

def save_settings(parent):
	parent.settings.setValue('GUI/window_size', parent.size())
	parent.settings.setValue('GUI/window_position', parent.pos())

def update_settings(parent):
	if parent.load_config_cb.isChecked():
		parent.settings.setValue('STARTUP/config', parent.ini_path)
	else:
		parent.settings.setValue('STARTUP/config', False)

def gui_changed(parent):
	if parent.gui_cb.currentData() == 'flexgui':
		parent.flex_gui_gb.setEnabled(True)
	else:
		parent.flex_gui_gb.setEnabled(False)

def units_changed(parent):
	if parent.linear_units_cb.currentData() == 'mm':
		parent.units_second = 'mm/s'
		parent.units_second2 = 'mm/s^2'
		parent.units_minute = 'mm/m'
	elif parent.linear_units_cb.currentData() == 'inch':
		parent.units_second = 'in/s'
		parent.units_second2 = 'i/s^2'
		parent.units_minute = 'in/m'
	else:
		parent.units_second = 'N/A'
		parent.units_second2 = 'N/A'
		parent.units_minute = 'N/A'
		for i in range(3):
			getattr(parent, f'units_lb_{i}').setText('Select Linear Units on the Settings Tab')

	for i in range(3): # cards
		for j in range(6): # drives
			getattr(parent, f'c{i}_max_vel_suffix_{j}').setText(parent.units_second)
			getattr(parent, f'c{i}_max_vel_min_suffix_{j}').setText(parent.units_minute)

	# c0_max_vel_suffix_0
	parent.c0_max_vel_min_suffix_0.setText(parent.units_minute)
	for i in range(6):
		for j in range(3): # <-- change when more cards are added
			getattr(parent, f'c{j}_max_vel_{i}').setPlaceholderText(parent.units_second)
			getattr(parent, f'c{j}_max_accel_{i}').setPlaceholderText(parent.units_second2)
	for i in range(3):
		getattr(parent, f'units_lb_{i}').setText(f'Velocity & Acceleration in {parent.units_second}')
	parent.max_lin_vel_lb.setText(f'{parent.units_second}')
	parent.min_lin_jog_lb.setText(f'{parent.units_second}')
	parent.default_lin_jog_lb.setText(f'{parent.units_second}')
	parent.max_lin_jog_lb.setText(f'{parent.units_second}')
	parent.min_linear_vel_lb.setText(f'{parent.min_lin_jog_vel_dsb.value() * 60:.1f} {parent.units_minute}')
	parent.default_linear_vel_lb.setText(f'{parent.default_lin_jog_vel_dsb.value() * 60:.1f} {parent.units_minute}')
	parent.max_linear_vel_lb.setText(f'{parent.max_lin_jog_vel_dsb.value() * 60:.1f} {parent.units_minute}')
	parent.min_angular_vel_lb.setText(f'{parent.min_ang_jog_vel_dsb.value() * 60:.1f} deg/min')
	parent.default_angular_vel_lb.setText(f'{parent.default_ang_jog_vel_dsb.value() * 60:.1f} deg/min')
	parent.max_angular_vel_lb.setText(f'{parent.max_ang_jog_vel_dsb.value() * 60:.1f} deg/min')

def max_vel_changed(parent):
	if parent.traj_max_lin_vel_dsb.value() > 0:
		val = parent.traj_max_lin_vel_dsb.value()
		if parent.linear_units_cb.currentData() == 'mm':
			parent.mlv_per_min_lb.setText(f'Max Velocity {val * 60:.1f} mm/min')
		if parent.linear_units_cb.currentData() == 'inch':
			parent.mlv_per_min_lb.setText(f'Max Velocity {val * 60:.1f} in/min')
	else:
		parent.mlv_per_min_lb.setText('')

def toggle_mdi(parent):
	if parent.sender().isChecked():
		parent.mdi_commands_gb.setEnabled(True)
	else:
		parent.mdi_commands_gb.setEnabled(False)

def changed(parent): # if anything is changed add * to title
	parent.status_lb.setText('Config Changed')
	parent.actionBuild.setText('Build Config *')

def backup_files(parent):
	parent.main_tw.setCurrentIndex(10)
	if not parent.config_path: # no machine name
		parent.info_pte.setPlainText('A Machine Name must be specified to get a path')
		return
	elif not os.path.exists(parent.config_path):
		parent.info_pte.setPlainText(f'There is nothing to back up.\nThe path {parent.config_path} does not exist.')
		return
	backup_dir = os.path.join(config_path, 'backups')
	if not os.path.exists(backup_dir):
		os.mkdir(backup_dir)
	p1 = subprocess.Popen(['find',config_path,'-maxdepth','1','-type','f','-print'], stdout=subprocess.PIPE)
	backup_file = os.path.join(backup_dir, f'{datetime.now():%m-%d-%y-%H:%M:%S}')
	p2 = subprocess.Popen(['zip','-j',backup_file,'-@'], stdin=p1.stdout, stdout=subprocess.PIPE)
	p1.stdout.close()
	parent.info_pte.appendPlainText('Backing up Confguration')
	output = p2.communicate()[0]
	parent.info_pte.appendPlainText(output.decode())

def add_mdi_row(parent):
	rows = parent.mdi_grid_layout.rowCount()
	# layout.addWidget(widget, row, column)
	parent.mdi_grid_layout.addWidget(QLabel('MDI Command'), rows, 0)
	le = QLineEdit(parent)
	le.setObjectName(f'mdi_le_{rows}')
	setattr(parent, f'mdi_le_{rows}', le) # add name to parent
	parent.mdi_grid_layout.addWidget(le, rows, 1)
	getattr(parent, f'mdi_le_{rows}').setFocus()
	getattr(parent, f'mdi_le_{rows}').returnPressed.connect(partial(add_mdi_row, parent))

def check_updates(parent):
	response = requests.get(f"https://api.github.com/repos/jethornton/mesact/releases/latest")
	repo_version = response.json()["name"]
	print(f'repo_version {repo_version}')
	parent.main_tw.setCurrentIndex(10)
	if tuple(repo_version.split('.')) > tuple(parent.version.split('.')):
		parent.info_pte.appendPlainText(f'This version {parent.version} is older than the latest release {repo_version}')
	elif tuple(repo_version.split('.')) == tuple(parent.version.split('.')):
		parent.info_pte.appendPlainText(f'This version {parent.version} is the same as the latest release {repo_version}')
	elif tuple(repo_version.split('.')) < tuple(parent.version.split('.')):
		parent.info_pte.appendPlainText(f'This version {parent.version} is newer than the latest release {repo_version}')




