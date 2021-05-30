import sys
import PyQt5.uic as uic
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication
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
		self.write_video.clicked.connect(self.write_video_onClick)
		self.choose_show.clicked.connect(self.choose_show_onClick)
		self.choose_animate.clicked.connect(self.choose_animate_onClick)
		self.choose_icon.clicked.connect(self.choose_icon_onClick)
		self.animate_filename = ""
		self.show_filename = ""
		self.icon_filename = ""

	@pyqtSlot()
	def choose_show_onClick(self):
		self.show_filename,_ = QFileDialog.getOpenFileName(self,"open file","./","vidoe file:(*.wmv *.mp4 *.m4v)")
		if not self.show_filename:
			self.show_path.setText("尚未選擇檔案")
		else:
			self.show_path.setText(self.show_filename)

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
	def write_video_onClick(self):
		#get value from line edit object
		start_min = self.start_min.text()
		start_sec = self.start_sec.text()	
		end_min = self.end_min.text()
		end_sec = self.end_sec.text()

		if not (start_min and start_sec and end_min and end_sec):
			self.status.setText("錯誤：未設定時間")
		elif not self.show_filename:
			self.status.setText("錯誤：未選擇表演影片")
		elif not self.animate_filename:
			self.status.setText("錯誤：未選擇片頭動畫")
		else:
			self.status.setText("輸出影片中...")
			self.status.repaint()
			autoedit.writevideo(start_min,start_sec,end_min,end_sec,self.animate_filename,self.show_filename,self.icon_filename)
			self.status.setText("影片輸出成功")

if __name__ == "__main__": #main function
	def run_app():
		app = QApplication(sys.argv)
		window = MainUi()
		window.show()
		app.exec_()
	run_app()