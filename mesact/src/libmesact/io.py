
hm2 = {'5i25': 'hm2_5i25', '5i25T': 'hm2_5i25', '6i25': 'hm2_5i25',
	'7i76E': 'hm2_7i76e', '7i76EU': 'm2_7i76e', '7i92': 'hm2_7i92',
	'7i92T': 'hm2_7i92','7i95': 'hm2_7i95', '7i95T': 'hm2_7i95',
	'7i96': 'hm2_7i96', '7i96S': 'hm2_7i96s', '7i97': 'hm2_7i97',
	'7i97T': 'hm2_7i97'}

outputs = {
'Motion Enable': 'net motion-enable =>',
'Coolant Flood': 'net flood-output iocontrol.0.coolant-flood =>',
'Coolant Mist': 'net mist-output iocontrol.0.coolant-mist =>',
'Spindle On': 'net spindle-on =>',
'Spindle CW': 'net spindle-cw spindle.0.forward =>',
'Spindle CCW': 'net spindle-ccw spindle.0.reverse =>',
'Spindle Brake': 'net spindle-brake spindle.0.brake =>',
'E-Stop Out': 'net estop-loopback =>',
'Digital Out 0': 'net digital-out-0 motion.digital-out-00 =>',
'Digital Out 1': 'net digital-out-1 motion.digital-out-01 =>',
'Digital Out 2': 'net digital-out-2 motion.digital-out-02 =>',
'Digital Out 3': 'net digital-out-3 motion.digital-out-03 =>',
'Joint 0 Amp Enable': 'net joint-0-enable joint.0.amp-enable-out =>',
'Joint 1 Amp Enable': 'net joint-1-enable joint.1.amp-enable-out =>',
'Joint 2 Amp Enable': 'net joint-2-enable joint.2.amp-enable-out =>',
'Joint 3 Amp Enable': 'net joint-3-enable joint.3.amp-enable-out =>',
'Joint 4 Amp Enable': 'net joint-4-enable joint.4.amp-enable-out =>',
'Joint 5 Amp Enable': 'net joint-5-enable joint.5.amp-enable-out =>',
'Joint 6 Amp Enable': 'net joint-6-enable joint.6.amp-enable-out =>',
'Joint 7 Amp Enable': 'net joint-7-enable joint.7.amp-enable-out =>',
'Joint 8 Amp Enable': 'net joint-8-enable joint.8.amp-enable-out =>',
}

inputs = {
	'Joint 0 Home':'net joint-0-home joint.0.home-sw-in <=',
	'Joint 1 Home':'net joint-1-home joint.1.home-sw-in <=',
	'Joint 2 Home':'net joint-2-home joint.2.home-sw-in <=',
	'Joint 3 Home':'net joint-3-home joint.3.home-sw-in <=',
	'Joint 4 Home':'net joint-4-home joint.4.home-sw-in <=',
	'Joint 5 Home':'net joint-5-home joint.5.home-sw-in <=',
	'Joint 6 Home':'net joint-6-home joint.6.home-sw-in <=',
	'Joint 7 Home':'net joint-7-home joint.7.home-sw-in <=',
	'Joint 8 Home':'net joint-8-home joint.8.home-sw-in <=',
	'Home All':'net home-all halui.home-all <=',

	'Joint 0 Plus':'net pos-limit-joint-0 joint.0.pos-lim-sw-in <=',
	'Joint 0 Minus':'net neg-limit-joint-0 joint.0.neg-lim-sw-in <=',
	'Joint 0 Both':'net both-limit-joint-0 joint.0.pos-lim-sw-in\n'
		'net both-limit-joint-0 joint.0.neg-lim-sw-in <=',
	'Joint 1 Plus':'net pos-limit-joint-1 joint.1.pos-lim-sw-in <=',
	'Joint 1 Minus':'net neg-limit-joint-1 joint.1.neg-lim-sw-in <=',
	'Joint 1 Both':'net both-limit-joint-1 joint.1.pos-lim-sw-in\n'
		'net both-limit-joint-1 joint.1.neg-lim-sw-in <=',
	'Joint 2 Plus':'net pos-limit-joint-2 joint.2.pos-lim-sw-in <=',
	'Joint 2 Minus':'net neg-limit-joint-2 joint.2.neg-lim-sw-in <=',
	'Joint 2 Both':'net both-limit-joint-2 joint.2.pos-lim-sw-in\n'
		'net both-limit-joint-2 joint.2.neg-lim-sw-in <=',
	'Joint 3 Plus':'net pos-limit-joint-3 joint.3.pos-lim-sw-in <=',
	'Joint 3 Minus':'net neg-limit-joint-3 joint.3.neg-lim-sw-in <=',
	'Joint 3 Both':'net both-limit-joint-3 joint.3.pos-lim-sw-in\n'
		'net both-limit-joint-3 joint..neg-lim-sw-in <=',
	'Joint 4 Plus':'net pos-limit-joint-4 joint.4.pos-lim-sw-in <=',
	'Joint 4 Minus':'net neg-limit-joint-4 joint.4.neg-lim-sw-in <=',
	'Joint 4 Both':'net both-limit-joint-4 joint.4.pos-lim-sw-in\n'
		'net both-limit-joint-4 joint.4.neg-lim-sw-in <=',
	'Joint 5 Plus':'net pos-limit-joint-5 joint.5.pos-lim-sw-in <=',
	'Joint 5 Minus':'net neg-limit-joint-5 joint.5.neg-lim-sw-in <=',
	'Joint 5 Both':'net both-limit-joint-5 joint.5.pos-lim-sw-in\n'
		'net both-limit-joint-5 joint.5.neg-lim-sw-in <=',
	'Joint 6 Plus':'net pos-limit-joint-6 joint.6.pos-lim-sw-in <=',
	'Joint 6 Minus':'net neg-limit-joint-6 joint.6.neg-lim-sw-in <=',
	'Joint 6 Both':'net both-limit-joint-6 joint.6.pos-lim-sw-in\n'
		'net both-limit-joint-6 joint.6.neg-lim-sw-in <=',
	'Joint 7 Plus':'net pos-limit-joint-7 joint.7.pos-lim-sw-in <=',
	'Joint 7 Minus':'net neg-limit-joint-7 joint.7.neg-lim-sw-in <=',
	'Joint 7 Both':'net both-limit-joint-7 joint.7.pos-lim-sw-in\n'
		'net both-limit-joint-7 joint.7.neg-lim-sw-in <=',
	'Joint 8 Plus':'net pos-limit-joint-8 joint.8.pos-lim-sw-in <=',
	'Joint 8 Minus':'net neg-limit-joint-8 joint.8.neg-lim-sw-in <=',
	'Joint 8 Both':'net both-limit-joint-8 joint.8.pos-lim-sw-in\n'
		'net both-limit-joint-8 joint.8.neg-lim-sw-in <=',

	'Joint 0 Plus Home':'net plus-home-joint-0 joint.0.pos-lim-sw-in\n'
		'net plus-home-joint-0 joint.0.home-sw-in <=',
	'Joint 0 Minus Home':'net minus-home-joint-0 joint.0.neg-lim-sw-in\n'
		'net minus-home-joint-0 joint.0.home-sw-in <=',
	'Joint 0 Plus Minus Home':'net plus-minus-home-joint-0 joint.0.pos-lim-sw-in\n'
		'net plus-minus-home-joint-0 joint.0.neg-lim-sw-in\n'
		'net plus-minus-home-joint-0 joint.0.home-sw-in <=',

	'Joint 1 Plus Home':'net plus-home-joint-1 joint.1.pos-lim-sw-in\n'
		'net plus-home-joint-1 joint.1.home-sw-in <=',
	'Joint 1 Minus Home':'net minus-home-joint-1 joint.1.neg-lim-sw-in\n'
		'net minus-home-joint-1 joint.1.home-sw-in <=',
	'Joint 1 Plus Minus Home':'net plus-minus-home-joint-1 joint.1.pos-lim-sw-in\n'
		'net plus-minus-home-joint-1 joint.1.neg-lim-sw-in\n'
		'net plus-minus-home-joint-1 joint.1.home-sw-in <=',

	'Joint 2 Plus Home':'net plus-home-joint-2 joint.2.pos-lim-sw-in\n'
		'net plus-home-joint-2 joint.2.home-sw-in <=',
	'Joint 2 Minus Home':'net minus-home-joint-2 joint.2.neg-lim-sw-in\n'
		'net minus-home-joint-2 joint.2.home-sw-in <=',
	'Joint 2 Plus Minus Home':'net plus-minus-home-joint-2 joint.2.pos-lim-sw-in\n'
		'net plus-minus-home-joint-2 joint.2.neg-lim-sw-in\n'
		'net plus-minus-home-joint-2 joint.2.home-sw-in <=',

	'Joint 3 Plus Home':'net plus-home-joint-3 joint.3.pos-lim-sw-in\n'
		'net plus-home-joint-3 joint.3.home-sw-in <=',
	'Joint 3 Minus Home':'net minus-home-joint-3 joint.3.neg-lim-sw-in\n'
		'net minus-home-joint-3 joint.3.home-sw-in <=',
	'Joint 3 Plus Minus Home':'net plus-minus-home-joint-3 joint.3.pos-lim-sw-in\n'
		'net plus-minus-home-joint-3 joint.3.neg-lim-sw-in\n'
		'net plus-minus-home-joint-3 joint.3.home-sw-in <=',

	'Joint 4 Plus Home':'net plus-home-joint-4 joint.4.pos-lim-sw-in\n'
		'net plus-home-joint-4 joint.4.home-sw-in <=',
	'Joint 4 Minus Home':'net minus-home-joint-4 joint.4.neg-lim-sw-in\n'
		'net minus-home-joint-4 joint.4.home-sw-in <=',
	'Joint 4 Plus Minus Home':'net plus-minus-home-joint-4 joint.4.pos-lim-sw-in\n'
		'net plus-minus-home-joint-4 joint.4.neg-lim-sw-in\n'
		'net plus-minus-home-joint-4 joint.4.home-sw-in <=',

	'Joint 5 Plus Home':'net plus-home-joint-5 joint.5.pos-lim-sw-in\n'
		'net plus-home-joint-5 joint.5.home-sw-in <=',
	'Joint 5 Minus Home':'net minus-home-joint-5 joint.5.neg-lim-sw-in\n'
		'net minus-home-joint-5 joint.5.home-sw-in <=',
	'Joint 5 Plus Minus Home':'net plus-minus-home-joint-5 joint.5.pos-lim-sw-in\n'
		'net plus-minus-home-joint-5 joint.5.neg-lim-sw-in\n'
		'net plus-minus-home-joint-5 joint.5.home-sw-in <=',

	'Joint 6 Plus Home':'net plus-home-joint-6 joint.6.pos-lim-sw-in\n'
		'net plus-home-joint-6 joint.6.home-sw-in <=',
	'Joint 6 Minus Home':'net minus-home-joint-6 joint.6.neg-lim-sw-in\n'
		'net minus-home-joint-6 joint.6.home-sw-in <=',
	'Joint 6 Plus Minus Home':'net plus-minus-home-joint-6 joint.6.pos-lim-sw-in\n'
		'net plus-minus-home-joint-6 joint.6.neg-lim-sw-in\n'
		'net plus-minus-home-joint-6 joint.6.home-sw-in <=',

	'Joint 7 Plus Home':'net plus-home-joint-7 joint.7.pos-lim-sw-in\n'
		'net plus-home-joint-7 joint.7.home-sw-in <=',
	'Joint 7 Minus Home':'net minus-home-joint-7 joint.7.neg-lim-sw-in\n'
		'net minus-home-joint-7 joint.7.home-sw-in <=',
	'Joint 7 Plus Minus Home':'net plus-minus-home-joint-7 joint.7.pos-lim-sw-in\n'
		'net plus-minus-home-joint-7 joint.7.neg-lim-sw-in\n'
		'net plus-minus-home-joint-7 joint.7.home-sw-in <=',

	'Joint 8 Plus Home':'net plus-home-joint-8 joint.8.pos-lim-sw-in\n'
		'net plus-home-joint-8 joint.8.home-sw-in <=',
	'Joint 8 Minus Home':'net minus-home-joint-8 joint.8.neg-lim-sw-in\n'
		'net minus-home-joint-8 joint.8.home-sw-in <=',
	'Joint 8 Plus Minus Home':'net plus-minus-home-joint-8 joint.8.pos-lim-sw-in\n'
		'net plus-minus-home-joint-8 joint.8.neg-lim-sw-in\n'
		'net plus-minus-home-joint-8 joint.8.home-sw-in <=',

	'Jog X Plus':'net jog-x-plus halui.axis.x.plus <=',
	'Jog X Minus':'net jog-x-minus halui.axis.x.minus <=',
	'Jog X Enable':'net jog-x-enable axis.x.jog-enable <=',
	'Jog Y Plus':'net jog-y-plus halui.axis.y.plus <=',
	'Jog Y Minus':'net jog-y-minus halui.axis.y.minus <=',
	'Jog Y Enable':'net jog-y-enable axis.y.jog-enable <=',
	'Jog Z Plus':'net jog-z-plus halui.axis.z.plus <=',
	'Jog Z Minus':'net jog-z-minus halui.axis.z.minus <=',
	'Jog Z Enable':'net jog-z-enable axis.z.jog-enable <=',
	'Jog A Plus':'net jog-a-plus halui.axis.a.plus <=',
	'Jog A Minus':'net jog-a-minus halui.axis.a.minus <=',
	'Jog A Enable':'net jog-a-enable axis.a.jog-enable <=',
	'Jog B Plus':'net jog-b-plus halui.axis.b.plus <=',
	'Jog B Minus':'net jog-b-minus halui.axis.b.minus <=',
	'Jog B Enable':'net jog-b-enable axis.b.jog-enable <=',
	'Jog C Plus':'net jog-c-plus halui.axis.c.plus <=',
	'Jog C Minus':'net jog-c-minus halui.axis.c.minus <=',
	'Jog C Enable':'net jog-c-enable axis.c.jog-enable <=',
	'Jog U Plus':'net jog-u-plus halui.axis.u.plus <=',
	'Jog U Minus':'net jog-u-minus halui.axis.u.minus <=',
	'Jog U Enable':'net jog-u-enable axis.u.jog-enable <=',
	'Jog V Plus':'net jog-v-plus halui.axis.v.plus <=',
	'Jog V Minus':'net jog-v-minus halui.axis.v.minus <=',
	'Jog V Enable':'net jog-v-enable axis.v.jog-enable <=',
	'Jog W Plus':'net jog-w-plus halui.axis.w.plus <=',
	'Jog W Minus':'net jog-w-minus halui.axis.w.minus <=',
	'Jog W Enable':'net jog-w-enable axis.w.jog-enable <=',

	'Probe Input':'net probe-input motion.probe-input <=',
	'Digital 0':'net digital-0-input motion.digital-in-00 <=',
	'Digital 1':'net digital-1-input motion.digital-in-01 <=',
	'Digital 2':'net digital-2-input motion.digital-in-02 <=',
	'Digital 3':'net digital-3-input motion.digital-in-03 <=',

	'Flood':'net coolant-flood iocontrol.0.coolant-flood <=',
	'Mist':'net coolant-mist iocontrol.0.coolant-mist <=',
	'Lube Level':'net lube-level iocontrol.0.lube_level <=',
	'Tool Changed':'net tool-changed iocontrol.0.tool-changed <=',
	'Tool Prepared':'net tool-prepared iocontrol.0.tool-prepared <=',
	'Tool Changer Fault':'iocontrol.0.toolchanger-fault <=',
	'Spindle Amp Fault':'spindle.0.amp-fault-in <=',
	'Spindle Inhibit':'spindle.0.inhibit <=',
	'Spindle Oriented':'spindle.0.is-oriented <=',
	'Spindle Orient Fault':'spindle.0.orient-fault <='
	}

