import os

from libmesact import check
from libmesact import utilities
from libmesact import updateini
from libmesact import buildini
from libmesact import buildhal
from libmesact import buildio

def build(parent):
	if not check.check_config(parent):
		return

	if parent.backup_cb.isChecked():
		utilities.backup_files(parent)

	# create linuxcnc directory if not there
	emc_path = os.path.expanduser('~/linuxcnc')
	if not os.path.isdir(emc_path):
		os.mkdir(emc_path)
		parent.info_pte.appendPlainText(f'The directory {emc_path} was created')

	# create the linuxcnc/configs directory if not there
	configs_path = os.path.expanduser('~/linuxcnc/configs')
	if not os.path.isdir(configs_path):
		os.mkdir(configs_path)
		parent.info_pte.appendPlainText(f'The directory {configs_path} was created')

	# create the linuxcnc/nc_files directory if not there
	nc_path = os.path.expanduser('~/linuxcnc/nc_files')
	if not os.path.isdir(nc_path):
		os.mkdir(nc_path)
		parent.info_pte.appendPlainText(f'The directory {nc_path} was created')

	# create the linuxcnc/subroutines directory if requested and not there
	if parent.subroutine_cb.isChecked():
		sub_path = os.path.expanduser('~/linuxcnc/subroutines')
		if not os.path.isdir(sub_path):
			os.mkdir(os.path.expanduser('~/linuxcnc/subroutines'))
			parent.info_pte.appendPlainText(f'The directory {sub_path} was created')

	# create the linuxcnc/configs/configuration directory if not there
	if not os.path.isdir(parent.config_path):
		os.mkdir(parent.config_path)
		parent.info_pte.appendPlainText(f'The directory {parent.config_path} was created')

	# create the var file if not there
	var_file = os.path.join(parent.config_path, 'parameters.var')
	if not os.path.isfile(var_file):
		open(var_file, 'a').close()
		parent.info_pte.appendPlainText(f'The parameters file {var_file} was created')

	# create the tool file if not there
	tool_file = os.path.join(parent.config_path, 'tool.tbl')
	if not os.path.isfile(tool_file):
		with open(tool_file, 'w') as f:
			f.write(';\n')
			f.write('T1  P1  ;sample tool')
		parent.info_pte.appendPlainText(f'The tool table file {tool_file} was created')

	# create the custom.hal file if requested and if not there
	if parent.custom_hal_cb.isChecked():
		custom_file = os.path.join(parent.config_path, 'custom.hal')
		if not os.path.isfile(custom_file):
			with open(custom_file, 'w') as f:
				f.write('# Add HAL commands to this file that need to be executed before the GUI loads\n')
				f.write('# This file will not be modified by the Configuration tool if it exists')
			parent.info_pte.appendPlainText(f'The custom HAL file {custom_file} was created')


	# for testing this is not used
	'''
	if os.path.exists(parent.ini_path):
		updateini.update(parent)
	else:
		buildini.build(parent)
	'''
	buildini.build(parent) # FIXME remove after update ini is started
	buildhal.build(parent)
	buildio.build_io(parent)
	#buildio.build_ss(parent)
	#buildmisc.build(parent)
	#parent.mainTW.setCurrentIndex(11)
	#parent.status_lb.setText('Saved')
	#parent.actionBuild.setText('Build Config')



