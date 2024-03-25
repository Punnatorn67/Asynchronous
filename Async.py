import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QDialog, QMessageBox, QFileDialog, QGraphicsView, QGraphicsScene
from PyQt6.QtWidgets import QLabel, QVBoxLayout
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QIcon, QImage, QPainter, QPixmap
from PyQt6.QtCore import QSize, Qt, QRectF
from PyQt6.QtSvg import QSvgGenerator
from PyQt6.QtPrintSupport import QPrinter
import textwrap
from PyQt6.QtGui import QPixmap
from graphviz import Digraph
import os
from generate import graph_full, graph_half, graph_chu133, graph_vbe5b
from circuit import circuit_full, circuit_half, circuit_vbe5b, circuit_chu133

class FileBrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vars = [None] * 15  # กำหนดตัวแปร vars ขนาด 15 ตัวเพื่อเก็บข้อมูลที่มาจาก text edit
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("STG")
        self.setGeometry(400, 100, 700, 400)
        self.setStyleSheet('background-color: #2C4B82;font: bold 14px;')
        # self.setWindowIcon(QIcon('your_icon.png'))

        # สร้างปุ่ม "Try" และกำหนดลักษณะ
        self.button_show = QPushButton("Try", self)
        self.button_show.setGeometry(510, 220, 90, 45)
        self.button_show.setStyleSheet("background-color:#F7B4A7;\n"
                                        "color: #2C4B82;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 5px;")
        self.button_show.clicked.connect(self.process_text)

        self.text_edit_1 = QTextEdit(self)
        self.text_edit_1.setGeometry(250, 30, 350, 180)
        self.text_edit_1.setStyleSheet("""QTextEdit {background-color: #F7B4A7;border-radius: 5px;color: black;}""")

        self.text_edit_3 = QTextEdit(self)
        self.text_edit_3.setGeometry(100, 30, 138, 180)
        self.text_edit_3.setStyleSheet("""QTextEdit {background-color: #F7B4A7;border-radius: 5px;color: black;}""")

        self.button_browse = QPushButton("Browse File", self)
        self.button_browse.setGeometry(120, 80, 100, 90)
        self.button_browse.setStyleSheet("background-color: #2C4B82;\n"
                                        "color: #F7B4A7;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 5px;")
        self.button_browse.clicked.connect(self.browse_file)

        self.button = QPushButton("", self)
        self.button.setGeometry(650, 345, 45, 50)
        self.button.setIcon(QIcon('question.png'))  # กำหนดภาพไอคอน
        self.button.setIconSize(QSize(22, 22))  # กำหนดขนาดไอคอน
        self.button.clicked.connect(self.show_howto)  # เชื่อมต่อกับฟังก์ชันที่ต้องการทำงานเมื่อคลิกปุ่ม
        self.button.setStyleSheet(
            "background-color:#F7B4A7;\n"
            "color: #2C4B82;\n"
            "border-radius: 5px;\n"
            "padding: 5px;"
        )  # กำหนดสไตล์ของปุ่ม

    def process_text(self):
        # รับข้อความจาก QTextEdit
        text = self.text_edit_1.toPlainText()

        if not text:
            QMessageBox.warning(self, "Warning", "โปรดป้อนสมการ")
            return

        # แยกข้อความเป็นบรรทัดๆ
        lines = text.split('\n')

        if len(lines) < 2:  # ตรวจสอบว่ามีคำน้อยกว่า 2 บรรทัดหรือไม่
            QMessageBox.warning(self, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร.")
            return
        if len(lines[0].split()) <= 3:
            QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร")
            return
        
            # ตรวจสอบว่ามีคำว่า "path" ในข้อมูลหรือไม่
        found_path = False
        for line in lines:
            if "path" in line:
                found_path = True
                break

        # ถ้าไม่พบคำว่า "path" ให้แสดงหน้าต่างเตือน
        if not found_path:
            QMessageBox.warning(self, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร")
            return

        # เพิ่มบรรทัดเปล่าถ้าน้อยกว่า 20 บรรทัด 
        while len(lines) < 20:
            lines.append("")

        # ตรวจสอบให้แน่ใจว่ามีอย่างน้อย 15 บรรทัด
        for i in range(min(len(lines), len(self.vars))):
            self.vars[i] = lines[i]

        data_to_send = self.text_edit_1.toPlainText()
        self.second_window = SecondWindow(data=data_to_send, vars=self.vars)
        self.second_window.show()
        self.hide()

        print("Vars:", self.vars)

    def browse_file(self):
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            if file_name.endswith('.txt'):  # เพิ่มเงื่อนไขเพื่อตรวจสอบไฟล์ .txt
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_edit_1.setPlainText(content)  
            else :
                QMessageBox.warning(self, "Error", "ต้องเป็นไฟล์ .txt เท่านั้น")

    def show_content(self):
        content = self.text_edit_1.toPlainText()
        data_to_send = self.text_edit_1.toPlainText()
        self.second_window = SecondWindow(data=data_to_send, vars=self.vars)
        self.second_window.show()
        self.hide()

    def show_howto(self):
        file_path = r'howto.text'
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # wrapped_content = textwrap.fill(content, width=70)
            QMessageBox.information(self, "วิธีใช้งาน",content)

class SecondWindow(QMainWindow):
    def __init__(self, data=None, vars=None):
        super().__init__()
        self.data = data
        self.vars = vars
        self.generated_edges = set()
        self.graph_image = None 
        self.circuit_image = None 
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("STG")
        self.setGeometry(400, 100, 780, 500)
        self.setStyleSheet('background-color: #2C4B82;color: #F7B4A7;font: bold 14px;') 

        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowIcon(QIcon('your_icon.png'))

        self.button_browse = QPushButton("Accept", self)
        self.button_browse.setGeometry(190, 230, 90, 45)
        self.button_browse.setStyleSheet("background-color:#F7B4A7;\n"
                                        "color: #2C4B82;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 5px;")
        self.button_browse.clicked.connect(self.accept_file1)

        if self.data is not None:
            self.text_edit_2 = QTextEdit(self)
            self.text_edit_2.setGeometry(140, 30, 500, 180)
            self.text_edit_2.setStyleSheet(
                """QTextEdit {background-color: #F7B4A7;color: black;border-radius:5px}""")
            self.text_edit_2.setPlainText(self.data)

        self.button_show = QPushButton("Back", self)
        self.button_show.setGeometry(490, 230, 90, 45)
        self.button_show.setStyleSheet("background-color:#F7B4A7;\n"
                                        "color: #2C4B82;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 5px;")
        self.button_show.clicked.connect(self.back_to_browse)

        self.svg_widget_circuit = QSvgWidget(self)
        self.svg_widget_circuit.setGeometry(400, 310, 275, 150)
        self.svg_widget_circuit.setStyleSheet('background-color: #F7B4A7; border-radius: 5px;')

        self.label_graph = QLabel(self)  # เพิ่ม QLabel สำหรับแสดงกราฟ
        self.label_graph.setGeometry(100, 310, 275, 150)
        self.label_graph.setStyleSheet('background-color: #F7B4A7; border-radius: 5px;')

        self.label_above_svg = QLabel("STG Graph", self)
        self.label_above_svg.setGeometry(100, 280, 100, 30)
        self.label_above_svg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.c_label_above_svg = QLabel("STG Circuit", self)
        self.c_label_above_svg.setGeometry(400, 280, 100, 30)
        self.c_label_above_svg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # เพิ่มปุ่ม "Save"
        self.button_save = QPushButton("Download", self)
        self.button_save.setGeometry(340, 230, 90, 45)
        self.button_save.setStyleSheet("background-color:#F7B4A7;\n"
                                        "color: #2C4B82;\n"
                                        "border-radius: 5px;\n"
                                        "padding: 5px;")
        self.button_save.clicked.connect(self.save_file)  # เชื่อมกับเมธอด save_file()
        
    def accept_file1(self):
        content = self.text_edit_2.toPlainText()

        lines = content.split('\n')    
        
        if len(lines) < 2:  # ตรวจสอบว่ามีคำน้อยกว่า 2 บรรทัดหรือไม่
            QMessageBox.warning(self, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร.")
            return
        if len(lines[0].split()) <= 3:
            QMessageBox.warning(None, "Warning", "ข้อมูลไม่ถูกต้องในการสร้างกราฟและวงจร")
            return
        
            # ตรวจสอบว่ามีคำว่า "path" ในข้อมูลหรือไม่
        found_path = False
        for line in lines:
            if "path" in line:
                found_path = True
                break

        # ถ้าไม่พบคำว่า "path" ให้แสดงหน้าต่างเตือน
        if not found_path:
            QMessageBox.warning(self, "Warning", "ข้อมูลไม่มีคำว่า 'path'")
            return

        for i, line in enumerate(lines[:len(self.vars)]):
            self.vars[i] = line

        for i, var1 in enumerate(self.vars):
            if var1.startswith("path"):
                all_text = var1.replace("p", "+").replace("m", "-")
                self.vars[i] = " ".join([a for a in all_text.split() if "+ath" not in a and ":" not in a])


        # แสดงกราฟ
        # self.graph_image = generate_graph(self.vars)  # เรียกใช้ฟังก์ชัน generate_graph() จากไฟล์ graph_generator.py
            # แสดงกราฟ
        # if len(lines) > 9:
        #     self.graph_image = graph_full(self.vars)  # เรียกใช้ฟังก์ชัน generate_graph() จากไฟล์ graph_generator.py
        if len(lines) > 9:
            self.graph_image = graph_vbe5b(self.vars)  # เรียกใช้ฟังก์ชัน generate_graph() จากไฟล์ graph_generator.py
        elif len(lines[0].split()) == 8:
            self.graph_image = graph_full(self.vars)  # เรียกใช้ฟังก์ชัน generate_graph() จากไฟล์ graph_generator.py
        elif len(lines[0].split()) == 10:
            self.graph_image = graph_chu133(self.vars)  # เรียกใช้ฟังก์ชัน generate_graph() จากไฟล์ graph_generator.py
        else:
            self.graph_image = graph_half(self.vars)  # เรียกใช้ฟังก์ชัน generate_graph() จากไฟล์ graph_generator.py ดึงข้อความที่เป็นตัวแรกของบรรทัดแรก
        

        # self.label_image.setPixmap(pixmap.scaled(QSize(400, 300), Qt.AspectRatioMode.KeepAspectRatio))
        # self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # แสดงกราฟใน QSvgWidget
        # svg_content = self.graph_image.pipe(format='svg').decode('utf-8')
        if self.graph_image:
            pixmap = QPixmap()  # สร้าง QPixmap
            pixmap.loadFromData(self.graph_image.pipe(format='png'))  # โหลดรูปภาพจาก Digraph โดยแปลงเป็นรูปแบบ PNG
            self.label_graph.setPixmap(pixmap)  # ใช้ QPixmap ในการแสดงรูปภาพใน QLabel


    #แสดง C-elemen
        # ตรวจสอบว่าบรรทัดแรกมีคำมากกว่า 7 หรือไม่
        if len(lines) > 9:
            text1 = self.text_edit_2.toPlainText().split('\n')
            circuit_svg_content = circuit_vbe5b(text1)
        elif len(lines[0].split()) == 8:
            # ใช้ฟังก์ชัน NAND_gate() สร้างวงจร
            text1 = self.text_edit_2.toPlainText().split('\n')  # ดึงข้อความที่เป็นตัวแรกของบรรทัดแรก
            circuit_svg_content = circuit_full(text1)
        elif len(lines[0].split()) == 10:
            text1 = self.text_edit_2.toPlainText().split('\n')
            circuit_svg_content = circuit_chu133(text1)
        else:
            # ใช้ฟังก์ชัน circuit_C() สร้างวงจร
            text1 = self.text_edit_2.toPlainText().split('\n')  # ดึงข้อความที่เป็นตัวแรกของบรรทัดแรก
            circuit_svg_content = circuit_half(text1)
        self.svg_widget_circuit.load(circuit_svg_content.encode('utf-8')) 

        # Resize the window to fit the graph and circuit SVGs
        self.svg_widget_circuit.setStyleSheet('background-color: #FFFFFF;')
        svg_size = self.label_graph.sizeHint()
        svg_margin = 10
        self.label_graph.setGeometry(100 + svg_margin, 310 + svg_margin, svg_size.width(), svg_size.height())
        self.label_above_svg.setGeometry(100, 280, 100, 30)
        self.c_label_above_svg.setGeometry(400, 280, 100, 30)
        svg_size1 = self.svg_widget_circuit.sizeHint()
        svg_margin1 = 10
        self.svg_widget_circuit.setGeometry(400 + svg_margin1, 310 + svg_margin1, svg_size1.width(), svg_size1.height())
        self.resize(520 + svg_size1.width() , 330 + svg_size.height() + 2 * svg_margin)

    def save_file(self):
        content = self.text_edit_2.toPlainText()

        # ตรวจสอบว่ามีรูปกราฟที่ถูกเก็บไว้หรือไม่
        if self.graph_image is None:
            QMessageBox.warning(self, "Warning", "ต้องทำการสร้างกราฟและวงจรก่อนที่จะดาวน์โหลด")
            return

        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF File", "")

        if file_path:
            # บันทึกรูปกราฟเป็นไฟล์ PDF
            if file_path.endswith('.pdf'):
                file_path += '.pdf'
            self.graph_image.render(file_path, format='pdf', quiet=False)

            # บันทึกข้อมูลที่ได้เป็นไฟล์ข้อความ
            text_file_path = os.path.splitext(file_path)[0] + '.txt'
            with open(text_file_path, 'w') as file:
                file.write(content)

            # Save the circuit image as well
            circuit_file_path = os.path.splitext(file_path)[0] + '_circuit.pdf'
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(circuit_file_path)
            painter = QPainter()
            painter.begin(printer)
            self.svg_widget_circuit.renderer().render(painter)
            painter.end()

    def try_2(self):
        content = self.text_edit_2.toPlainText()
        if content == "path : Rip Aop Rop Rim Aom Rom Rop Aip Rom Rim Aim Rop Aom Rom":
            popup = PopupWindow(self)
            popup.exec()
        else:
            QMessageBox.warning(self, "Warning", "Not Correct Please Try Again.")

    def back_to_browse(self):
        self.back_to_browse = FileBrowserApp()
        self.back_to_browse.show()
        self.hide()

    def back_to_original_state(self):
        self.text_edit_2.setHidden(False)
        self.button_show.setHidden(False)
        self.sender().setHidden(True)


class PopupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Pop-up')
        self.setGeometry(200, 200, 200, 100)
        layout = QVBoxLayout()
        label = QLabel('STG is Correct')
        layout.addWidget(label)
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileBrowserApp()
    window.show()
    sys.exit(app.exec())
