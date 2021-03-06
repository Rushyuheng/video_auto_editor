import sys
import PyQt5.uic as uic
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
import autoedit

qtCreatorFile = "main.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainUi(QMainWindow, Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.iniGuiEvent()

	def iniGuiEvent(self):# connect all button to all event slot
		self.choose_show.clicked.connect(self.choose_show_onClick)
		self.choose_animate.clicked.connect(self.choose_animate_onClick)
		self.choose_icon.clicked.connect(self.choose_icon_onClick)
		self.blackfilter_checkbox.clicked.connect(self.blackfilter_checkboxChangedAction)
		self.icon_pos_combobox.activated.connect(self.icon_pos_comboboxActivate)
		self.generate_icon_checkbox.clicked.connect(self.generate_icon_checkboxChangedAction)
		self.add_queue.clicked.connect(self.add_queue_onClick)
		self.clear_table.clicked.connect(self.clear_table_onClick)
		self.quality_combobox.activated.connect(self.quality_comboboxActivate)
		self.write_video.clicked.connect(self.write_video_onClick)

		#intialize parameter
		self.animate_filename = ""
		self.show_filename = ""
		self.icon_filename = ""
		self.enable_blackfilter = True
		self.enable_genicon = True
		self.icon_pos = "左下"
		self.quality = "1080"

	@pyqtSlot()
	def choose_show_onClick(self):
		self.show_filename,_ = QFileDialog.getOpenFileName(self,"open file","./","vidoe file:(*.wmv *.mp4 *.m4v)")
		if not self.show_filename:
			self.show_path.setText("尚未選擇檔案")
			self.start_min.setText("0")
			self.start_sec.setText("0")	
			self.end_min.setText("0")
			self.end_sec.setText("0")
		else:
			self.show_path.setText(self.show_filename)
			self.start_min.setText("0")
			self.start_sec.setText("0")	
			min,sec = autoedit.getvideolength(self.show_filename)
			self.end_min.setText(str(min))
			self.end_sec.setText(str(sec))

	@pyqtSlot()
	def choose_animate_onClick(self):
		self.animate_filename,_ = QFileDialog.getOpenFileName(self,"open file","./","vidoe file:(*.wmv *.mp4 *.m4v)")
		if not self.animate_filename:
			self.animate_path.setText("尚未選擇檔案")
		else:
			self.animate_path.setText(self.animate_filename)

	@pyqtSlot()
	def choose_icon_onClick(self):
		self.icon_filename,_ = QFileDialog.getOpenFileName(self,"open file","./","image file:(*.png *.jpg *.jpeg)")
		if not self.icon_filename:
			self.icon_filename = ""
			self.icon_path.setText("尚未選擇檔案")
		else:
			self.icon_path.setText(self.icon_filename)

	@pyqtSlot()
	def icon_pos_comboboxActivate(self):
		self.icon_pos = self.icon_pos_combobox.currentText()

	@pyqtSlot()
	def blackfilter_checkboxChangedAction(self):
		if self.blackfilter_checkbox.isChecked():
			self.enable_blackfilter = True
		else:
			self.enable_blackfilter = False

	@pyqtSlot()
	def generate_icon_checkboxChangedAction(self):
		if self.generate_icon_checkbox.isChecked():
			self.enable_genicon = True
		else:
			self.enable_genicon = False
	@pyqtSlot()
	def quality_comboboxActivate(self):
		self.quality = self.quality_combobox.currentText()

	@pyqtSlot()
	def add_queue_onClick(self):
		#get value from line edit object
		start_min = self.start_min.text()
		start_sec = self.start_sec.text()	
		end_min = self.end_min.text()
		end_sec = self.end_sec.text()
		start_time = start_min + ":" + start_sec
		end_time = end_min + ":"  + end_sec

		icon_width = self.icon_width.text()
		icon_height = self.icon_height.text()
		icon_size = icon_width + "X" + icon_height


		if not (start_min and start_sec and end_min and end_sec):
			self.status.setText("錯誤：未設定時間")
		elif not (icon_width and icon_height):
			self.status.setText("錯誤：未設定ICON尺寸")
		elif not self.show_filename:
			self.status.setText("錯誤：未選擇表演影片")
		elif not self.animate_filename:
			self.status.setText("錯誤：未選擇片頭動畫")
		else:
			rowPosition = self.processqueue.rowCount()
			self.processqueue.insertRow(rowPosition)
			self.processqueue.setItem(rowPosition , 0, QTableWidgetItem(self.show_filename))
			self.processqueue.setItem(rowPosition , 1, QTableWidgetItem(start_time))
			self.processqueue.setItem(rowPosition , 2, QTableWidgetItem(end_time))
			self.processqueue.setItem(rowPosition , 3, QTableWidgetItem(self.animate_filename))
			self.processqueue.setItem(rowPosition , 4, QTableWidgetItem(str(self.enable_blackfilter)))
			self.processqueue.setItem(rowPosition , 5, QTableWidgetItem(self.icon_filename))
			self.processqueue.setItem(rowPosition , 6, QTableWidgetItem(self.icon_pos))
			self.processqueue.setItem(rowPosition , 7, QTableWidgetItem(icon_size))
			self.processqueue.setItem(rowPosition , 8, QTableWidgetItem(str(self.enable_genicon)))
			self.status.setText("成功加入影片處理清單")

	@pyqtSlot()
	def clear_table_onClick(self):
		rowlength = self.processqueue.rowCount()
		for index in range(0,rowlength):
			self.processqueue.removeRow(0)
		self.status.setText("已清除影片處理清單")

	@pyqtSlot()
	def write_video_onClick(self):
		rowlength = self.processqueue.rowCount()
		for index in range(0,rowlength):
			#parse table content
			show_filename = str(self.processqueue.item(index,0).text())

			start_time = str(self.processqueue.item(index,1).text()).split(":")
			start_time = (int(start_time[0]),int(start_time[1]))

			end_time = str(self.processqueue.item(index,2).text()).split(":")
			end_time = (int(end_time[0]),int(end_time[1]))

			animate_filename = str(self.processqueue.item(index,3).text())

			enable_blackfilter = str(self.processqueue.item(index,4).text())
			if enable_blackfilter == "False":
				enable_blackfilter = False # cast to bool
			else:
				enable_blackfilter = True
			
			icon_filename = str(self.processqueue.item(index,5).text())
			
			icon_pos = str(self.processqueue.item(index,6).text())
			if icon_pos == "右下":
				icon_pos = ("right","bottom")
			elif icon_pos == "右上":
				icon_pos = ("right","top")
			elif icon_pos == "左上":
				icon_pos = ("left","top")
			else:
				icon_pos = ("left","bottom")

			icon_size = str(self.processqueue.item(index,7).text()).split("X")
			icon_size = (int(icon_size[0]),int(icon_size[1])) # API resize (width,height)

			enable_genicon = str(self.processqueue.item(index,8).text())
			if enable_genicon == "False":
				enable_genicon = False # cast to bool
			else:
				enable_genicon = True

			quality = int(self.quality)

			self.status.setText("輸出影片中...({0}/{1})".format(index + 1,rowlength))
			self.status.repaint()
			#print([index,show_filename,start_time,end_time,animate_filename,enable_blackfilter,icon_filename,icon_pos,icon_size,enable_genicon,quality])
			autoedit.writevideo(index,show_filename,start_time,end_time,animate_filename,enable_blackfilter,icon_filename,icon_pos,icon_size,enable_genicon,quality)
		self.status.setText("已輸出所有影片")

if __name__ == "__main__": #main function
	def run_app():
		app = QApplication(sys.argv)
		window = MainUi()
		window.show()
		app.exec_()
	run_app()