import os, shutil

from libmesact import check
from libmesact import dialogs
from libmesact import utilities
from libmesact import updateini
from libmesact import buildini
from libmesact import buildhal
from libmesact import buildio
from libmesact import buildss
from libmesact import buildmisc

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

	# create the linuxcnc/configs/configuration directory if not there
	if not os.path.exists(parent.config_path): # there might be a file by the same name
		os.mkdir(parent.config_path)
		parent.info_pte.appendPlainText(f'The directory {parent.config_path} was created')
		if parent.gui_cb.currentData() == 'flexgui':
			if parent.flex_gui_path_lb.text() and parent.flex_gui_lb.text():
				ui_path = os.path.join(parent.flex_gui_path_lb.text(), parent.flex_gui_lb.text())
				if os.path.isfile(ui_path):
					shutil.copy2(ui_path, parent.config_path)
	elif os.path.isfile(parent.config_path):
		msg = ('There seems to be a file in\n'
		f'{os.path.expanduser("~/linuxcnc/configs")} with the\n'
		'same name as the configuration directory.\n'
		'The configuration directory\n'
		f'{parent.config_path}\n'
		'can not be created.\n'
		'Either rename or remove the file\n'
		'The build has failed')
		dialogs.msg_error_ok(parent, msg, 'Build Error')
		return


	# for testing this is not used
	'''
	if os.path.exists(parent.ini_path):
		updateini.update(parent)
	else:
		buildini.build(parent)
	'''
	buildini.build(parent) # FIXME remove after update ini is started
	buildhal.build(parent)
	buildio.build(parent)
	buildss.build(parent)
	buildmisc.build(parent)
	#parent.mainTW.setCurrentIndex(11)
	parent.status_lb.setText('Saved')
	parent.actionBuild.setText('Build Config')



